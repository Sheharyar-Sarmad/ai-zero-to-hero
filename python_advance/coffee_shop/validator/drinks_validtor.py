import re
from typing import List, Dict, Any, Union

class DrinkValidator:
    """All validation methods for Drink management"""
    
    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        """
        Validate drink title length and character constraints
        
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
    def validate_ingredients(ingredients: List[Dict[str, Any]]) -> tuple[bool, str]:
        """
        Validate ingredients list structure and content
        
        Args:
            ingredients: List of ingredient dictionaries with name and quantity
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not ingredients:
            return False, "Ingredients cannot be empty!"
        
        if not isinstance(ingredients, list):
            return False, "Ingredients must be a list!"
        
        if len(ingredients) == 0:
            return False, "At least one ingredient is required!"
        
        if len(ingredients) > 20:
            return False, "Cannot have more than 20 ingredients!"
        
        for idx, ingredient in enumerate(ingredients):
            # Check if ingredient is a dictionary
            if not isinstance(ingredient, dict):
                return False, f"Ingredient at position {idx + 1} must be a dictionary!"
            
            # Check required fields
            if "name" not in ingredient:
                return False, f"Ingredient at position {idx + 1} missing 'name' field!"
            
            if "quantity" not in ingredient:
                return False, f"Ingredient at position {idx + 1} missing 'quantity' field!"
            
            # Validate ingredient name
            if not ingredient["name"] or len(ingredient["name"].strip()) == 0:
                return False, f"Ingredient at position {idx + 1} has empty name!"
            
            if len(ingredient["name"]) > 50:
                return False, f"Ingredient name at position {idx + 1} exceeds 50 characters!"
            
            # Validate quantity
            if not isinstance(ingredient["quantity"], (int, float)):
                return False, f"Quantity for '{ingredient['name']}' must be a number!"
            
            if ingredient["quantity"] <= 0:
                return False, f"Quantity for '{ingredient['name']}' must be greater than 0!"
            
            if ingredient["quantity"] > 1000000:
                return False, f"Quantity for '{ingredient['name']}' cannot exceed 1,000,000!"
        
        return True, "Ingredients are valid"
    
    @staticmethod
    def validate_drink_id(drink_id: str) -> tuple[bool, str]:
        """
        Validate drink ID format
        
        Args:
            drink_id: ID string to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not drink_id:
            return False, "Drink ID cannot be empty!"
        
        if not isinstance(drink_id, str):
            return False, "Drink ID must be a string!"
        
        # Check if it's a valid ObjectId format (24 hex characters)
        if not re.fullmatch(r'^[0-9a-fA-F]{24}$', drink_id):
            return False, "Invalid drink ID format!"
        
        return True, "Drink ID is valid"
    
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
        valid_fields = ["title", "description", "price", "ingredients", "status"]
        has_valid_field = any(field in update_data for field in valid_fields)
        
        if not has_valid_field:
            return False, f"Update data must contain at least one valid field: {', '.join(valid_fields)}!"
        
        return True, "Update data is valid"
    
    @staticmethod
    def validate_status(status: str) -> tuple[bool, str]:
        """
        Validate drink status
        
        Args:
            status: Status to validate
        
        Returns:
            tuple: (is_valid, error_message)
        """
        valid_statuses = ["available", "unavailable"]
        
        if not status:
            return False, "Status cannot be empty!"
        
        if status.lower() not in valid_statuses:
            return False, f"Status must be one of: {', '.join(valid_statuses)}!"
        
        return True, "Status is valid"
    
    @staticmethod
    def validate_all_fields(
        title: str = None,
        description: str = None,
        price: Union[int, float] = None,
        ingredients: List[Dict[str, Any]] = None,
        status: str = None
    ) -> dict:
        """
        Validate all drink fields at once
        
        Args:
            title: Title to validate
            description: Description to validate
            price: Price to validate
            ingredients: Ingredients to validate
            status: Status to validate
        
        Returns:
            dict: Dictionary with validation results for each field
        """
        results = {
            "valid": True,
            "errors": {},
            "messages": {}
        }
        
        if title is not None:
            is_valid, message = DrinkValidator.validate_title(title)
            if not is_valid:
                results["valid"] = False
                results["errors"]["title"] = message
            results["messages"]["title"] = message
        
        if description is not None:
            is_valid, message = DrinkValidator.validate_description(description)
            if not is_valid:
                results["valid"] = False
                results["errors"]["description"] = message
            results["messages"]["description"] = message
        
        if price is not None:
            is_valid, message = DrinkValidator.validate_price(price)
            if not is_valid:
                results["valid"] = False
                results["errors"]["price"] = message
            results["messages"]["price"] = message
        
        if ingredients is not None:
            is_valid, message = DrinkValidator.validate_ingredients(ingredients)
            if not is_valid:
                results["valid"] = False
                results["errors"]["ingredients"] = message
            results["messages"]["ingredients"] = message
        
        if status is not None:
            is_valid, message = DrinkValidator.validate_status(status)
            if not is_valid:
                results["valid"] = False
                results["errors"]["status"] = message
            results["messages"]["status"] = message
        
        return results