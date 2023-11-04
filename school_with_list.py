#!/usr/bin/env python3
"""resumen of students for activity

print list of students grouping for classroom
that asisting in each ativity
"""
__version__ = "0.1.0"
__author__ = "alefuentes"
__licence__ = "unlicense"

classroom_a = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
classroom_b = ['mmm', 'nnn', 'ooo','ppp','qqq', 'rrr']

# mixing student between activity
class_english = ['aaa','ooo','ppp', 'ccc', 'mmm', 'nnn', 'ooo','ppp', 'ddd', 'eee', 'fff', 'qqq', 'rrr']
class_biology = ['mmm', 'nnn', 'ooo','ppp','qqq','aaa', 'bbb', 'ccc',]
class_technology = ['fff', 'bbb', 'ccc','qqq', 'rrr']

activities = [
    ("English", class_english), 
    ("Biology", class_biology), 
    ("Technology", class_technology)
]

# list student of each activity
for label, activity in activities: 

    activity_classroom_a = []
    activity_classroom_b = []

    for student in activity:
        if student in classroom_a:
            activity_classroom_a.append(student)
        elif student in classroom_b:
            activity_classroom_b.append(student)

    print(label)
    print(f"classroom 1: \n{activity_classroom_a}")
    print(f"classroom 2: \n{activity_classroom_b}")
    print("-" * 30)
