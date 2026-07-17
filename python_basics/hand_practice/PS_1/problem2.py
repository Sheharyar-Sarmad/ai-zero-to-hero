

def problem2(fruits : list , rates : list) -> dict:
    try:
       fruitDict = {}
       for fruit,rate in zip(fruits , rates) :
           fruitDict[fruit] = rate
           
       return fruitDict           
   
    except Exception as e:
        return f"Error is saying this {e}"
    
fruits = ["Mangoes","Apple","Banana","Grapes"]  
rates = [350,250,150,500]  
print(problem2(fruits,rates));