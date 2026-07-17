

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# 1
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

expenses = [
    2200, 2350, 2000, 2130,
    2000, 2000, 2500, 2400,
    2100, 2250, 2300, 2150
]

jan_expenses,feb_expenses,march_quarter = expenses[0],expenses[1],expenses[2]
print(f"In {months[1]}, {feb_expenses - jan_expenses} are spend more than {months[0]} expenses")

# 2
first_quarter_total = sum(expenses[:3])
print(first_quarter_total)

# 3
for index,value in enumerate(expenses):
    if value == 2000:
        print(months[index], value)
        
# 4
# for i,v in enumerate(months): 
#     if v == "June": O(n)
#         expenses[i] = 1980
#         print(v,expenses[i])

expenses[5] = 1980
print(expenses)

# 5
expenses[3] = expenses[3] - 200 # O(1)
print(expenses)