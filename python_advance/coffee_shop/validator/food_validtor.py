import re
from typing import List, Dict, Any, Union, Optional

class FoodValidator:
    """All validation methods for Food management"""
    
    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        """
        Validate food title length and character constraints
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
        """
        if not description or len(description.strip()) == 0:
            return False, "Description cannot be empty!"
        
        if len(description) < 20:
            return False, "Description must be at least 20 characters long!"
        
        if len(description) > 500:
            return False, "Description cannot exceed 500 characters!"
        
        return True, "Description is valid"
    
    @staticmethod
    def validate_price(price: Union[int, float]) -> tuple[bool, str]:
        """
        Validate price constraints
        """
        if not isinstance(price, (int, float)):
            return False, "Price must be a number!"
        
        if price <= 0:
            return False, "Price must be greater than 0!"
        
        if price > 999999.99:
            return False, "Price cannot exceed 999,999.99!"
        
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
        """
        if not ingredients:
            return False, "Ingredients cannot be empty!"
        
        if not isinstance(ingredients, list):
            return False, "Ingredients must be a list!"
        
        if len(ingredients) == 0:
            return False, "At least one ingredient is required!"
        
        if len(ingredients) > 30:
            return False, "Cannot have more than 30 ingredients!"
        
        for idx, ingredient in enumerate(ingredients):
            if not isinstance(ingredient, dict):
                return False, f"Ingredient at position {idx + 1} must be a dictionary!"
            
            if "name" not in ingredient:
                return False, f"Ingredient at position {idx + 1} missing 'name' field!"
            
            if "quantity" not in ingredient:
                return False, f"Ingredient at position {idx + 1} missing 'quantity' field!"
            
            if not ingredient["name"] or len(ingredient["name"].strip()) == 0:
                return False, f"Ingredient at position {idx + 1} has empty name!"
            
            if len(ingredient["name"]) > 50:
                return False, f"Ingredient name at position {idx + 1} exceeds 50 characters!"
            
            if not isinstance(ingredient["quantity"], (int, float)):
                return False, f"Quantity for '{ingredient['name']}' must be a number!"
            
            if ingredient["quantity"] <= 0:
                return False, f"Quantity for '{ingredient['name']}' must be greater than 0!"
            
            if ingredient["quantity"] > 1000000:
                return False, f"Quantity for '{ingredient['name']}' cannot exceed 1,000,000!"
        
        return True, "Ingredients are valid"
    
    @staticmethod
    def validate_food_id(food_id: str) -> tuple[bool, str]:
        """
        Validate food ID format
        """
        if not food_id:
            return False, "Food ID cannot be empty!"
        
        if not isinstance(food_id, str):
            return False, "Food ID must be a string!"
        
        if not re.fullmatch(r'^[0-9a-fA-F]{24}$', food_id):
            return False, "Invalid food ID format!"
        
        return True, "Food ID is valid"
    
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
    def validate_update_data(update_data: dict) -> tuple[bool, str]:
        """
        Validate update data dictionary
        """
        if not update_data:
            return False, "Update data cannot be empty!"
        
        if not isinstance(update_data, dict):
            return False, "Update data must be a dictionary!"
        
        valid_fields = ["title", "description", "price", "ingredients", "status", 
                       "veg", "preparation_time", "calories", "image_url", "featured", "is_spicy"]
        has_valid_field = any(field in update_data for field in valid_fields)
        
        if not has_valid_field:
            return False, f"Update data must contain at least one valid field: {', '.join(valid_fields)}!"
        
        return True, "Update data is valid"
    
    @staticmethod
    def validate_status(status: str) -> tuple[bool, str]:
        """
        Validate food status
        """
        valid_statuses = ["available", "unavailable"]
        
        if not status:
            return False, "Status cannot be empty!"
        
        if status.lower() not in valid_statuses:
            return False, f"Status must be one of: {', '.join(valid_statuses)}!"
        
        return True, "Status is valid"
    
    @staticmethod
    def validate_price_range(min_price: float, max_price: float) -> tuple[bool, str]:
        """
        Validate price range for filtering
        """
        if min_price is None and max_price is None:
            return False, "At least one price bound must be provided!"
        
        if min_price is not None:
            if not isinstance(min_price, (int, float)):
                return False, "Minimum price must be a number!"
            if min_price < 0:
                return False, "Minimum price cannot be negative!"
        
        if max_price is not None:
            if not isinstance(max_price, (int, float)):
                return False, "Maximum price must be a number!"
            if max_price < 0:
                return False, "Maximum price cannot be negative!"
        
        if min_price is not None and max_price is not None:
            if min_price > max_price:
                return False, "Minimum price cannot be greater than maximum price!"
        
        return True, "Price range is valid"
    
    @staticmethod
    def validate_preparation_time(time: int) -> tuple[bool, str]:
        """
        Validate preparation time
        """
        if not isinstance(time, int):
            return False, "Preparation time must be an integer!"
        
        if time < 1:
            return False, "Preparation time must be at least 1 minute!"
        
        if time > 120:
            return False, "Preparation time cannot exceed 120 minutes!"
        
        return True, "Preparation time is valid"
    
    @staticmethod
    def validate_calories(calories: int) -> tuple[bool, str]:
        """
        Validate calories
        """
        if not isinstance(calories, int):
            return False, "Calories must be an integer!"
        
        if calories < 0:
            return False, "Calories cannot be negative!"
        
        if calories > 5000:
            return False, "Calories cannot exceed 5000!"
        
        return True, "Calories are valid"
    
    @staticmethod
    def validate_image_url(image_url: str) -> tuple[bool, str]:
        """
        Validate image URL
        """
        if image_url:
            if not isinstance(image_url, str):
                return False, "Image URL must be a string!"
            
            if len(image_url) > 500:
                return False, "Image URL cannot exceed 500 characters!"
            
            # Simple URL validation
            if not re.match(r'^https?://', image_url):
                return False, "Image URL must start with http:// or https://!"
        
        return True, "Image URL is valid"
    
    @staticmethod
    def validate_all_fields(
        title: str = None,
        description: str = None,
        price: Union[int, float] = None,
        ingredients: List[Dict[str, Any]] = None,
        status: str = None,
        veg: bool = None,
        preparation_time: int = None,
        calories: int = None,
        image_url: str = None,
        featured: bool = None,
        is_spicy: bool = None
    ) -> dict:
        """
        Validate all food fields at once
        """
        results = {
            "valid": True,
            "errors": {},
            "messages": {}
        }
        
        if title is not None:
            is_valid, message = FoodValidator.validate_title(title)
            if not is_valid:
                results["valid"] = False
                results["errors"]["title"] = message
            results["messages"]["title"] = message
        
        if description is not None:
            is_valid, message = FoodValidator.validate_description(description)
            if not is_valid:
                results["valid"] = False
                results["errors"]["description"] = message
            results["messages"]["description"] = message
        
        if price is not None:
            is_valid, message = FoodValidator.validate_price(price)
            if not is_valid:
                results["valid"] = False
                results["errors"]["price"] = message
            results["messages"]["price"] = message
        
        if ingredients is not None:
            is_valid, message = FoodValidator.validate_ingredients(ingredients)
            if not is_valid:
                results["valid"] = False
                results["errors"]["ingredients"] = message
            results["messages"]["ingredients"] = message
        
        if status is not None:
            is_valid, message = FoodValidator.validate_status(status)
            if not is_valid:
                results["valid"] = False
                results["errors"]["status"] = message
            results["messages"]["status"] = message
        
        if veg is not None:
            if not isinstance(veg, bool):
                results["valid"] = False
                results["errors"]["veg"] = "Veg must be a boolean value!"
            results["messages"]["veg"] = "Veg is valid"
        
        if preparation_time is not None:
            is_valid, message = FoodValidator.validate_preparation_time(preparation_time)
            if not is_valid:
                results["valid"] = False
                results["errors"]["preparation_time"] = message
            results["messages"]["preparation_time"] = message
        
        if calories is not None:
            is_valid, message = FoodValidator.validate_calories(calories)
            if not is_valid:
                results["valid"] = False
                results["errors"]["calories"] = message
            results["messages"]["calories"] = message
        
        if image_url is not None:
            is_valid, message = FoodValidator.validate_image_url(image_url)
            if not is_valid:
                results["valid"] = False
                results["errors"]["image_url"] = message
            results["messages"]["image_url"] = message
        
        if featured is not None:
            if not isinstance(featured, bool):
                results["valid"] = False
                results["errors"]["featured"] = "Featured must be a boolean value!"
            results["messages"]["featured"] = "Featured is valid"
        
        if is_spicy is not None:
            if not isinstance(is_spicy, bool):
                results["valid"] = False
                results["errors"]["is_spicy"] = "Is spicy must be a boolean value!"
            results["messages"]["is_spicy"] = "Is spicy is valid"
        
        return results