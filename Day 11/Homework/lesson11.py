#დავალება N1
n = int(input())
for i in range(0,n+2,1):
    print(i)

#დავალება N2
age = int(input("Please enter your age: "))
students_card = input("Do you have students card? yes or no : ")
if age < 18 or students_card == "yes":
    print("You have discount")
elif age > 60 and students_card == "no":
    print("You have pensioners discount")
else:
    print("You dont have discount")

# დავალება N3
num_1 = int(input())
num_2 = int(input())
if num_1 > 0 and num_2 > 0:
    print("Both numbers are positive")
elif num_1 > 0 and num_2 < 0 or num_1 < 0 and num_2 > 0:
    print("Only one is positive")
else:
    print("None is positive")

# დავალება N4
n_1 = int(input())
n_2 = int(input())
operation = input("Please enter operation")
if operation == "+":
    print(n_1 + n_2)
elif operation == "-":
    print(n_1 - n_2)
elif operation == "*":
    print(n_1 * n_2)
elif operation == "/" and n_2 != 0:
    print(n_1 / n_2)
elif n_2 == 0 and operation == "/":
    print("You cant devide on zero!!!")
else:
    print("Wrong operation")

# დავალება N5
A = True
B = False
C = False 
#ა) (A&&!B)||(B&&!A)
#აქ იქნება (True and True) or (False and False)რადგან ! ცვლის მნიშვნელობას. საბოლოოდ კი იქნება True or False და შემდეგ True.
# პასუხია-True
a = "Answer in ა is: "
result_0 = "True"
#ბ) (B&&C)&&(A||B)
#აქ იქნება (False and False) and (True or False), შემდეგ False and True და შემდეგ False.
#პასუხია-False
b = "Answer in ბ is: "
result_1 = "False"
#გ) (A&&!C)||(B&&!A)||(B&&!C)
# აქ იქნება (True and True) or (False and False) or (False and True), შემდეგ კი True or False or False, საბოლოოდ კი True.
c = "Answer in გ is: "
result_2 = "True"
#პასუხი-True
print(a + result_0)
print(b + result_1)
print(c + result_2)
