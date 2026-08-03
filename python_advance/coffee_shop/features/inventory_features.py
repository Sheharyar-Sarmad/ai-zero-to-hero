from database.db import Db
from middlewares.middleware import Middlewares
from dotenv import load_dotenv
import os
from typing import Literal, Optional, Union
import re
from bson import ObjectId
from validator.inventory_validator import InventoryValidator

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db = Db(mongo_uri)
db.create_collection("inventory")
inventory = db['inventory']

class Inventory:
    def __init__(
        self, 
        title: str = None,
        description: str = None, 
        weight: float = None, 
        stock: int = None, 
        price: float = None, 
        category: Literal["liquid", "solid"] = "liquid"
    ):
        self.title = title
        self.description = description
        self.weight = weight
        self.stock = stock
        self.price = price
        self.category = category
        self.is_authorized = False
        self.success = False
        self.validator = InventoryValidator()

    # Helper function for middleware checking of admin session
    @staticmethod
    def helper_is_admin() -> bool:
        if not Middlewares.is_admin():
            return False
        return True

    # CRUD Operations
    def add_inventory(self) -> dict:
        """
        Add new inventory item with validation
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
                stock=self.stock,
                price=self.price,
                category=self.category,
                weight=self.weight
            )
            
            if not validation_result["valid"]:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": validation_result["errors"]
                }
            
            # Prepare inventory data
            inventory_data = {
                "title": self.title.strip(),
                "description": self.description.strip(),
                "weight": float(self.weight),
                "stock": int(self.stock),
                "price": float(self.price),
                "category": self.category.lower()
            }
            
            # Check if title already exists
            existing = inventory.find_one({"title": inventory_data["title"]})
            if existing:
                return {
                    "success": False,
                    "message": f"Inventory with title '{self.title}' already exists!"
                }
            
            # Insert into database
            result = inventory.insert_one(inventory_data)
            
            if result.inserted_id:
                self.success = True
                inventory_data["_id"] = str(result.inserted_id)
                return {
                    "success": True,
                    "message": "Inventory added successfully!",
                    "data": inventory_data
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to add inventory!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def update_inventory(self, inventory_id: str, update_data: dict) -> dict:
        """
        Update inventory item with validation
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate inventory ID
            is_valid, message = self.validator.validate_inventory_id(inventory_id)
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
            
            # Validate individual fields in update data
            errors = {}
            if "title" in update_data:
                is_valid, message = self.validator.validate_title(update_data["title"])
                if not is_valid:
                    errors["title"] = message
                    # Check if title already exists
                    existing = inventory.find_one({"title": update_data["title"]})
                    if existing and str(existing["_id"]) != inventory_id:
                        errors["title"] = f"Title '{update_data['title']}' already exists!"
            
            if "description" in update_data:
                is_valid, message = self.validator.validate_description(update_data["description"])
                if not is_valid:
                    errors["description"] = message
            
            if "stock" in update_data:
                is_valid, message = self.validator.validate_stock(update_data["stock"])
                if not is_valid:
                    errors["stock"] = message
            
            if "price" in update_data:
                is_valid, message = self.validator.validate_price(update_data["price"])
                if not is_valid:
                    errors["price"] = message
            
            if "category" in update_data:
                is_valid, message = self.validator.validate_category(update_data["category"])
                if not is_valid:
                    errors["category"] = message
            
            if "weight" in update_data:
                is_valid, message = self.validator.validate_weight(update_data["weight"])
                if not is_valid:
                    errors["weight"] = message
            
            if errors:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": errors
                }
            
            # Update in database
            result = inventory.update_one(
                {"_id": ObjectId(inventory_id)},
                {"$set": update_data}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Inventory updated successfully!",
                    "modified_count": result.modified_count
                }
            else:
                return {
                    "success": False,
                    "message": "No inventory was updated! Item may not exist or no changes made."
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def delete_inventory(self, inventory_id: str) -> dict:
        """
        Delete inventory item
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate inventory ID
            is_valid, message = self.validator.validate_inventory_id(inventory_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if item exists
            existing = inventory.find_one({"_id": ObjectId(inventory_id)})
            if not existing:
                return {
                    "success": False,
                    "message": "Inventory item not found!"
                }
            
            result = inventory.delete_one({"_id": ObjectId(inventory_id)})
            
            if result.deleted_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Inventory deleted successfully!",
                    "deleted_item": {
                        "_id": str(existing["_id"]),
                        "title": existing.get("title")
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to delete inventory!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Read Operations with Pagination
    @staticmethod
    def get_inventory(inventory_id: str) -> dict:
        """
        Get single inventory item by ID
        """
        try:
            # Validate inventory ID
            is_valid, message = InventoryValidator.validate_inventory_id(inventory_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            result = inventory.find_one({"_id": ObjectId(inventory_id)})
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result
                }
            else:
                return {
                    "success": False,
                    "message": "Inventory not found!"
                }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_all_inventory(
        page: int = 1, 
        limit: int = 10,
        sort_by: str = "title",
        sort_order: Literal["asc", "desc"] = "asc",
        filter_criteria: Optional[dict] = None
    ) -> dict:
        """
        Get all inventory with pagination support
        """
        try:
            # Validate pagination parameters
            is_valid, message = InventoryValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = InventoryValidator.validate_limit(limit)
            if not is_valid:
                limit = 10
            
            is_valid, message = InventoryValidator.validate_sort_order(sort_order)
            if not is_valid:
                sort_order = "asc"
            
            # Calculate skip value
            skip = (page - 1) * limit
            
            # Build query filter
            query = {}
            if filter_criteria:
                query.update(filter_criteria)
            
            # Determine sort order
            sort_direction = 1 if sort_order == "asc" else -1
            
            # Get total count for pagination metadata
            total_count = inventory.count_documents(query)
            
            # Get paginated results
            cursor = inventory.find(query)
            cursor = cursor.sort(sort_by, sort_direction)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            # Convert ObjectId to string for JSON serialization
            for item in results:
                item["_id"] = str(item["_id"])
            
            # Calculate pagination metadata
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
                "message": f"Retrieved {len(results)} items from page {page} of {total_pages}"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Search with Pagination
    @staticmethod
    def search_inventory(
        search_term: str, 
        search_field: str = "title",
        page: int = 1,
        limit: int = 10
    ) -> dict:
        """
        Search inventory with pagination support
        """
        try:
            # Validate search term
            is_valid, message = InventoryValidator.validate_search_term(search_term)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate pagination parameters
            is_valid, message = InventoryValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = InventoryValidator.validate_limit(limit)
            if not is_valid:
                limit = 10
            
            # Calculate skip value
            skip = (page - 1) * limit
            
            # Create regex pattern for case-insensitive search
            regex_pattern = re.compile(search_term, re.IGNORECASE)
            
            # Build search query
            query = {search_field: {"$regex": regex_pattern}}
            
            # Get total count for pagination metadata
            total_count = inventory.count_documents(query)
            
            # Get paginated results
            cursor = inventory.find(query)
            cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            
            results = list(cursor)
            
            # Convert ObjectId to string for JSON serialization
            for item in results:
                item["_id"] = str(item["_id"])
            
            # Calculate pagination metadata
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

    # Stock Management
    def update_stock(self, inventory_id: str, new_stock: int) -> dict:
        """
        Update stock for an inventory item
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate inventory ID
            is_valid, message = self.validator.validate_inventory_id(inventory_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate new stock
            is_valid, message = self.validator.validate_stock(new_stock)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if item exists
            existing = inventory.find_one({"_id": ObjectId(inventory_id)})
            if not existing:
                return {
                    "success": False,
                    "message": "Inventory item not found!"
                }
            
            result = inventory.update_one(
                {"_id": ObjectId(inventory_id)},
                {"$set": {"stock": int(new_stock)}}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": f"Stock updated to {new_stock} successfully!",
                    "old_stock": existing.get("stock"),
                    "new_stock": new_stock
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to update stock!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def increase_stock(self, inventory_id: str, amount: int) -> dict:
        """
        Increase stock by a specific amount
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate inventory ID
            is_valid, message = self.validator.validate_inventory_id(inventory_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate amount
            is_valid, message = self.validator.validate_amount(amount)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if item exists
            existing = inventory.find_one({"_id": ObjectId(inventory_id)})
            if not existing:
                return {
                    "success": False,
                    "message": "Inventory item not found!"
                }
            
            result = inventory.update_one(
                {"_id": ObjectId(inventory_id)},
                {"$inc": {"stock": int(amount)}}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": f"Stock increased by {amount} successfully!",
                    "old_stock": existing.get("stock"),
                    "increase_amount": amount,
                    "new_stock": existing.get("stock", 0) + amount
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to increase stock!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def decrease_stock(self, inventory_id: str, amount: int) -> dict:
        """
        Decrease stock by a specific amount
        """
        try:
            self.success = False
            
            # Check admin authorization
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate inventory ID
            is_valid, message = self.validator.validate_inventory_id(inventory_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate amount
            is_valid, message = self.validator.validate_amount(amount)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if there's enough stock
            current_inventory = inventory.find_one({"_id": ObjectId(inventory_id)})
            if not current_inventory:
                return {
                    "success": False,
                    "message": "Inventory item not found!"
                }
            
            if current_inventory["stock"] < amount:
                return {
                    "success": False,
                    "message": f"Insufficient stock! Available: {current_inventory['stock']}, Requested: {amount}"
                }
            
            result = inventory.update_one(
                {"_id": ObjectId(inventory_id)},
                {"$inc": {"stock": -int(amount)}}
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": f"Stock decreased by {amount} successfully!",
                    "old_stock": current_inventory.get("stock"),
                    "decrease_amount": amount,
                    "new_stock": current_inventory.get("stock", 0) - amount
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to decrease stock!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Statistics
    @staticmethod
    def inventory_count() -> dict:
        """
        Get inventory statistics
        """
        try:
            total_count = inventory.count_documents({})
            
            # Get additional statistics
            pipeline = [
                {"$group": {
                    "_id": None,
                    "total_stock": {"$sum": "$stock"},
                    "average_price": {"$avg": "$price"},
                    "min_price": {"$min": "$price"},
                    "max_price": {"$max": "$price"},
                    "total_items": {"$sum": 1}
                }}
            ]
            
            stats = list(inventory.aggregate(pipeline))
            
            # Get category counts
            category_pipeline = [
                {"$group": {
                    "_id": "$category",
                    "count": {"$sum": 1},
                    "total_stock": {"$sum": "$stock"}
                }}
            ]
            category_stats = list(inventory.aggregate(category_pipeline))
            
            return {
                "success": True,
                "total_items": total_count,
                "statistics": stats[0] if stats else {},
                "category_breakdown": category_stats if category_stats else [],
                "message": "Inventory statistics retrieved successfully!"
            }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_low_stock_items(threshold: int = 10, page: int = 1, limit: int = 10) -> dict:
        """
        Get items with low stock
        """
        try:
            # Validate threshold
            if threshold < 0:
                threshold = 10
            
            # Validate pagination parameters
            is_valid, message = InventoryValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = InventoryValidator.validate_limit(limit)
            if not is_valid:
                limit = 10
            
            skip = (page - 1) * limit
            
            query = {"stock": {"$lte": threshold}}
            total_count = inventory.count_documents(query)
            
            cursor = inventory.find(query)
            cursor = cursor.sort("stock", 1)
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
                "threshold": threshold,
                "message": f"Found {total_count} items with stock at or below {threshold}"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }