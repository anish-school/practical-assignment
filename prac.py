# 1. avg marks and grades of students
# subjects = ["english", "science", "math", "hindi", "social science", "IT"]
# grades = {
#     100: "A",
#     90: "A",
#     80: "B",
#     70: "B",
#     60: "C",
#     50: "C",
#     40: "D",
#     30: "E",
#     20: "F",
#     10: "F",
#     0: "F",
# }
# total = 0
# for sub in subjects:
#     marks = int(input(f"Enter your marks for {sub}: "))
#     total += marks

# avg = total / len(subjects)
# print(f"Avg marks are {int(avg)}, grade is {grades[int(avg) - int(avg) % 10]}")


# 2. selling price after discount
cost = float(input("enter the cost "))
discount = float(input("enter the discount percentage "))
sale = cost - discount * cost / 100
print(sale)


# 3. perimeter and area of shapes
# import math
# shape = input("Enter your shape: ")
# if shape == "triangle":
#     side1 = float(input("Enter the length of side 1: "))
#     side2 = float(input("Enter the length of side 2: "))
#     side3 = float(input("Enter the length of side 3: "))
#     print(f"Perimeter: {side1 + side2 + side3}")
#     s = (side1 + side2 + side3) / 2
#     print(f"Area: {math.sqrt(s * (s - side1) * (s - side2) * (s - side3))}")
# elif shape == "rectangle":
#     length = float(input("Enter the length: "))
#     breadth = float(input("Enter the breadth: "))
#     print(f"Perimiter: {2 * (length + breadth)}")
#     print(f"Area: {length * breadth}")
# elif shape == "square":
#     side = float(input("Enter the length of the side: "))
#     print(f"Perimeter: {4 * side}")
#     print(f"Area: {side * side}")
# elif shape == "circle":
#     radius = float(input("Enter the length of the radius: "))
#     print(f"Circumference: {math.pi * 2 * radius}")
#     print(f"Area: {math.pi * radius * radius}")


# 4. compound and simple interest
# amt = float(input("Enter the amount: "))
# roi = float(input("Enter the rate of interest: "))
# dur = float(input("Enter the time duration: "))
# interest_type = input("SI or CI? ")
# if interest_type == "SI":
#     print(f"Your interest is: {amt * roi * dur / 100}")
# elif interest_type == "CI":
#     n = float(input("Enter the number of times interest got compounded annually: "))
#     print(f"Your interest is: {amt * (1 + roi / (100 * n) ** (n * dur))}")


# 5. calculating profit and loss
# cost = float(input("Enter the cost price: "))
# sell = float(input("Enter the selling price: "))
# if cost < sell:
#     print(f"Profit = {sell - cost}")
# elif cost > sell:
#     print(f"Loss = {cost - sell}")
# else:
#     print("Neither profit nor loss")


# 6. calculating EMI
# amt = float(input("Enter the amount: "))
# roi = float(input("Enter the monthly rate of interest: "))
# months = int(input("Enter the number of months: "))
# emi = amt * roi * ((1 + roi) ** months / ((1 + roi) ** months - 1))
# print(emi)


# 7. largest and smallest numbers in a list
# nums = [56, 34, 76, 45, 12, 87, 98]
# nums.sort()
# print(f"smallest: {nums[0]}, largest: {nums[-1]}")


# 8. third largest and smallest numbers in a list
# nums = [34, 56, 76, 234, 13, 78,445, 23]
# nums.sort()
# print(f"third largest: {nums[2]}, third smallest: {nums[-3]}")


# 9. sum of first 100 natural numbers
# sum  = 0
# for i in range(1, 101):
#     sum += i * i

# print(sum)


# 10. multiples of a number
# num = int(input("Enter the number: "))
# n = int(input("Enter the number of multiples you want: "))
# for i in range(1, n + 1):
#     print(f"{num} * {n} = {num * n}")


# 11. vowels in string
# vowels = ['a', 'e', 'i', 'o', 'u']
# string = input("Enter a string: ")
# count = 0
# for i in range(len(string)):
#     if string[i] in vowels:
#         count += 1
# print(count)


# 12. states and capitals
# capitals = {}
# state = input("Enter the state: ")
# capital = input("Enter the capital: ")
# capitals[state] = capital
# print(capitals)


# 13. names and marks of students
# marks = {}
# name = input("Enter your name: ")
# marks[name] = {}
# for i in range(1, 6):
#     m = int(input(f"Enter your marks in subject{i}: "))
#     marks[name][f"subject{i}"] = m

# print(marks)


# 14. highest and lowest values in a dictionary
# nums = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "hundred": 100,
#     "seven": 7,
#     "four": 4,
# }
# maximum = nums[list(nums.keys())[0]]
# for key in nums:
#     if nums[key] > maximum:
#         maximum = nums[key]
# print(maximum)


# 15. print the number of occurrences of a given alphabet in each string
# char = input("Enter a character: ")
# string = input("Enter a string: ")
# print(string.count(char))
