import re
from typing import List, Dict, Any, Union, Optional
from datetime import datetime

class OrderValidator:
    """All validation methods for Order management"""
    
    @staticmethod
    def validate_order_id(order_id: str) -> tuple[bool, str]:
        """
        Validate order ID format
        """
        if not order_id:
            return False, "Order ID cannot be empty!"
        
        if not isinstance(order_id, str):
            return False, "Order ID must be a string!"
        
        if not re.fullmatch(r'^[0-9a-fA-F]{24}$', order_id):
            return False, "Invalid order ID format!"
        
        return True, "Order ID is valid"
    
    @staticmethod
    def validate_customer_name(name: str) -> tuple[bool, str]:
        """
        Validate customer name
        """
        if not name or len(name.strip()) == 0:
            return False, "Customer name cannot be empty!"
        
        if len(name) < 2:
            return False, "Customer name must be at least 2 characters long!"
        
        if len(name) > 50:
            return False, "Customer name cannot exceed 50 characters!"
        
        if not re.fullmatch(r"[A-Za-z ]+", name):
            return False, "Customer name can only contain letters and spaces!"
        
        return True, "Customer name is valid"
    
    @staticmethod
    def validate_phone_number(phone: str) -> tuple[bool, str]:
        """
        Validate phone number
        """
        if not phone or len(phone.strip()) == 0:
            return True, "Phone number is optional"  # Optional field
        
        if not re.fullmatch(r'^[0-9+\-() ]+$', phone):
            return False, "Phone number contains invalid characters!"
        
        if len(phone) < 7 or len(phone) > 20:
            return False, "Phone number must be between 7 and 20 characters!"
        
        return True, "Phone number is valid"
    
    @staticmethod
    def validate_table_number(table: Union[int, str]) -> tuple[bool, str]:
        """
        Validate table number
        """
        if table is None:
            return True, "Table number is optional"
        
        try:
            table_num = int(table)
            if table_num < 1:
                return False, "Table number must be at least 1!"
            
            if table_num > 100:
                return False, "Table number cannot exceed 100!"
            
            return True, "Table number is valid"
        except (ValueError, TypeError):
            return False, "Table number must be a valid number!"
    
    @staticmethod
    def validate_waiter_name(name: str) -> tuple[bool, str]:
        """
        Validate waiter name
        """
        if not name or len(name.strip()) == 0:
            return True, "Waiter name is optional"
        
        if len(name) < 2:
            return False, "Waiter name must be at least 2 characters long!"
        
        if len(name) > 50:
            return False, "Waiter name cannot exceed 50 characters!"
        
        if not re.fullmatch(r"[A-Za-z ]+", name):
            return False, "Waiter name can only contain letters and spaces!"
        
        return True, "Waiter name is valid"
    
    @staticmethod
    def validate_items(items: List[Dict[str, Any]]) -> tuple[bool, str]:
        """
        Validate order items
        """
        if not items:
            return False, "Order must contain at least one item!"
        
        if not isinstance(items, list):
            return False, "Items must be a list!"
        
        if len(items) > 50:
            return False, "Order cannot have more than 50 items!"
        
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                return False, f"Item at position {idx + 1} must be a dictionary!"
            
            # Check required fields
            required_fields = ["type", "item_id", "title", "price", "quantity"]
            for field in required_fields:
                if field not in item:
                    return False, f"Item at position {idx + 1} missing '{field}' field!"
            
            # Validate type
            if item["type"] not in ["food", "drink"]:
                return False, f"Item type must be 'food' or 'drink', got '{item['type']}'!"
            
            # Validate item_id
            if not item["item_id"] or not isinstance(item["item_id"], str):
                return False, f"Item ID for '{item.get('title', 'unknown')}' is invalid!"
            
            # Validate title
            if not item["title"] or len(item["title"].strip()) == 0:
                return False, f"Item title at position {idx + 1} is empty!"
            
            # Validate price
            if not isinstance(item["price"], (int, float)):
                return False, f"Price for '{item['title']}' must be a number!"
            
            if item["price"] <= 0:
                return False, f"Price for '{item['title']}' must be greater than 0!"
            
            # Validate quantity
            if not isinstance(item["quantity"], int):
                return False, f"Quantity for '{item['title']}' must be an integer!"
            
            if item["quantity"] <= 0:
                return False, f"Quantity for '{item['title']}' must be at least 1!"
            
            if item["quantity"] > 100:
                return False, f"Quantity for '{item['title']}' cannot exceed 100!"
        
        return True, "Items are valid"
    
    @staticmethod
    def validate_payment_method(method: str) -> tuple[bool, str]:
        """
        Validate payment method
        """
        valid_methods = ["cash", "card", "online"]
        
        if not method:
            return False, "Payment method cannot be empty!"
        
        if method.lower() not in valid_methods:
            return False, f"Payment method must be one of: {', '.join(valid_methods)}!"
        
        return True, "Payment method is valid"
    
    @staticmethod
    def validate_payment_status(status: str) -> tuple[bool, str]:
        """
        Validate payment status
        """
        valid_statuses = ["pending", "paid", "refunded"]
        
        if not status:
            return False, "Payment status cannot be empty!"
        
        if status.lower() not in valid_statuses:
            return False, f"Payment status must be one of: {', '.join(valid_statuses)}!"
        
        return True, "Payment status is valid"
    
    @staticmethod
    def validate_order_status(status: str) -> tuple[bool, str]:
        """
        Validate order status
        """
        valid_statuses = ["pending", "preparing", "ready", "served", "completed", "cancelled"]
        
        if not status:
            return False, "Order status cannot be empty!"
        
        if status.lower() not in valid_statuses:
            return False, f"Order status must be one of: {', '.join(valid_statuses)}!"
        
        return True, "Order status is valid"
    
    @staticmethod
    def validate_discount(discount: Union[int, float]) -> tuple[bool, str]:
        """
        Validate discount amount
        """
        if discount is None:
            return True, "Discount is optional"
        
        if not isinstance(discount, (int, float)):
            return False, "Discount must be a number!"
        
        if discount < 0:
            return False, "Discount cannot be negative!"
        
        if discount > 1000:
            return False, "Discount cannot exceed 1000!"
        
        return True, "Discount is valid"
    
    @staticmethod
    def validate_notes(notes: str) -> tuple[bool, str]:
        """
        Validate order notes
        """
        if not notes:
            return True, "Notes are optional"
        
        if len(notes) > 500:
            return False, "Notes cannot exceed 500 characters!"
        
        return True, "Notes are valid"
    
    @staticmethod
    def validate_search_term(search_term: str) -> tuple[bool, str]:
        """
        Validate search term
        """
        if not search_term or len(search_term.strip()) == 0:
            return False, "Search term cannot be empty!"
        
        if len(search_term) < 2:
            return False, "Search term must be at least 2 characters long!"
        
        if len(search_term) > 100:
            return False, "Search term cannot exceed 100 characters!"
        
        return True, "Search term is valid"
    
    @staticmethod
    def validate_page_number(page: int) -> tuple[bool, str]:
        """
        Validate page number for pagination
        """
        if not isinstance(page, int):
            return False, "Page number must be an integer!"
        
        if page < 1:
            return False, "Page number must be at least 1!"
        
        if page > 1000:
            return False, "Page number cannot exceed 1000!"
        
        return True, "Page number is valid"
    
    @staticmethod
    def validate_limit(limit: int) -> tuple[bool, str]:
        """
        Validate limit for pagination
        """
        if not isinstance(limit, int):
            return False, "Limit must be an integer!"
        
        if limit < 1:
            return False, "Limit must be at least 1!"
        
        if limit > 100:
            return False, "Limit cannot exceed 100!"
        
        return True, "Limit is valid"
    
    @staticmethod
    def validate_date_range(start_date: str, end_date: str) -> tuple[bool, str]:
        """
        Validate date range
        """
        try:
            if not start_date or not end_date:
                return False, "Both start and end dates are required!"
            
            # Try to parse dates
            start = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
            end = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
            
            if start > end:
                return False, "Start date cannot be after end date!"
            
            return True, "Date range is valid"
        except ValueError:
            return False, "Invalid date format! Use ISO format (YYYY-MM-DDTHH:MM:SS)"
    
    @staticmethod
    def validate_update_data(update_data: dict) -> tuple[bool, str]:
        """
        Validate update data dictionary
        """
        if not update_data:
            return False, "Update data cannot be empty!"
        
        if not isinstance(update_data, dict):
            return False, "Update data must be a dictionary!"
        
        valid_fields = ["status", "payment_status", "notes", "discount", "waiter_name", "table_number"]
        has_valid_field = any(field in update_data for field in valid_fields)
        
        if not has_valid_field:
            return False, f"Update data must contain at least one valid field: {', '.join(valid_fields)}!"
        
        return True, "Update data is valid"
    
    @staticmethod
    def validate_all_fields(
        customer_name: str = None,
        phone_number: str = None,
        table_number: int = None,
        waiter_name: str = None,
        items: List[Dict[str, Any]] = None,
        discount: Union[int, float] = None,
        payment_method: str = None,
        payment_status: str = None,
        notes: str = None,
        status: str = None
    ) -> dict:
        """
        Validate all order fields at once
        """
        results = {
            "valid": True,
            "errors": {},
            "messages": {}
        }
        
        if customer_name is not None:
            is_valid, message = OrderValidator.validate_customer_name(customer_name)
            if not is_valid:
                results["valid"] = False
                results["errors"]["customer_name"] = message
            results["messages"]["customer_name"] = message
        
        if phone_number is not None:
            is_valid, message = OrderValidator.validate_phone_number(phone_number)
            if not is_valid:
                results["valid"] = False
                results["errors"]["phone_number"] = message
            results["messages"]["phone_number"] = message
        
        if table_number is not None:
            is_valid, message = OrderValidator.validate_table_number(table_number)
            if not is_valid:
                results["valid"] = False
                results["errors"]["table_number"] = message
            results["messages"]["table_number"] = message
        
        if waiter_name is not None:
            is_valid, message = OrderValidator.validate_waiter_name(waiter_name)
            if not is_valid:
                results["valid"] = False
                results["errors"]["waiter_name"] = message
            results["messages"]["waiter_name"] = message
        
        if items is not None:
            is_valid, message = OrderValidator.validate_items(items)
            if not is_valid:
                results["valid"] = False
                results["errors"]["items"] = message
            results["messages"]["items"] = message
        
        if discount is not None:
            is_valid, message = OrderValidator.validate_discount(discount)
            if not is_valid:
                results["valid"] = False
                results["errors"]["discount"] = message
            results["messages"]["discount"] = message
        
        if payment_method is not None:
            is_valid, message = OrderValidator.validate_payment_method(payment_method)
            if not is_valid:
                results["valid"] = False
                results["errors"]["payment_method"] = message
            results["messages"]["payment_method"] = message
        
        if payment_status is not None:
            is_valid, message = OrderValidator.validate_payment_status(payment_status)
            if not is_valid:
                results["valid"] = False
                results["errors"]["payment_status"] = message
            results["messages"]["payment_status"] = message
        
        if notes is not None:
            is_valid, message = OrderValidator.validate_notes(notes)
            if not is_valid:
                results["valid"] = False
                results["errors"]["notes"] = message
            results["messages"]["notes"] = message
        
        if status is not None:
            is_valid, message = OrderValidator.validate_order_status(status)
            if not is_valid:
                results["valid"] = False
                results["errors"]["status"] = message
            results["messages"]["status"] = message
        
        return results