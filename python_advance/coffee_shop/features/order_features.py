from database.db import Db
from middlewares.middleware import Middlewares
from dotenv import load_dotenv
import os
from typing import Literal, Optional, List, Dict, Any, Union
import re
from bson import ObjectId
from datetime import datetime, timedelta
from validator.order_validator import OrderValidator
from foods_features import Foods
from drinks_features import Drinks

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
db = Db(mongo_uri)
db.create_collection("orders")
orders = db['orders']

class Orders:
    def __init__(
        self,
        customer_name: str = None,
        phone_number: str = None,
        table_number: int = None,
        waiter_name: str = None,
        items: List[Dict[str, Any]] = None,
        discount: float = 0,
        payment_method: Literal["cash", "card", "online"] = "cash",
        notes: str = None,
        status: Literal["pending", "preparing", "ready", "served", "completed", "cancelled"] = "pending"
    ):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.table_number = table_number
        self.waiter_name = waiter_name
        self.items = items or []
        self.discount = discount
        self.payment_method = payment_method
        self.notes = notes
        self.status = status
        self.payment_status = "pending"
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.is_authorized = False
        self.success = False
        self.validator = OrderValidator()
        self.foods = Foods()
        self.drinks = Drinks()

    # Helper function for middleware checking of admin session
    @staticmethod
    def helper_is_admin() -> bool:
        if not Middlewares.is_admin():
            return False
        return True

    # Core Order Operations - No admin required for customers
    def place_order(self) -> dict:
        """
        Place a new order with full validation and stock deduction
        No admin required - customers can place orders
        """
        try:
            self.success = False
            
            # Validate all fields
            validation_result = self.validator.validate_all_fields(
                customer_name=self.customer_name,
                phone_number=self.phone_number,
                table_number=self.table_number,
                waiter_name=self.waiter_name,
                items=self.items,
                discount=self.discount,
                payment_method=self.payment_method,
                notes=self.notes,
                status=self.status
            )
            
            if not validation_result["valid"]:
                return {
                    "success": False,
                    "message": "Validation failed!",
                    "errors": validation_result["errors"]
                }
            
            # Verify all items are available
            availability_check = self._verify_items_availability()
            if not availability_check["success"]:
                return availability_check
            
            # Calculate billing
            self._calculate_billing()
            
            # Deduct inventory
            deduction_result = self._deduct_inventory()
            if not deduction_result["success"]:
                return deduction_result
            
            # Prepare order data
            order_data = {
                "customer_name": self.customer_name.strip(),
                "phone_number": self.phone_number,
                "table_number": self.table_number,
                "waiter_name": self.waiter_name,
                "items": self.items,
                "subtotal": self.subtotal,
                "tax": self.tax,
                "discount": self.discount,
                "total": self.total,
                "payment_method": self.payment_method.lower(),
                "payment_status": "pending",
                "status": self.status.lower(),
                "notes": self.notes,
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat()
            }
            
            # Insert into database
            result = orders.insert_one(order_data)
            
            if result.inserted_id:
                self.success = True
                order_data["_id"] = str(result.inserted_id)
                return {
                    "success": True,
                    "message": "Order placed successfully!",
                    "data": order_data,
                    "receipt": self.generate_receipt(order_data)
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to place order!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def _verify_items_availability(self) -> dict:
        """
        Verify all items in the order are available
        Internal method - no admin required
        """
        try:
            unavailable_items = []
            
            for item in self.items:
                item_type = item.get("type")
                item_id = item.get("item_id")
                quantity = item.get("quantity", 1)
                
                if item_type == "food":
                    result = self.foods.is_available(item_id)
                elif item_type == "drink":
                    result = self.drinks.is_available(item_id)
                else:
                    return {
                        "success": False,
                        "message": f"Unknown item type: {item_type}"
                    }
                
                if not result.get("available", False):
                    unavailable_items.append({
                        "title": item.get("title"),
                        "type": item_type,
                        "reason": result.get("reason", "Not available")
                    })
            
            if unavailable_items:
                return {
                    "success": False,
                    "message": "Some items are not available!",
                    "unavailable_items": unavailable_items
                }
            
            return {
                "success": True,
                "message": "All items are available!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error verifying availability: {str(err)}"
            }

    def _deduct_inventory(self) -> dict:
        """
        Deduct inventory for all items in the order
        Internal method - no admin required
        """
        try:
            deduction_results = []
            errors = []
            
            for item in self.items:
                item_type = item.get("type")
                item_id = item.get("item_id")
                quantity = item.get("quantity", 1)
                title = item.get("title")
                
                if item_type == "food":
                    result = self.foods.deduct_ingredients(item_id, quantity)
                elif item_type == "drink":
                    result = self.drinks.deduct_ingredients(item_id, quantity)
                else:
                    errors.append({
                        "title": title,
                        "error": f"Unknown item type: {item_type}"
                    })
                    continue
                
                if result.get("success"):
                    deduction_results.append({
                        "title": title,
                        "type": item_type,
                        "quantity": quantity,
                        "success": True
                    })
                else:
                    errors.append({
                        "title": title,
                        "type": item_type,
                        "error": result.get("message", "Failed to deduct inventory")
                    })
            
            if errors:
                return {
                    "success": False,
                    "message": "Some items failed to deduct inventory!",
                    "deduction_results": deduction_results,
                    "errors": errors
                }
            
            return {
                "success": True,
                "message": "Inventory deducted successfully!",
                "deduction_results": deduction_results
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error deducting inventory: {str(err)}"
            }

    def _calculate_billing(self) -> None:
        """
        Calculate subtotal, tax, discount, and total
        Internal method - no admin required
        """
        # Calculate subtotal
        self.subtotal = 0
        for item in self.items:
            self.subtotal += item.get("price", 0) * item.get("quantity", 1)
        
        # Calculate tax (10%)
        self.tax = round(self.subtotal * 0.10, 2)
        
        # Calculate total with discount
        self.total = self.subtotal + self.tax - self.discount
        
        # Ensure total is not negative
        if self.total < 0:
            self.total = 0

    def _revert_inventory(self, order: dict) -> dict:
        """
        Revert inventory for cancelled order
        Internal method - no admin required
        """
        try:
            reverted_items = []
            errors = []
            
            items = order.get("items", [])
            
            for item in items:
                item_type = item.get("type")
                item_title = item.get("title")
                quantity = item.get("quantity", 1)
                
                # Find the item in inventory
                inventory_item = db['inventory'].find_one({"title": item_title})
                if not inventory_item:
                    errors.append({
                        "title": item_title,
                        "error": "Item not found in inventory"
                    })
                    continue
                
                # Revert stock
                for ingredient in inventory_item.get("ingredients", []):
                    ingredient_name = ingredient.get("name")
                    ingredient_quantity = ingredient.get("quantity", 0) * quantity
                    
                    result = db['inventory'].update_one(
                        {"title": ingredient_name},
                        {"$inc": {"stock": ingredient_quantity}}
                    )
                    
                    if result.modified_count > 0:
                        reverted_items.append({
                            "ingredient": ingredient_name,
                            "quantity": ingredient_quantity
                        })
            
            if errors:
                return {
                    "success": False,
                    "message": "Some inventory items could not be reverted!",
                    "reverted_items": reverted_items,
                    "errors": errors
                }
            
            return {
                "success": True,
                "message": "Inventory reverted successfully!",
                "reverted_items": reverted_items
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error reverting inventory: {str(err)}"
            }

    # Order Status Management - Admin required
    def update_order_status(self, order_id: str, status: str) -> dict:
        """
        Update order status
        Admin required
        """
        try:
            self.success = False
            
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate status
            is_valid, message = self.validator.validate_order_status(status)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Validate order ID
            is_valid, message = self.validator.validate_order_id(order_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if order exists
            existing_order = orders.find_one({"_id": ObjectId(order_id)})
            if not existing_order:
                return {
                    "success": False,
                    "message": "Order not found!"
                }
            
            # Update order
            result = orders.update_one(
                {"_id": ObjectId(order_id)},
                {
                    "$set": {
                        "status": status.lower(),
                        "updated_at": datetime.utcnow().isoformat()
                    }
                }
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": f"Order status updated to '{status}' successfully!",
                    "old_status": existing_order.get("status"),
                    "new_status": status
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to update order status!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def cancel_order(self, order_id: str) -> dict:
        """
        Cancel an order and revert inventory
        Admin required
        """
        try:
            self.success = False
            
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate order ID
            is_valid, message = self.validator.validate_order_id(order_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if order exists
            existing_order = orders.find_one({"_id": ObjectId(order_id)})
            if not existing_order:
                return {
                    "success": False,
                    "message": "Order not found!"
                }
            
            # Check if order can be cancelled
            current_status = existing_order.get("status")
            if current_status in ["completed", "cancelled"]:
                return {
                    "success": False,
                    "message": f"Cannot cancel order with status '{current_status}'!"
                }
            
            # Revert inventory
            revert_result = self._revert_inventory(existing_order)
            if not revert_result["success"]:
                return revert_result
            
            # Update order status
            result = orders.update_one(
                {"_id": ObjectId(order_id)},
                {
                    "$set": {
                        "status": "cancelled",
                        "updated_at": datetime.utcnow().isoformat(),
                        "cancelled_at": datetime.utcnow().isoformat()
                    }
                }
            )
            
            if result.modified_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Order cancelled successfully!",
                    "reverted_inventory": revert_result.get("reverted_items", [])
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to cancel order!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    def complete_order(self, order_id: str) -> dict:
        """
        Mark order as completed
        Admin required
        """
        return self.update_order_status(order_id, "completed")

    # Read Operations - Some require admin, some don't
    @staticmethod
    def get_order(order_id: str) -> dict:
        """
        Get a single order by ID
        No admin required - customers can view their own orders
        """
        try:
            is_valid, message = OrderValidator.validate_order_id(order_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            result = orders.find_one({"_id": ObjectId(order_id)})
            if result:
                result["_id"] = str(result["_id"])
                return {
                    "success": True,
                    "data": result
                }
            else:
                return {
                    "success": False,
                    "message": "Order not found!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_all_orders(
        page: int = 1,
        limit: int = 10,
        sort_by: str = "created_at",
        sort_order: Literal["asc", "desc"] = "desc",
        filter_criteria: Optional[dict] = None
    ) -> dict:
        """
        Get all orders with pagination
        Admin required - to see all orders
        """
        try:
            # Check admin authorization
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            is_valid, message = OrderValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = OrderValidator.validate_limit(limit)
            if not is_valid:
                limit = 10
            
            skip = (page - 1) * limit
            
            query = {}
            if filter_criteria:
                query.update(filter_criteria)
            
            sort_direction = 1 if sort_order == "asc" else -1
            
            total_count = orders.count_documents(query)
            
            cursor = orders.find(query)
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
                "message": f"Retrieved {len(results)} orders from page {page} of {total_pages}"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Search Operations - Admin required for all searches
    @staticmethod
    def search_orders(
        search_term: str,
        search_field: str = "customer_name",
        page: int = 1,
        limit: int = 10
    ) -> dict:
        """
        Search orders with pagination
        Admin required
        """
        try:
            # Check admin authorization
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            is_valid, message = OrderValidator.validate_search_term(search_term)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            is_valid, message = OrderValidator.validate_page_number(page)
            if not is_valid:
                page = 1
            
            is_valid, message = OrderValidator.validate_limit(limit)
            if not is_valid:
                limit = 10
            
            skip = (page - 1) * limit
            
            regex_pattern = re.compile(search_term, re.IGNORECASE)
            query = {search_field: {"$regex": regex_pattern}}
            
            total_count = orders.count_documents(query)
            
            cursor = orders.find(query)
            cursor = cursor.sort("created_at", -1)
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

    @staticmethod
    def search_by_customer(customer_name: str, page: int = 1, limit: int = 10) -> dict:
        """
        Search orders by customer name
        Admin required
        """
        return Orders.search_orders(customer_name, "customer_name", page, limit)

    @staticmethod
    def search_by_date(start_date: str, end_date: str, page: int = 1, limit: int = 10) -> dict:
        """
        Search orders by date range
        Admin required
        """
        try:
            # Check admin authorization
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            is_valid, message = OrderValidator.validate_date_range(start_date, end_date)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            query = {
                "created_at": {
                    "$gte": start_date,
                    "$lte": end_date
                }
            }
            
            return Orders.get_all_orders(page, limit, "created_at", "desc", query)
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def search_by_status(status: str, page: int = 1, limit: int = 10) -> dict:
        """
        Search orders by status
        Admin required
        """
        try:
            # Check admin authorization
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            is_valid, message = OrderValidator.validate_order_status(status)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            return Orders.get_all_orders(page, limit, "created_at", "desc", {"status": status.lower()})
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Filter Methods - Admin required
    @staticmethod
    def get_pending_orders(page: int = 1, limit: int = 10) -> dict:
        """Get all pending orders - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.get_all_orders(page, limit, "created_at", "asc", {"status": "pending"})

    @staticmethod
    def get_preparing_orders(page: int = 1, limit: int = 10) -> dict:
        """Get all preparing orders - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.get_all_orders(page, limit, "created_at", "asc", {"status": "preparing"})

    @staticmethod
    def get_ready_orders(page: int = 1, limit: int = 10) -> dict:
        """Get all ready orders - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.get_all_orders(page, limit, "created_at", "asc", {"status": "ready"})

    @staticmethod
    def get_completed_orders(page: int = 1, limit: int = 10) -> dict:
        """Get all completed orders - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.get_all_orders(page, limit, "created_at", "desc", {"status": "completed"})

    @staticmethod
    def get_cancelled_orders(page: int = 1, limit: int = 10) -> dict:
        """Get all cancelled orders - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.get_all_orders(page, limit, "created_at", "desc", {"status": "cancelled"})

    @staticmethod
    def get_today_orders(page: int = 1, limit: int = 10) -> dict:
        """Get today's orders - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            today_end = datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
            
            query = {
                "created_at": {
                    "$gte": today_start,
                    "$lte": today_end
                }
            }
            
            return Orders.get_all_orders(page, limit, "created_at", "desc", query)
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_orders_between_dates(start_date: str, end_date: str, page: int = 1, limit: int = 10) -> dict:
        """Get orders between two dates - Admin required"""
        if not Middlewares.is_admin():
            return {
                "success": False,
                "message": "Login required! Admin access needed."
            }
        return Orders.search_by_date(start_date, end_date, page, limit)

    # Delete Operations - Admin required
    def delete_order(self, order_id: str) -> dict:
        """
        Delete an order (admin only)
        Admin required
        """
        try:
            self.success = False
            
            if not self.helper_is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            # Validate order ID
            is_valid, message = self.validator.validate_order_id(order_id)
            if not is_valid:
                return {
                    "success": False,
                    "message": message
                }
            
            # Check if order exists
            existing_order = orders.find_one({"_id": ObjectId(order_id)})
            if not existing_order:
                return {
                    "success": False,
                    "message": "Order not found!"
                }
            
            result = orders.delete_one({"_id": ObjectId(order_id)})
            
            if result.deleted_count > 0:
                self.success = True
                return {
                    "success": True,
                    "message": "Order deleted successfully!",
                    "deleted_item": {
                        "_id": str(existing_order["_id"]),
                        "customer_name": existing_order.get("customer_name")
                    }
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to delete order!"
                }
                
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    # Receipt Operations - No admin required for customers
    def generate_receipt(self, order_data: dict) -> dict:
        """
        Generate a receipt for an order
        No admin required - customers can view receipts
        """
        try:
            receipt = {
                "order_id": str(order_data.get("_id", "")),
                "customer_name": order_data.get("customer_name", ""),
                "date": order_data.get("created_at", datetime.utcnow().isoformat()),
                "items": [],
                "subtotal": order_data.get("subtotal", 0),
                "tax": order_data.get("tax", 0),
                "discount": order_data.get("discount", 0),
                "total": order_data.get("total", 0),
                "payment_method": order_data.get("payment_method", ""),
                "status": order_data.get("status", ""),
                "receipt_number": f"RCP-{datetime.utcnow().strftime('%Y%m%d')}-{order_data.get('_id', '')[:6]}"
            }
            
            # Add items
            for item in order_data.get("items", []):
                receipt["items"].append({
                    "title": item.get("title", ""),
                    "type": item.get("type", ""),
                    "quantity": item.get("quantity", 0),
                    "price": item.get("price", 0),
                    "total": item.get("price", 0) * item.get("quantity", 0)
                })
            
            return receipt
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error generating receipt: {str(err)}"
            }

    @staticmethod
    def print_receipt(order_id: str) -> dict:
        """
        Print receipt for an order
        No admin required - customers can view receipts
        """
        try:
            order_result = Orders.get_order(order_id)
            if not order_result["success"]:
                return order_result
            
            order_data = order_result["data"]
            
            # Format receipt for printing
            receipt = "=" * 50 + "\n"
            receipt += "          CAFE MANAGEMENT SYSTEM\n"
            receipt += "=" * 50 + "\n"
            receipt += f"Receipt #: RCP-{datetime.utcnow().strftime('%Y%m%d')}-{order_id[:6]}\n"
            receipt += f"Date: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\n"
            receipt += f"Customer: {order_data.get('customer_name', 'N/A')}\n"
            receipt += f"Table: {order_data.get('table_number', 'N/A')}\n"
            receipt += f"Waiter: {order_data.get('waiter_name', 'N/A')}\n"
            receipt += "-" * 50 + "\n"
            receipt += "Items:\n"
            
            for item in order_data.get("items", []):
                receipt += f"  {item.get('quantity', 0)}x {item.get('title', '')} "
                receipt += f"({item.get('type', '')}) - "
                receipt += f"${item.get('price', 0) * item.get('quantity', 0):.2f}\n"
            
            receipt += "-" * 50 + "\n"
            receipt += f"Subtotal: ${order_data.get('subtotal', 0):.2f}\n"
            receipt += f"Tax (10%): ${order_data.get('tax', 0):.2f}\n"
            receipt += f"Discount: ${order_data.get('discount', 0):.2f}\n"
            receipt += "-" * 50 + "\n"
            receipt += f"TOTAL: ${order_data.get('total', 0):.2f}\n"
            receipt += "=" * 50 + "\n"
            receipt += f"Payment: {order_data.get('payment_method', 'N/A')}\n"
            receipt += f"Status: {order_data.get('status', 'N/A')}\n"
            receipt += "=" * 50 + "\n"
            receipt += "Thank you for your order!\n"
            receipt += "=" * 50
            
            return {
                "success": True,
                "receipt": receipt,
                "message": "Receipt generated successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error printing receipt: {str(err)}"
            }

    @staticmethod
    def save_receipt_pdf(order_id: str) -> dict:
        """
        Save receipt as PDF
        No admin required - customers can save receipts
        """
        try:
            order_result = Orders.get_order(order_id)
            if not order_result["success"]:
                return order_result
            
            # In a real implementation, you would use a PDF library like ReportLab or fpdf
            # This is a placeholder that returns the receipt data
            
            return {
                "success": True,
                "message": "PDF receipt would be saved here",
                "data": order_result["data"]
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error saving receipt: {str(err)}"
            }

    # Statistics - Admin required for all statistics
    @staticmethod
    def total_orders() -> dict:
        """Get total number of orders - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            total = orders.count_documents({})
            return {
                "success": True,
                "total_orders": total,
                "message": "Total orders count retrieved successfully!"
            }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def today_orders() -> dict:
        """Get today's order count - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            today_end = datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
            
            query = {
                "created_at": {
                    "$gte": today_start,
                    "$lte": today_end
                }
            }
            
            count = orders.count_documents(query)
            return {
                "success": True,
                "today_orders": count,
                "message": "Today's orders count retrieved successfully!"
            }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def today_revenue() -> dict:
        """Get today's revenue - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            today_end = datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()
            
            pipeline = [
                {
                    "$match": {
                        "created_at": {"$gte": today_start, "$lte": today_end},
                        "status": {"$ne": "cancelled"}
                    }
                },
                {
                    "$group": {
                        "_id": None,
                        "total_revenue": {"$sum": "$total"},
                        "order_count": {"$sum": 1}
                    }
                }
            ]
            
            result = list(orders.aggregate(pipeline))
            
            if result:
                return {
                    "success": True,
                    "today_revenue": result[0]["total_revenue"],
                    "order_count": result[0]["order_count"],
                    "message": "Today's revenue retrieved successfully!"
                }
            else:
                return {
                    "success": True,
                    "today_revenue": 0,
                    "order_count": 0,
                    "message": "No orders found for today!"
                }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def weekly_revenue() -> dict:
        """Get weekly revenue - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            week_start = datetime.utcnow() - timedelta(days=7)
            week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            
            pipeline = [
                {
                    "$match": {
                        "created_at": {"$gte": week_start},
                        "status": {"$ne": "cancelled"}
                    }
                },
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": {"$toDate": "$created_at"}
                            }
                        },
                        "daily_revenue": {"$sum": "$total"},
                        "order_count": {"$sum": 1}
                    }
                },
                {"$sort": {"_id": 1}}
            ]
            
            result = list(orders.aggregate(pipeline))
            
            return {
                "success": True,
                "weekly_data": result,
                "total_orders": sum(r["order_count"] for r in result),
                "total_revenue": sum(r["daily_revenue"] for r in result),
                "message": "Weekly revenue retrieved successfully!"
            }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def monthly_revenue() -> dict:
        """Get monthly revenue - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            month_start = datetime.utcnow() - timedelta(days=30)
            month_start = month_start.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
            
            pipeline = [
                {
                    "$match": {
                        "created_at": {"$gte": month_start},
                        "status": {"$ne": "cancelled"}
                    }
                },
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": {"$toDate": "$created_at"}
                            }
                        },
                        "daily_revenue": {"$sum": "$total"},
                        "order_count": {"$sum": 1}
                    }
                },
                {"$sort": {"_id": 1}}
            ]
            
            result = list(orders.aggregate(pipeline))
            
            return {
                "success": True,
                "monthly_data": result,
                "total_orders": sum(r["order_count"] for r in result),
                "total_revenue": sum(r["daily_revenue"] for r in result),
                "message": "Monthly revenue retrieved successfully!"
            }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def best_selling_drink() -> dict:
        """Get best selling drink - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            pipeline = [
                {"$unwind": "$items"},
                {"$match": {"items.type": "drink"}},
                {
                    "$group": {
                        "_id": {
                            "title": "$items.title",
                            "item_id": "$items.item_id"
                        },
                        "total_sold": {"$sum": "$items.quantity"},
                        "total_revenue": {"$sum": {"$multiply": ["$items.price", "$items.quantity"]}}
                    }
                },
                {"$sort": {"total_sold": -1}},
                {"$limit": 1}
            ]
            
            result = list(orders.aggregate(pipeline))
            
            if result:
                return {
                    "success": True,
                    "best_selling_drink": result[0],
                    "message": "Best selling drink retrieved successfully!"
                }
            else:
                return {
                    "success": True,
                    "message": "No drinks found in orders!"
                }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def best_selling_food() -> dict:
        """Get best selling food - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            pipeline = [
                {"$unwind": "$items"},
                {"$match": {"items.type": "food"}},
                {
                    "$group": {
                        "_id": {
                            "title": "$items.title",
                            "item_id": "$items.item_id"
                        },
                        "total_sold": {"$sum": "$items.quantity"},
                        "total_revenue": {"$sum": {"$multiply": ["$items.price", "$items.quantity"]}}
                    }
                },
                {"$sort": {"total_sold": -1}},
                {"$limit": 1}
            ]
            
            result = list(orders.aggregate(pipeline))
            
            if result:
                return {
                    "success": True,
                    "best_selling_food": result[0],
                    "message": "Best selling food retrieved successfully!"
                }
            else:
                return {
                    "success": True,
                    "message": "No foods found in orders!"
                }
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }

    @staticmethod
    def get_full_statistics() -> dict:
        """Get complete order statistics - Admin required"""
        try:
            if not Middlewares.is_admin():
                return {
                    "success": False,
                    "message": "Login required! Admin access needed."
                }
            
            total_orders = orders.count_documents({})
            pending_orders = orders.count_documents({"status": "pending"})
            preparing_orders = orders.count_documents({"status": "preparing"})
            ready_orders = orders.count_documents({"status": "ready"})
            completed_orders = orders.count_documents({"status": "completed"})
            cancelled_orders = orders.count_documents({"status": "cancelled"})
            
            # Revenue statistics
            revenue_pipeline = [
                {"$match": {"status": {"$ne": "cancelled"}}},
                {"$group": {
                    "_id": None,
                    "total_revenue": {"$sum": "$total"},
                    "average_order_value": {"$avg": "$total"},
                    "max_order_value": {"$max": "$total"},
                    "min_order_value": {"$min": "$total"}
                }}
            ]
            revenue_stats = list(orders.aggregate(revenue_pipeline))
            
            # Get today's statistics
            today_stats = Orders.today_revenue()
            
            # Get best sellers
            best_food = Orders.best_selling_food()
            best_drink = Orders.best_selling_drink()
            
            return {
                "success": True,
                "statistics": {
                    "order_counts": {
                        "total": total_orders,
                        "pending": pending_orders,
                        "preparing": preparing_orders,
                        "ready": ready_orders,
                        "completed": completed_orders,
                        "cancelled": cancelled_orders
                    },
                    "revenue": {
                        "total_revenue": revenue_stats[0]["total_revenue"] if revenue_stats else 0,
                        "average_order_value": revenue_stats[0]["average_order_value"] if revenue_stats else 0,
                        "max_order_value": revenue_stats[0]["max_order_value"] if revenue_stats else 0,
                        "min_order_value": revenue_stats[0]["min_order_value"] if revenue_stats else 0,
                        "today_revenue": today_stats.get("today_revenue", 0)
                    },
                    "best_sellers": {
                        "best_food": best_food.get("best_selling_food") if best_food.get("success") else None,
                        "best_drink": best_drink.get("best_selling_drink") if best_drink.get("success") else None
                    }
                },
                "message": "Complete statistics retrieved successfully!"
            }
            
        except Exception as err:
            return {
                "success": False,
                "message": f"Error: {str(err)}"
            }