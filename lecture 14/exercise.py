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
grades = list(map(lambda x: 
                  'F' if x < 50 
                  else 'E' if x < 60 
                  else 'D' if x < 70 
                  else 'C' if x < 80 
                  else 'B' if x < 90 
                  else 'A', 
                  scores)
                  )

print(f"\nAll score: {scores}")
print(f"All grades: {grades}")

passing_grades = list(filter(lambda x: x != 'F', grades))
failing_grades = list(filter(lambda x: x == 'F', grades))
print(f"Passing Grade: {passing_grades}")
print(f"Failing Grade: {failing_grades}")

# First time lambda x=45,y=41. Second time x=45+41, y=85 ...
average_grade = reduce(lambda x, y: x + y, scores) / len(scores)
print(f"Avetage score: {average_grade}")

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


# Two dict to keep track of score and grade
score_and_grade = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    50: "E",
    0: "F"
}
    
def grades_dict(scores):
    score_and_count = {
        "A":[], 
        "B":[], 
        "C":[], 
        "D":[], 
        "E":[], 
        "F":[]
    }

    for score in scores:
        for grade in score_and_grade.keys():
            if score >= grade:
                score_and_count[score_and_grade[grade]].append(score)
                break
                
    return score_and_count

print(f"\nAll Score for A, B, C, etc:")
print(grades_dict(scores))
# Output: {'A': [92, 90, 95], 'B': [85, 89, 88], 'C': [78, 82, 80], 'D


def get_grades(score: int):
    for grade in score_and_grade.keys():
        if score >= grade:
            return score_and_grade[grade]

ag = int(average_grade) 
print(f"Average point is: {ag}. That givs the grade: {get_grades(ag)}\n")          


def who_made_it():
    made_it_not = []
    made_it = []
    all_grades = grades_dict(scores)
    for grade in all_grades:
        if grade == "F":
            made_it_not.append(all_grades[grade]) 
        else:
            made_it.append(all_grades[grade]) 
            
    print(f"This score made it: {made_it}! \nThose did't: {made_it_not}!\n")
    return made_it, made_it_not
high_score, f_score = who_made_it()


for score in f_score[0]:
    print(f"Luhooser ---> {score} Score F !")

for score in high_score[0]:
    print(f"You did it ---> {score} Score A !")

for  score_list in high_score:
    for score in score_list:
        print(f"Score that made it: {score}")