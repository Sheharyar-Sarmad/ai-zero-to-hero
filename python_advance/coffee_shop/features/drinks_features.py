from database.db import Db
from middlewares.middleware import Middlewares
from dotenv import load_dotenv
import os
from typing import Literal, Optional, List, Dict, Any
import re
from bson import ObjectId
from validator.drinks_validtor import DrinkValidator
from inventory_features import Inventory

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db = Db(mongo_uri)
db.create_collection("drinks")
drinks = db['drinks']

class Drinks:
    def __init__(
        self,
        title: str = None,
        description: str = None,
        ingredients: List[Dict[str, Any]] = None,
        price: float = None,
        status: Literal["available", "unavailable"] = "available"
    ):
        self.title = title
        self.description = description
        self.ingredients = ingredients or []
        self.price = price
        self.status = status
        self.is_authorized = False
        self.success = False
        self.validator = DrinkValidator()

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
    def add_drink(self) -> dict:
        """
        Add a new drink with validation
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
                status=self.status
            )
            
            if not validation_result["valid"]:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": validation_result["errors"]
                }
            
            # Check duplicate title
            existing = drinks.find_one({"title": self.title.strip()})
            if existing:
                return {
                    "success": False,
                    "message": f"Drink with title '{self.title}' already exists!"
                }
            
            # Verify all ingredients exist in inventory
            inventory_check = self._verify_ingredients_in_inventory(self.ingredients)
            if not inventory_check["success"]:
                return inventory_check
            
            # Prepare drink data
            drink_data = {
                "title": self.title.strip(),
                "description": self.description.strip(),
                "ingredients": self.ingredients,
                "price": float(self.price),
                "status": self.status.lower(),
                "created_at": db.get_current_timestamp() if hasattr(db, 'get_current_timestamp') else None
            }
            
            # Insert into database
            result = drinks.insert_one(drink_data)
            
            if result.inserted_id:
                self.success = True
                drink_data["_id"] = str(result.inserted_id)
                return {
                    "success": True,
                    "message": "Drink added successfully!",
                    "data": drink_data
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to add drink!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Update Operations - Admin Only
    def update_drink(self, drink_id: str, update_data: dict) -> dict:
        """
        Update a drink with validation
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
            
            # Validate drink ID
            is_valid, message = self.validator.validate_drink_id(drink_id)
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
            
            # Check if drink exists
            existing_drink = drinks.find_one({"_id": ObjectId(drink_id)})
            if not existing_drink:
                return {
                    "success": False,
                    "message": "Drink not found!"
                }
            
            # Validate individual fields
            errors = {}
            
            if "title" in update_data:
                is_valid, message = self.validator.validate_title(update_data["title"])
                if not is_valid:
                    errors["title"] = message
                else:
                    # Check duplicate title
                    duplicate = drinks.find_one({
                        "title": update_data["title"].strip(),
                        "_id": {"$ne": ObjectId(drink_id)}
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
                    # Verify ingredients exist in inventory
                    inventory_check = self._verify_ingredients_in_inventory(update_data["ingredients"])
                    if not inventory_check["success"]:
                        errors["ingredients"] = inventory_check["message"]
            
            if "status" in update_data:
                is_valid, message = self.validator.validate_status(update_data["status"])
                if not is_valid:
                    errors["status"] = message
            
            if errors:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": errors
                }
            
            # Update in database
            result = drinks.update_one(
                {"_id": ObjectId(drink_id)},
                {"$set": update_data}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Drink updated successfully!",
                    "modified_count": result.modified_count
                }
            else:
                return {
                    "success": False,
                    "message": "No changes were made to the drink!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Delete Operations - Admin Only
    def delete_drink(self, drink_id: str) -> dict:
        """
        Delete a drink by ID
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
            
            # Validate drink ID
            is_valid, message = self.validator.validate_drink_id(drink_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if drink exists
            existing_drink = drinks.find_one({"_id": ObjectId(drink_id)})
            if not existing_drink:
                return {
                    "success": False,
                    "message": "Drink not found!"
                }
            
            result = drinks.delete_one({"_id": ObjectId(drink_id)})
            
            if result.deleted_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Drink deleted successfully!",
                    "deleted_item": {
                        "_id": str(existing_drink["_id"]),
                        "title": existing_drink.get("title")
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to delete drink!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Status Management - Admin Only
    def enable_drink(self, drink_id: str) -> dict:
        """
        Enable/available a drink
        ADMIN ONLY
        """
        return self.update_drink(drink_id, {"status": "available"})

    def disable_drink(self, drink_id: str) -> dict:
        """
        Disable/unavailable a drink
        ADMIN ONLY
        """
        return self.update_drink(drink_id, {"status": "unavailable"})

    def update_status(self, drink_id: str, status: Literal["available", "unavailable"]) -> dict:
        """
        Update drink status
        ADMIN ONLY
        """
        try:
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate status
            is_valid, message = self.validator.validate_status(status)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            return self.update_drink(drink_id, {"status": status.lower()})
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Stock Deduction - Admin Only (Changes inventory)
    def deduct_ingredients(self, drink_id: str, quantity: int = 1) -> dict:
        """
        Deduct ingredients from inventory when order is placed
        ADMIN ONLY - This modifies inventory
        """
        try:
            self.success = False
            
            # Check admin authorization - This modifies inventory
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate drink ID
            is_valid, message = self.validator.validate_drink_id(drink_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Get the drink
            drink = drinks.find_one({"_id": ObjectId(drink_id)})
            if not drink:
                return {
                    "success": False,
                    "message": "Drink not found!"
                }
            
            # Validate quantity
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
            
            # Check availability
            availability = self.is_available(drink_id)
            if not availability["success"]:
                return availability
            
            if not availability.get("available", False):
                return {
                    "success": False,
                    "message": "Drink is not available!",
                    "details": availability
                }
            
            # Deduct ingredients
            ingredients = drink.get("ingredients", [])
            deduction_results = []
            errors = []
            
            for ingredient in ingredients:
                ingredient_name = ingredient["name"]
                required_quantity = ingredient["quantity"] * quantity
                
                # Update inventory
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
                "message": f"Ingredients deducted successfully for {quantity} drink(s)!",
                "deductions": deduction_results
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # ============================================
    # INTERNAL HELPER (No Middleware Required)
    # ============================================

    def _verify_ingredients_in_inventory(self, ingredients: List[Dict[str, Any]]) -> dict:
        """
        Verify all ingredients exist in inventory
        INTERNAL HELPER - Called internally, no admin required
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
                
                # Check if ingredient has enough stock (optional)
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
    # PUBLIC READ OPERATIONS (No Middleware Required)
    # ============================================

    # Read Operations - Public
    @staticmethod
    def get_drink(drink_id: str) -> dict:
        """
        Get a single drink by ID
        PUBLIC - No admin required
        """
        try:
            # Validate drink ID
            is_valid, message = DrinkValidator.validate_drink_id(drink_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            result = drinks.find_one({"_id": ObjectId(drink_id)})
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result
                }
            else:
                return {
                    "success": False,
                    "message": "Drink not found!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_all_drinks(
        page: int = 1,
        limit: int = 9,
        sort_by: str = "title",
        sort_order: Literal["asc", "desc"] = "asc",
        filter_criteria: Optional[dict] = None
    ) -> dict:
        """
        Get all drinks with pagination
        PUBLIC - No admin required
        """
        try:
            # Validate pagination parameters
            is_valid, message = DrinkValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = DrinkValidator.validate_limit(limit)
            if not is_valid:
                limit = 9
            
            # Calculate skip value
            skip = (page - 1) * limit
            
            # Build query filter
            query = {}
            if filter_criteria:
                query.update(filter_criteria)
            
            # Determine sort order
            sort_direction = 1 if sort_order == "asc" else -1
            
            # Get total count
            total_count = drinks.count_documents(query)
            
            # Get paginated results
            cursor = drinks.find(query)
            cursor = cursor.sort(sort_by, sort_direction)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            # Convert ObjectId to string
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
                "message": f"Retrieved {len(results)} drinks from page {page} of {total_pages}"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Search Operations - Public
    @staticmethod
    def search_drinks(
        search_term: str,
        search_field: str = "title",
        page: int = 1,
        limit: int = 9
    ) -> dict:
        """
        Search drinks with pagination
        PUBLIC - No admin required
        """
        try:
            # Validate search term
            is_valid, message = DrinkValidator.validate_search_term(search_term)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate pagination parameters
            is_valid, message = DrinkValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = DrinkValidator.validate_limit(limit)
            if not is_valid:
                limit = 9
            
            # Calculate skip value
            skip = (page - 1) * limit
            
            # Create regex pattern
            regex_pattern = re.compile(search_term, re.IGNORECASE)
            
            # Build search query
            query = {search_field: {"$regex": regex_pattern}}
            
            # Get total count
            total_count = drinks.count_documents(query)
            
            # Get paginated results
            cursor = drinks.find(query)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            # Convert ObjectId to string
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

    # Availability Operations - Public
    def is_available(self, drink_id: str) -> dict:
        """
        Check if a drink is available (all ingredients have enough stock)
        PUBLIC - Called during order placement, only reads data
        """
        try:
            # Get the drink
            drink = drinks.find_one({"_id": ObjectId(drink_id)})
            if not drink:
                return {
                    "success": False,
                    "message": "Drink not found!",
                    "available": False
                }
            
            # Check drink status
            if drink.get("status") == "unavailable":
                return {
                    "success": True,
                    "available": False,
                    "message": "Drink is currently unavailable!",
                    "reason": "Drink status is set to unavailable"
                }
            
            # Check ingredients
            ingredients = drink.get("ingredients", [])
            if not ingredients:
                return {
                    "success": True,
                    "available": False,
                    "message": "No ingredients defined for this drink!",
                    "reason": "Drink has no ingredients"
                }
            
            # Verify each ingredient
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
                    "message": "Drink is not available!",
                    "insufficient_ingredients": insufficient_ingredients
                }
            
            return {
                "success": True,
                "available": True,
                "message": "Drink is available!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}",
                "available": False
            }

    # Get Available Drinks - Public
    @staticmethod
    def get_available_drinks(page: int = 1, limit: int = 9) -> dict:
        """
        Get all available drinks
        PUBLIC - Customers can view available drinks
        """
        try:
            # Validate pagination parameters
            is_valid, message = DrinkValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = DrinkValidator.validate_limit(limit)
            if not is_valid:
                limit = 9
            
            skip = (page - 1) * limit
            
            query = {"status": "available"}
            total_count = drinks.count_documents(query)
            
            cursor = drinks.find(query)
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
                    "has_previous": page > 1
                },
                "message": f"Found {total_count} available drinks"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Statistics - Public (Read only, no sensitive data)
    @staticmethod
    def drinks_count() -> dict:
        """
        Get drinks statistics
        PUBLIC - Can be shown on customer side
        """
        try:
            total_count = drinks.count_documents({})
            
            # Get additional statistics
            pipeline = [
                {"$group": {
                    "_id": None,
                    "average_price": {"$avg": "$price"},
                    "min_price": {"$min": "$price"},
                    "max_price": {"$max": "$price"},
                    "total_items": {"$sum": 1}
                }}
            ]
            
            stats = list(drinks.aggregate(pipeline))
            
            # Get status counts
            status_pipeline = [
                {"$group": {
                    "_id": "$status",
                    "count": {"$sum": 1}
                }}
            ]
            status_stats = list(drinks.aggregate(status_pipeline))
            
            return {
                "success": True,
                "total_drinks": total_count,
                "statistics": stats[0] if stats else {},
                "status_breakdown": status_stats if status_stats else [],
                "message": "Drinks statistics retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }