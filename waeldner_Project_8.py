'''
Creating a Transcript Reader
File Name: Waeldner_project_8
Author: Matt Waeldner
Date: 11/15/22
Course: COMP-1351
Assingment: Project 8 - Transcript Reader
Collaborators: N/A
Internet Source: N/A
'''

#THE FILE MUST BE dan.glysack.txt FOR THIS TO WORK
nameinfile = True
student_name = ['dan glysack']
first_name = str(input("What is the students first name?: "))
last_name = str(input("What is the students last name?: "))
major = str(input("Major?(all caps): "))


while first_name != 'dan':
    first_name = str(input("Enter a valid students first name: "))

while last_name != "glysack":
    last_name = str(input("Enter a valid students last name: "))
 
class_abvs = []
course_numbers = []
course_names = []
all_credit_hours = []
grades = []
numbergrade4gpa = []


with open(f'{first_name}_{last_name}.txt') as file:
    for line in range(12):
        one_line = file.readline().strip().split(',')
        class_abvs.append(one_line[0])
        course_numbers.append(one_line[1])
        course_names.append(one_line[2])
        all_credit_hours.append(float(one_line[3]))
        grades.append(one_line[4])

totalhours = 0
for i in range(len(course_numbers)):
    totalhours += all_credit_hours[i]


#Making a list of number GPA coresponding to letter grade
for grade in grades:
    if grade == "T" or grade == "P":
        1
    else:
        if grade == "A+":
            numbergrade4gpa.append(4.0) 
        elif grade == "A":
            numbergrade4gpa.append(4.0)
        elif grade == "A-":
            numbergrade4gpa.append(3.3)
        elif grade == "B+":
            numbergrade4gpa.append(3.0)
        elif grade == "B":
            numbergrade4gpa.append(3.7)
        elif grade == "B-":
            numbergrade4gpa.append(2.7)
        elif grade == "C+":
            numbergrade4gpa.append(2.3)
        elif grade == "C":
            numbergrade4gpa.append(2.0)
        elif grade == "C":
            numbergrade4gpa.append(2.0)
        elif grade == "C-":
            numbergrade4gpa.append(1.7)
        elif grade == "D+":
            numbergrade4gpa.append(1.3)
        elif grade == "D":
            numbergrade4gpa.append(1.0)
        elif grade == "F":
            numbergrade4gpa.append(0.0)
        
#determining the GPA
gradesum = 0

for g in numbergrade4gpa:
    gradesum += g
    gpa = gradesum / len(numbergrade4gpa)

#Sifting out just the grades that student got in major classes
majorgrades = []
majornumbergrades = []
for i in range(len(course_numbers)):
    if class_abvs[i] == major:
        majorgrades.append(grades[i])

#Making a numbered gpa corresponding to the letter grade
for each in majorgrades:
        if each == "A+":
            majornumbergrades.append(4.0) 
        elif each == "A":
            majornumbergrades.append(4.0)
        elif each == "A-":
            majornumbergrades.append(3.3)
        elif each == "B+":
            majornumbergrades.append(3.0)
        elif each == "B":
            majornumbergrades.append(3.7)
        elif each == "B-":
            majornumbergrades.append(2.7)
        elif each == "C+":
            majornumbergrades.append(2.3)
        elif each == "C":
            majornumbergrades.append(2.0)
        elif each == "C":
            majornumbergrades.append(2.0)
        elif each == "C-":
            majornumbergrades.append(1.7)
        elif each == "D+":
            majornumbergrades.append(1.3)
        elif each == "D":
            majornumbergrades.append(1.0)
        elif each == "F":
            majornumbergrades.append(0.0)
        else:
            1

#Determining the Major Gpa
print(majornumbergrades)
majorgpa = 0
majorsum = 0
for numbergrade in majornumbergrades:
    majorsum += numbergrade
    majorgpa = majorsum / len(majornumbergrades)

hoursinmajor = []

#making a list with only the credit hours in students major classes
for i in range(len(course_numbers)):
    if class_abvs[i] == major:
        hoursinmajor.append(all_credit_hours[i])
#Finding the sum of all the hours in major classes
majorhours_sum = 0
for each in hoursinmajor:
    majorhours_sum += each
#Printing out all the info
print(f'Name: {first_name} {last_name}')
print(f'{first_name}_{last_name}.txt file succesfuly located')
print(f'GPA: {gpa}')
print(f'University credit hours: {totalhours}')
print(f'Major Credit Hours: {majorhours_sum}')
print(f'Major GPA: {majorgpa}')





        


        


    



    



