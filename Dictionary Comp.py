#new_dict = {new_key: new_value for (key,value), in dict.items()}
#new_dict = {new_key: new_value for (key,value), in dict.items() if test}

import random

names = ["Brandon", "Amber", "Alex", "Meagan", "Anthony", "Luke"]

student_scores = {student: random.randint(1,100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)