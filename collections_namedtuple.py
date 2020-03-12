from collections import namedtuple


#Example 1
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)

dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)

#Example 2
Car = namedtuple('Car', 'Price Mileage Color Class')
xyz = Car(Price = 100000, Mileage = 30, Color = 'Cyan', Class = 'Y')


#Experimentation

Student = namedtuple('Student', 'ID, MARKS, NAME, CLASS')

student_1 = Student(1, 97,'David', 1)
student_2 = Student(2, 80,'Jess', 7)
student_3 = Student(3, 77,'Calvin', 9)
student_4 = Student(4, 64,'Kara', 4)

Avg = float((student_1.MARKS + student_2.MARKS + student_3.MARKS + student_4.MARKS)/4)

#Solution from e_erkela that doesn't violate PEP8

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))