grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
grades = list(filter(lambda x: x >= 70, grades))
print(grades)

my_list = [12, 8, 4, 1, 2, 6, 4, 4, 5]
my_new_list = [i * 7 for i in my_list]
print(my_new_list)

transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]
transaction = [round(x) for x in transactions]
print(transaction)