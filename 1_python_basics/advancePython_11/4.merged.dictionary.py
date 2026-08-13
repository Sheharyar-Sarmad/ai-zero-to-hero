from json import dumps

student = {
    "name": "Ali",
    "class": 10,
    "roll_no": 25,
    "marks": 88
}

product = {
    "id": 101,
    "name": "Laptop",
    "price": 75000,
    "in_stock": True
}

merged = student | product
print(dumps(merged , indent=2))