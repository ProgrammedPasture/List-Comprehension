# numbers = [1,2,3,4,5,6,7,8,9]
#
# new_numbers = [n + 1 for n in numbers]
#
# print(new_numbers)

# name = "Brandon"
#
# new_name =[letter for letter in name]
# print(new_name)

numbers = range(1,5)

new_numbers = [n * 2 for n in numbers]
print(new_numbers)

names = ["Brandon", "Amber", "Alex", "Meagan", "Anthony", "Luke"]

# new_names = [names for names in names if len(names) < 5 ]
new_names = [n.upper() for n in names if len(names) > 5]
print(new_names)