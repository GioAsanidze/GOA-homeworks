#დავალება N1 
num = 1
while num <= 10:
    print( num )
    num = num + 1

#დავალება N2
number = 10
while number >= 0:
    print( number )
    number = number - 1

#დავალება N3
#while ფუნქცია არის ისეთი ფუნქცია, სადაც შეგვიძლია კოდი გავუშვათ იმდენჯერ რამდენჯერაც გვინდა, სანამ რაიმე პირობა არ შესრულდება.

#დავალება N4
correct_code = "python123"
guess_code = input("Guess the code: ")
while guess_code != correct_code:
    guess_code = input("Incorrect! Try again! ")
if guess_code == correct_code:
    print("Correct! ")

#დავალება N5
n = int(input("Enter number: "))
Num = 1
total = 0 

while Num <= n:
    total += Num
    Num += 1

print(total)