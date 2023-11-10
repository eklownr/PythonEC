""" 
DAGENS UPPGIFT:

1. Applicera Map för att konvertera scores till olika betyg! 
F: 0-49
E: 50-59 
D: 60-69
C: 70-79
B: 80-89
A: 90-100

2. Använd filter för att sedan lägga alla Med godkänt betyg 
    (E eller högre) i en lista, och F i en annan

3. Använd reduce för att beräkna medelvärdet av betygen på scoreslistan

"""
from functools import reduce

scores = [45, 41, 85, 92, 78, 90, 44, 89, 95, 88, 63, 75, 80, 82]
# score_and_count = {"A":[],"B":[],"C":[],"D":[],"E":[],"F":[]}
# def grade_dict(scores):
#     for score in scores:
#         if score < 50:
#             score_and_count["F"] = score
#         elif score < 60:
#             score_and_count["E"] = score
#         elif score < 70:
#             score_and_count["D"] = score
#         elif score < 80:
#             score_and_count["C"] = score
#         elif score < 90:
#             score_and_count["B"] = score
#         elif score > 90:
#             score_and_count["A"] = score            
#     return score_and_count
# 
# print(grade_dict(scores))
# print(score_and_count["F"]) 


grades = list(map(lambda x: 'F' if x < 50 else 'E' if x < 60 else 'D' if x < 70 else 'C' if x < 80 else 'B' if x < 90 else 'A', scores))
print(f"\nPrint out all grades: {grades}")

passing_grades = list(filter(lambda x: x != 'F', grades))
failing_grades = list(filter(lambda x: x == 'F', grades))
print(f"Passing Grade: {passing_grades}")
print(f"Failing Grade: {failing_grades}")


average_grade = reduce(lambda x, y: x + y, scores) / len(scores)
print(f"Avetage Gade: {average_grade}")

# count how many got grade A, B, C, ect...
grade_count = {
    'A': grades.count('A'),
    'B': grades.count('B'),
    'C': grades.count('C'),
    'D': grades.count('D'),
    'E': grades.count('E'),
    'F': grades.count('F')
} 
print(f"\ncount how many got grade A, B, C, ect ... :")
print(grade_count)


# Använder map-funktionen för att konvertera poäng till
# betygsbokstäver och lägger till dem i den slutliga dictionaryn:
score_list = [45, 41, 85, 92, 78, 90, 44, 89, 95, 88, 63, 75, 80, 82]

score_and_count = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[]}

def grades_dict(scores):
    score_and_grade = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        50: "E",
        0: "F"
    }
    
    for score in scores:
        for grade in score_and_grade.keys():
            if score >= grade:
                score_and_count[score_and_grade[grade]].append(score)
                break
                
    return score_and_count

print(f"\nAll Score for A, B, C, etc:")
print(grades_dict(score_list))
# Output: {'A': [92, 90, 95], 'B': [85, 89, 88], 'C': [78, 82, 80], 'D



def get_grades(score: int):
    score_and_grade = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        50: "E",
        0: "F"
    }
    
    for grade in score_and_grade.keys():
        if score >= grade:
            return score_and_grade[grade]

ag = int(average_grade) 
print(f"Average point is: {ag}. That givs the grade: {get_grades(ag)}")          