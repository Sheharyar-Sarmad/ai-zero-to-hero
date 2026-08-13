
import math

def perfectSquare(n) :
    try:
        if isinstance(n , int) :
            if n == 0 or n < 0 :
                return "0 & negative values are allowed!"
            else :
                root = math.isqrt(n)            
                result = root * root == n
    
                if result :
                    return f"{n} is a perfect square of the {root}"
                else :
                    return f"{n} is not a perfect square of the {root}"
                
            return result
            
    except Exception as e:
        return f'An error is coming and saying this: {e}'
    
    
n = int(input('Enter the perfect square: ')) 
print(perfectSquare(n))