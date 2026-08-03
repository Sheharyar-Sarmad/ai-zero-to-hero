from database.db import Db
from middlewares.middleware import Middlewares
from dotenv import load_dotenv
import os
from typing import Literal, Optional, List, Dict, Any, Union
import re
from bson import ObjectId
from datetime import datetime
from validator.food_validtor import FoodValidator

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db = Db(mongo_uri)
db.create_collection("foods")
foods = db['foods']

class Foods:
    def __init__(
        self,
        title: str = None,
        description: str = None,
        ingredients: List[Dict[str, Any]] = None,
        price: float = None,
        status: Literal["available", "unavailable"] = "available",
        veg: bool = False,
        preparation_time: int = None,
        calories: int = None,
        image_url: str = None,
        featured: bool = False,
        is_spicy: bool = False
    ):
        self.title = title
        self.description = description
        self.ingredients = ingredients or []
        self.price = price
        self.status = status
        self.veg = veg
        self.preparation_time = preparation_time
        self.calories = calories
        self.image_url = image_url
        self.featured = featured
        self.is_spicy = is_spicy
        self.is_authorized = False
        self.success = False
        self.validator = FoodValidator()

    # Helper function for middleware checking of admin session
    @staticmethod
    def helper_is_admin() -> bool:
        if not Middlewares.is_admin():
            return False
        return True

    # ============================================
    # ADMIN ONLY OPERATIONS (Middleware Required)
    # ============================================

    # Create Operations - Admin Only
    def add_food(self) -> dict:
        """
        Add a new food with validation
        ADMIN ONLY
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate all fields
            validation_result = self.validator.validate_all_fields(
                title=self.title,
                description=self.description,
                price=self.price,
                ingredients=self.ingredients,
                status=self.status,
                veg=self.veg,
                preparation_time=self.preparation_time,
                calories=self.calories,
                image_url=self.image_url,
                featured=self.featured,
                is_spicy=self.is_spicy
            )
            
            if not validation_result["valid"]:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": validation_result["errors"]
                }
            
            # Check duplicate title
            existing = foods.find_one({"title": self.title.strip()})
            if existing:
                return {
                    "success": False,
                    "message": f"Food with title '{self.title}' already exists!"
                }
            
            # Verify all ingredients exist in inventory
            inventory_check = self._verify_ingredients_in_inventory(self.ingredients)
            if not inventory_check["success"]:
                return inventory_check
            
            # Prepare food data
            food_data = {
                "title": self.title.strip(),
                "description": self.description.strip(),
                "ingredients": self.ingredients,
                "price": float(self.price),
                "status": self.status.lower(),
                "veg": self.veg,
                "preparation_time": self.preparation_time,
                "calories": self.calories,
                "image_url": self.image_url,
                "featured": self.featured,
                "is_spicy": self.is_spicy,
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat()
            }
            
            # Insert into database
            result = foods.insert_one(food_data)
            
            if result.inserted_id:
                self.success = True
                food_data["_id"] = str(result.inserted_id)
                return {
                    "success": True,
                    "message": "Food added successfully!",
                    "data": food_data
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to add food!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Update Operations - Admin Only
    def update_food(self, food_id: str, update_data: dict) -> dict:
        """
        Update a food with validation
        ADMIN ONLY
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate food ID
            is_valid, message = self.validator.validate_food_id(food_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate update data
            is_valid, message = self.validator.validate_update_data(update_data)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if food exists
            existing_food = foods.find_one({"_id": ObjectId(food_id)})
            if not existing_food:
                return {
                    "success": False,
                    "message": "Food not found!"
                }
            
            # Validate individual fields
            errors = {}
            
            if "title" in update_data:
                is_valid, message = self.validator.validate_title(update_data["title"])
                if not is_valid:
                    errors["title"] = message
                else:
                    duplicate = foods.find_one({
                        "title": update_data["title"].strip(),
                        "_id": {"$ne": ObjectId(food_id)}
                    })
                    if duplicate:
                        errors["title"] = f"Title '{update_data['title']}' already exists!"
            
            if "description" in update_data:
                is_valid, message = self.validator.validate_description(update_data["description"])
                if not is_valid:
                    errors["description"] = message
            
            if "price" in update_data:
                is_valid, message = self.validator.validate_price(update_data["price"])
                if not is_valid:
                    errors["price"] = message
            
            if "ingredients" in update_data:
                is_valid, message = self.validator.validate_ingredients(update_data["ingredients"])
                if not is_valid:
                    errors["ingredients"] = message
                else:
                    inventory_check = self._verify_ingredients_in_inventory(update_data["ingredients"])
                    if not inventory_check["success"]:
                        errors["ingredients"] = inventory_check["message"]
            
            if "status" in update_data:
                is_valid, message = self.validator.validate_status(update_data["status"])
                if not is_valid:
                    errors["status"] = message
            
            if "veg" in update_data:
                if not isinstance(update_data["veg"], bool):
                    errors["veg"] = "Veg must be a boolean value!"
            
            if "preparation_time" in update_data:
                is_valid, message = self.validator.validate_preparation_time(update_data["preparation_time"])
                if not is_valid:
                    errors["preparation_time"] = message
            
            if "calories" in update_data:
                is_valid, message = self.validator.validate_calories(update_data["calories"])
                if not is_valid:
                    errors["calories"] = message
            
            if "image_url" in update_data:
                is_valid, message = self.validator.validate_image_url(update_data["image_url"])
                if not is_valid:
                    errors["image_url"] = message
            
            if "featured" in update_data:
                if not isinstance(update_data["featured"], bool):
                    errors["featured"] = "Featured must be a boolean value!"
            
            if "is_spicy" in update_data:
                if not isinstance(update_data["is_spicy"], bool):
                    errors["is_spicy"] = "Is spicy must be a boolean value!"
            
            if errors:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": errors
                }
            
            # Add updated_at timestamp
            update_data["updated_at"] = datetime.utcnow().isoformat()
            
            # Update in database
            result = foods.update_one(
                {"_id": ObjectId(food_id)},
                {"$set": update_data}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Food updated successfully!",
                    "modified_count": result.modified_count
                }
            else:
                return {
                    "success": False,
                    "message": "No changes were made to the food!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Delete Operations - Admin Only
    def delete_food(self, food_id: str) -> dict:
        """
        Delete a food by ID
        ADMIN ONLY
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate food ID
            is_valid, message = self.validator.validate_food_id(food_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if food exists
            existing_food = foods.find_one({"_id": ObjectId(food_id)})
            if not existing_food:
                return {
                    "success": False,
                    "message": "Food not found!"
                }
            
            result = foods.delete_one({"_id": ObjectId(food_id)})
            
            if result.deleted_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Food deleted successfully!",
                    "deleted_item": {
                        "_id": str(existing_food["_id"]),
                        "title": existing_food.get("title")
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to delete food!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Status Management - Admin Only
    def enable_food(self, food_id: str) -> dict:
        """Enable/available a food - ADMIN ONLY"""
        return self.update_food(food_id, {"status": "available"})

    def disable_food(self, food_id: str) -> dict:
        """Disable/unavailable a food - ADMIN ONLY"""
        return self.update_food(food_id, {"status": "unavailable"})

    def update_status(self, food_id: str, status: Literal["available", "unavailable"]) -> dict:
        """Update food status - ADMIN ONLY"""
        try:
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            is_valid, message = self.validator.validate_status(status)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            return self.update_food(food_id, {"status": status.lower()})
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # ============================================
    # PUBLIC OPERATIONS (No Middleware Required)
    # ============================================

    # Read Operations - Public
    @staticmethod
    def get_food(food_id: str) -> dict:
        """
        Get a single food by ID
        PUBLIC - No admin required
        """
        try:
            is_valid, message = FoodValidator.validate_food_id(food_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            result = foods.find_one({"_id": ObjectId(food_id)})
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result
                }
            else:
                return {
                    "success": False,
                    "message": "Food not found!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_all_foods(
        page: int = 1,
        limit: int = 9,
        sort_by: str = "title",
        sort_order: Literal["asc", "desc"] = "asc",
        filter_criteria: Optional[dict] = None
    ) -> dict:
        """
        Get all foods with pagination
        PUBLIC - No admin required
        """
        try:
            is_valid, message = FoodValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = FoodValidator.validate_limit(limit)
            if not is_valid:
                limit = 9
            
            skip = (page - 1) * limit
            
            query = {}
            if filter_criteria:
                query.update(filter_criteria)
            
            sort_direction = 1 if sort_order == "asc" else -1
            
            total_count = foods.count_documents(query)
            
            cursor = foods.find(query)
            cursor = cursor.sort(sort_by, sort_direction)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            for item in results:
                item["_id"] = str(item["_id"])
            
            total_pages = (total_count + limit - 1) // limit if total_count > 0 else 0
            
            return {
                "success": True,
                "data": results,
                "pagination": {
                    "current_page": page,
                    "per_page": limit,
                    "total_items": total_count,
                    "total_pages": total_pages,
                    "has_next": page < total_pages,
                    "has_previous": page > 1,
                    "next_page": page + 1 if page < total_pages else None,
                    "previous_page": page - 1 if page > 1 else None
                },
                "sort": {
                    "field": sort_by,
                    "order": sort_order
                },
                "message": f"Retrieved {len(results)} foods from page {page} of {total_pages}"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Search Operations - Public
    @staticmethod
    def search_foods(
        search_term: str,
        search_field: str = "title",
        page: int = 1,
        limit: int = 9
    ) -> dict:
        """
        Search foods with pagination
        PUBLIC - No admin required
        """
        try:
            is_valid, message = FoodValidator.validate_search_term(search_term)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            is_valid, message = FoodValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = FoodValidator.validate_limit(limit)
            if not is_valid:
                limit = 9
            
            skip = (page - 1) * limit
            
            regex_pattern = re.compile(search_term, re.IGNORECASE)
            query = {search_field: {"$regex": regex_pattern}}
            
            total_count = foods.count_documents(query)
            
            cursor = foods.find(query)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            for item in results:
                item["_id"] = str(item["_id"])
            
            total_pages = (total_count + limit - 1) // limit if total_count > 0 else 0
            
            return {
                "success": True,
                "data": results,
                "pagination": {
                    "current_page": page,
                    "per_page": limit,
                    "total_items": total_count,
                    "total_pages": total_pages,
                    "has_next": page < total_pages,
                    "has_previous": page > 1,
                    "next_page": page + 1 if page < total_pages else None,
                    "previous_page": page - 1 if page > 1 else None
                },
                "search": {
                    "term": search_term,
                    "field": search_field
                },
                "message": f"Found {total_count} results for '{search_term}'"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Specific Search Methods - Public
    @staticmethod
    def search_by_title(title: str, page: int = 1, limit: int = 9) -> dict:
        """Search foods by title - PUBLIC"""
        return Foods.search_foods(title, "title", page, limit)
    
    @staticmethod
    def search_by_price(min_price: float, max_price: float, page: int = 1, limit: int = 9) -> dict:
        """Search foods by price range - PUBLIC"""
        try:
            is_valid, message = FoodValidator.validate_price_range(min_price, max_price)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            query = {}
            if min_price is not None:
                query["price"] = {"$gte": min_price}
            if max_price is not None:
                query["price"] = {"$lte": max_price}
            
            if min_price is not None and max_price is not None:
                query["price"] = {"$gte": min_price, "$lte": max_price}
            
            return Foods.get_all_foods(page, limit, "price", "asc", query)
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }
    
    @staticmethod
    def search_by_status(status: str, page: int = 1, limit: int = 9) -> dict:
        """Search foods by status - PUBLIC (Only shows available)"""
        try:
            is_valid, message = FoodValidator.validate_status(status)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            return Foods.get_all_foods(page, limit, "title", "asc", {"status": status.lower()})
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Availability Operations - Internal/Public
    def is_available(self, food_id: str) -> dict:
        """
        Check if a food is available (all ingredients have enough stock)
        PUBLIC - Called during order placement
        """
        try:
            food = foods.find_one({"_id": ObjectId(food_id)})
            if not food:
                return {
                    "success": False,
                    "message": "Food not found!",
                    "available": False
                }
            
            if food.get("status") == "unavailable":
                return {
                    "success": True,
                    "available": False,
                    "message": "Food is currently unavailable!",
                    "reason": "Food status is set to unavailable"
                }
            
            ingredients = food.get("ingredients", [])
            if not ingredients:
                return {
                    "success": True,
                    "available": False,
                    "message": "No ingredients defined for this food!",
                    "reason": "Food has no ingredients"
                }
            
            insufficient_ingredients = []
            for ingredient in ingredients:
                inventory_item = db['inventory'].find_one({"title": ingredient["name"]})
                
                if not inventory_item:
                    insufficient_ingredients.append({
                        "name": ingredient["name"],
                        "reason": "Not found in inventory",
                        "required": ingredient.get("quantity", 0),
                        "available": 0
                    })
                    continue
                
                available_stock = inventory_item.get("stock", 0)
                required_quantity = ingredient.get("quantity", 0)
                
                if available_stock < required_quantity:
                    insufficient_ingredients.append({
                        "name": ingredient["name"],
                        "reason": "Insufficient stock",
                        "required": required_quantity,
                        "available": available_stock
                    })
            
            if insufficient_ingredients:
                return {
                    "success": True,
                    "available": False,
                    "message": "Food is not available!",
                    "insufficient_ingredients": insufficient_ingredients
                }
            
            return {
                "success": True,
                "available": True,
                "message": "Food is available!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}",
                "available": False
            }

    # Stock Deduction - Internal (No admin required - called automatically)
    def deduct_ingredients(self, food_id: str, quantity: int = 1) -> dict:
        """
        Deduct ingredients from inventory when order is placed
        INTERNAL - Called automatically, no admin required
        """
        try:
            self.success = False
            
            # No admin check - this is called automatically during order placement
            
            is_valid, message = self.validator.validate_food_id(food_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            food = foods.find_one({"_id": ObjectId(food_id)})
            if not food:
                return {
                    "success": False,
                    "message": "Food not found!"
                }
            
            if quantity <= 0:
                return {
                    "success": False,
                    "message": "Quantity must be greater than 0!"
                }
            
            if quantity > 100:
                return {
                    "success": False,
                    "message": "Quantity cannot exceed 100!"
                }
            
            availability = self.is_available(food_id)
            if not availability["success"]:
                return availability
            
            if not availability.get("available", False):
                return {
                    "success": False,
                    "message": "Food is not available!",
                    "details": availability
                }
            
            ingredients = food.get("ingredients", [])
            deduction_results = []
            errors = []
            
            for ingredient in ingredients:
                ingredient_name = ingredient["name"]
                required_quantity = ingredient["quantity"] * quantity
                
                result = db['inventory'].update_one(
                    {"title": ingredient_name},
                    {"$inc": {"stock": -required_quantity}}
                )
                
                if result.modified_count > 0:
                    deduction_results.append({
                        "name": ingredient_name,
                        "deducted": required_quantity,
                        "success": True
                    })
                else:
                    errors.append({
                        "name": ingredient_name,
                        "error": "Failed to deduct stock"
                    })
            
            if errors:
                return {
                    "success": False,
                    "message": "Some ingredients could not be deducted!",
                    "deductions": deduction_results,
                    "errors": errors
                }
            
            self.success = True
            return {
                "success": True,
                "message": f"Ingredients deducted successfully for {quantity} food item(s)!",
                "deductions": deduction_results
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Helper method - Internal
    def _verify_ingredients_in_inventory(self, ingredients: List[Dict[str, Any]]) -> dict:
        """
        Verify all ingredients exist in inventory
        INTERNAL - No admin required
        """
        try:
            for ingredient in ingredients:
                # Check if ingredient exists in inventory
                inventory_item = db['inventory'].find_one({"title": ingredient["name"]})
                
                if not inventory_item:
                    return {
                        "success": False,
                        "message": f"Ingredient '{ingredient['name']}' not found in inventory!"
                    }
                
                # Check if ingredient has enough stock
                if inventory_item.get("stock", 0) < ingredient.get("quantity", 0):
                    return {
                        "success": False,
                        "message": f"Insufficient stock for '{ingredient['name']}'! Available: {inventory_item.get('stock', 0)}, Required: {ingredient.get('quantity', 0)}"
                    }
            
            return {
                "success": True,
                "message": "All ingredients verified!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error verifying ingredients: {str(err)}"
            }

    # ============================================
    # PUBLIC FILTERS (No Middleware Required)
    # ============================================

    @staticmethod
    def get_available_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all available foods - PUBLIC"""
        return Foods.get_all_foods(page, limit, "title", "asc", {"status": "available"})

    @staticmethod
    def get_foods_by_price(min_price: float, max_price: float, page: int = 1, limit: int = 9) -> dict:
        """Get foods by price range - PUBLIC"""
        return Foods.search_by_price(min_price, max_price, page, limit)

    @staticmethod
    def get_foods_using_ingredient(ingredient_name: str, page: int = 1, limit: int = 9) -> dict:
        """Get foods that use a specific ingredient - PUBLIC"""
        try:
            if not ingredient_name or len(ingredient_name.strip()) == 0:
                return {
                    "success": False,
                    "message": "Ingredient name cannot be empty!"
                }
            
            query = {"ingredients.name": ingredient_name}
            return Foods.get_all_foods(page, limit, "title", "asc", query)
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_foods_without_ingredient(ingredient_name: str, page: int = 1, limit: int = 9) -> dict:
        """Get foods that don't use a specific ingredient - PUBLIC"""
        try:
            if not ingredient_name or len(ingredient_name.strip()) == 0:
                return {
                    "success": False,
                    "message": "Ingredient name cannot be empty!"
                }
            
            query = {"ingredients.name": {"$ne": ingredient_name}}
            return Foods.get_all_foods(page, limit, "title", "asc", query)
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_veg_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all vegetarian foods - PUBLIC"""
        return Foods.get_all_foods(page, limit, "title", "asc", {"veg": True})

    @staticmethod
    def get_non_veg_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all non-vegetarian foods - PUBLIC"""
        return Foods.get_all_foods(page, limit, "title", "asc", {"veg": False})

    @staticmethod
    def get_featured_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all featured foods - PUBLIC"""
        return Foods.get_all_foods(page, limit, "title", "asc", {"featured": True})

    @staticmethod
    def get_spicy_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all spicy foods - PUBLIC"""
        return Foods.get_all_foods(page, limit, "title", "asc", {"is_spicy": True})

    @staticmethod
    def get_unavailable_foods(page: int = 1, limit: int = 9) -> dict:
        """Get all unavailable foods - ADMIN ONLY"""
        # Check admin authorization
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Foods.get_all_foods(page, limit, "title", "asc", {"status": "unavailable"})

    # ============================================
    # PUBLIC PRICE INFO (No Middleware Required)
    # ============================================

    @staticmethod
    def highest_price_food() -> dict:
        """Get food with highest price - PUBLIC"""
        try:
            result = foods.find_one({}, sort=[("price", -1)])
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result,
                    "message": "Highest price food retrieved successfully!"
                }
            else:
                return {
                    "success": False,
                    "message": "No foods found!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def lowest_price_food() -> dict:
        """Get food with lowest price - PUBLIC"""
        try:
            result = foods.find_one({}, sort=[("price", 1)])
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result,
                    "message": "Lowest price food retrieved successfully!"
                }
            else:
                return {
                    "success": False,
                    "message": "No foods found!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # ============================================
    # ADMIN STATISTICS (Middleware Required)
    # ============================================

    @staticmethod
    def foods_count() -> dict:
        """Get total food count - ADMIN ONLY"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            total_count = foods.count_documents({})
            return {
                "success": True,
                "total_foods": total_count,
                "message": "Food count retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def available_foods_count() -> dict:
        """Get available food count - ADMIN ONLY"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            available_count = foods.count_documents({"status": "available"})
            return {
                "success": True,
                "available_foods": available_count,
                "message": "Available food count retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def unavailable_foods_count() -> dict:
        """Get unavailable food count - ADMIN ONLY"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            unavailable_count = foods.count_documents({"status": "unavailable"})
            return {
                "success": True,
                "unavailable_foods": unavailable_count,
                "message": "Unavailable food count retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def average_price() -> dict:
        """Get average food price - ADMIN ONLY"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            pipeline = [
                {"$group": {
                    "_id": None,
                    "average_price": {"$avg": "$price"}
                }}
            ]
            result = list(foods.aggregate(pipeline))
            
            return {
                "success": True,
                "average_price": result[0]["average_price"] if result else 0,
                "message": "Average price retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_full_statistics() -> dict:
        """Get complete food statistics - ADMIN ONLY"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            total_count = foods.count_documents({})
            available_count = foods.count_documents({"status": "available"})
            unavailable_count = foods.count_documents({"status": "unavailable"})
            
            veg_count = foods.count_documents({"veg": True})
            non_veg_count = foods.count_documents({"veg": False})
            
            featured_count = foods.count_documents({"featured": True})
            spicy_count = foods.count_documents({"is_spicy": True})
            
            pipeline = [
                {"$group": {
                    "_id": None,
                    "average_price": {"$avg": "$price"},
                    "min_price": {"$min": "$price"},
                    "max_price": {"$max": "$price"},
                    "total_foods": {"$sum": 1}
                }}
            ]
            stats = list(foods.aggregate(pipeline))
            
            # Category breakdown
            category_pipeline = [
                {"$group": {
                    "_id": "$status",
                    "count": {"$sum": 1}
                }}
            ]
            status_stats = list(foods.aggregate(category_pipeline))
            
            return {
                "success": True,
                "statistics": {
                    "total_foods": total_count,
                    "available_foods": available_count,
                    "unavailable_foods": unavailable_count,
                    "veg_foods": veg_count,
                    "non_veg_foods": non_veg_count,
                    "featured_foods": featured_count,
                    "spicy_foods": spicy_count,
                    "average_price": stats[0]["average_price"] if stats else 0,
                    "min_price": stats[0]["min_price"] if stats else 0,
                    "max_price": stats[0]["max_price"] if stats else 0,
                    "status_breakdown": status_stats if status_stats else []
                },
                "message": "Food statistics retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }