import re
from typing import Literal, Union

class InventoryValidator:
    """All validation methods for Inventory management"""
    
    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        """
        Validate title length and character constraints
        
        Args:
            title: Title string to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not title or len(title.strip()) == 0:
            return False, "Title cannot be empty!"
        
        if len(title) < 2:
            return False, "Title must be at least 2 characters long!"
        
        if len(title) > 50:
            return False, "Title cannot exceed 50 characters!"
        
        if not re.fullmatch(r"[A-Za-z0-9 ]+", title):
            return False, "Title can only contain letters, numbers, and spaces!"
        
        return True, "Title is valid"
    
    @staticmethod
    def validate_description(description: str) -> tuple[bool, str]:
        """
        Validate description length constraints
        
        Args:
            description: Description string to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not description or len(description.strip()) == 0:
            return False, "Description cannot be empty!"
        
        if len(description) < 20:
            return False, "Description must be at least 20 characters long!"
        
        if len(description) > 250:
            return False, "Description cannot exceed 250 characters!"
        
        return True, "Description is valid"
    
    @staticmethod
    def validate_stock(stock: Union[int, float]) -> tuple[bool, str]:
        """
        Validate stock quantity
        
        Args:
            stock: Stock quantity to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(stock, (int, float)):
            return False, "Stock must be a number!"
        
        if stock < 0:
            return False, "Stock cannot be negative!"
        
        if not isinstance(stock, int):
            return False, "Stock must be a whole number!"
        
        return True, "Stock is valid"
    
    @staticmethod
    def validate_price(price: Union[int, float]) -> tuple[bool, str]:
        """
        Validate price constraints
        
        Args:
            price: Price to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(price, (int, float)):
            return False, "Price must be a number!"
        
        if price <= 0:
            return False, "Price must be greater than 0!"
        
        if price > 999999.99:
            return False, "Price cannot exceed 999,999.99!"
        
        # Validate price has maximum 2 decimal places
        if isinstance(price, float):
            price_str = str(price)
            if '.' in price_str:
                decimals = len(price_str.split('.')[1])
                if decimals > 2:
                    return False, "Price can only have up to 2 decimal places!"
        
        return True, "Price is valid"
    
    @staticmethod
    def validate_category(category: str) -> tuple[bool, str]:
        """
        Validate category type
        
        Args:
            category: Category to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        valid_categories = ["liquid", "solid"]
        
        if not category:
            return False, "Category cannot be empty!"
        
        if category.lower() not in valid_categories:
            return False, f"Category must be one of: {', '.join(valid_categories)}!"
        
        return True, "Category is valid"
    
    @staticmethod
    def validate_weight(weight: Union[int, float]) -> tuple[bool, str]:
        """
        Validate weight constraints
        
        Args:
            weight: Weight to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(weight, (int, float)):
            return False, "Weight must be a number!"
        
        if weight <= 0:
            return False, "Weight must be greater than 0!"
        
        if weight > 10000:
            return False, "Weight cannot exceed 10,000 units!"
        
        # Validate weight has maximum 2 decimal places
        if isinstance(weight, float):
            weight_str = str(weight)
            if '.' in weight_str:
                decimals = len(weight_str.split('.')[1])
                if decimals > 2:
                    return False, "Weight can only have up to 2 decimal places!"
        
        return True, "Weight is valid"
    
    @staticmethod
    def validate_inventory_id(inventory_id: str) -> tuple[bool, str]:
        """
        Validate inventory ID format
        
        Args:
            inventory_id: ID string to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not inventory_id:
            return False, "Inventory ID cannot be empty!"
        
        if not isinstance(inventory_id, str):
            return False, "Inventory ID must be a string!"
        
        # Check if it's a valid ObjectId format (24 hex characters)
        if not re.fullmatch(r'^[0-9a-fA-F]{24}$', inventory_id):
            return False, "Invalid inventory ID format!"
        
        return True, "Inventory ID is valid"
    
    @staticmethod
    def validate_search_term(search_term: str) -> tuple[bool, str]:
        """
        Validate search term
        
        Args:
            search_term: Search term to validate
        
        Returns:
            tuple: (is_valid, error_message)
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
        
        Args:
            page: Page number to validate
        
        Returns:
            tuple: (is_valid, error_message)
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
        
        Args:
            limit: Limit to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(limit, int):
            return False, "Limit must be an integer!"
        
        if limit < 1:
            return False, "Limit must be at least 1!"
        
        if limit > 100:
            return False, "Limit cannot exceed 100!"
        
        return True, "Limit is valid"
    
    @staticmethod
    def validate_sort_order(sort_order: str) -> tuple[bool, str]:
        """
        Validate sort order
        
        Args:
            sort_order: Sort order to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        valid_orders = ["asc", "desc"]
        
        if not sort_order:
            return False, "Sort order cannot be empty!"
        
        if sort_order.lower() not in valid_orders:
            return False, f"Sort order must be one of: {', '.join(valid_orders)}!"
        
        return True, "Sort order is valid"
    
    @staticmethod
    def validate_amount(amount: Union[int, float]) -> tuple[bool, str]:
        """
        Validate amount for stock operations
        
        Args:
            amount: Amount to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not isinstance(amount, (int, float)):
            return False, "Amount must be a number!"
        
        if amount <= 0:
            return False, "Amount must be greater than 0!"
        
        if not isinstance(amount, int):
            return False, "Amount must be a whole number!"
        
        if amount > 1000000:
            return False, "Amount cannot exceed 1,000,000!"
        
        return True, "Amount is valid"
    
    @staticmethod
    def validate_update_data(update_data: dict) -> tuple[bool, str]:
        """
        Validate update data dictionary
        
        Args:
            update_data: Dictionary containing fields to update
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not update_data:
            return False, "Update data cannot be empty!"
        
        if not isinstance(update_data, dict):
            return False, "Update data must be a dictionary!"
        
        # Check if at least one valid field is being updated
        valid_fields = ["title", "description", "stock", "price", "category", "weight"]
        has_valid_field = any(field in update_data for field in valid_fields)
        
        if not has_valid_field:
            return False, f"Update data must contain at least one valid field: {', '.join(valid_fields)}!"
        
        return True, "Update data is valid"
    
    @staticmethod
    def validate_all_fields(
        title: str = None,
        description: str = None,
        stock: Union[int, float] = None,
        price: Union[int, float] = None,
        category: str = None,
        weight: Union[int, float] = None
    ) -> dict:
        """
        Validate all inventory fields at once
        
        Args:
            title: Title to validate
            description: Description to validate
            stock: Stock to validate
            price: Price to validate
            category: Category to validate
            weight: Weight to validate
        
        Returns:
            dict: Dictionary with validation results for each field
        """
        results = {
            "valid": True,
            "errors": {},
            "messages": {}
        }
        
        if title is not None:
            is_valid, message = InventoryValidator.validate_title(title)
            if not is_valid:
                results["valid"] = False
                results["errors"]["title"] = message
            results["messages"]["title"] = message
        
        if description is not None:
            is_valid, message = InventoryValidator.validate_description(description)
            if not is_valid:
                results["valid"] = False
                results["errors"]["description"] = message
            results["messages"]["description"] = message
        
        if stock is not None:
            is_valid, message = InventoryValidator.validate_stock(stock)
            if not is_valid:
                results["valid"] = False
                results["errors"]["stock"] = message
            results["messages"]["stock"] = message
        
        if price is not None:
            is_valid, message = InventoryValidator.validate_price(price)
            if not is_valid:
                results["valid"] = False
                results["errors"]["price"] = message
            results["messages"]["price"] = message
        
        if category is not None:
            is_valid, message = InventoryValidator.validate_category(category)
            if not is_valid:
                results["valid"] = False
                results["errors"]["category"] = message
            results["messages"]["category"] = message
        
        if weight is not None:
            is_valid, message = InventoryValidator.validate_weight(weight)
            if not is_valid:
                results["valid"] = False
                results["errors"]["weight"] = message
            results["messages"]["weight"] = message
        
        return results