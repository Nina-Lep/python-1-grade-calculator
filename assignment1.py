labs = float(input("Enter the number of labs completed: "))
quizzes = float(input("Enter the number of quizzes completed: "))
as1 = float(input("Enter grade for Assignment 1: "))
as2 = float(input("Enter grade for Assignment 2: "))
as3 = float(input("Enter grade for Assignment 3: "))
as4 = float(input("Enter grade for Assignment 4: "))
mid1 = float(input("Enter grade for Midterm 1: "))
mid2 = float(input("Enter grade for Midterm 2: "))
fin = float(input("Enter grade for Final Exam: "))
midfin = float(input("Enter grade for Midterms and Final Preparation: "))

grade = ((labs*((100/6)*20)/100) + 
             (quizzes*((100/6)*15)/100) + 
              ((as1*4)/100) +
               ((as1*4)/100) +
                ((as3*4)/100) +
                 ((as4*4)/100) +
                  ((mid1*12.5)/100) +
                   ((mid2*12.5)/100) +
                    ((fin*18)/100) +
                     ((midfin*6)/100))
print("Your garde is: " + str(grade))
