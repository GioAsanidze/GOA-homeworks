#დავალება N1
systolic = int(input())
diastolic = int(input())
if systolic > 140 or diastolic > 90:
    print("მაღალი წნევა")
elif systolic < 90 or diastolic < 60:
    print("დაბალი წნევა")
else:
    print("წნევა ნორმალურია")

#დავალება N2
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
if age <= 10:
    if weight <= 20:
        print("წონა დაბალია")
    elif 20 < weight < 40:
        print("წონა ნორმალურია")
    elif weight >= 40:
        print("წონა მაღალია")
elif 10 < age < 17:
    if weight <= 40:
        print("წონა დაბალია")
    elif 40 < weight < 65:
        print("წონა ნორმალურია")
    elif weight >= 65:
        print("წონა მაღალია")
else:
    if weight <= 50:
        print("წონა დაბალია")
    elif 50 < weight < 90:
        print("წონა ნორმალურია")
    elif weight >= 90:
        print("წონა მაღალია")

#დავალება N3
Age = int(input("Enter your age: "))
time = int(input("Enter what time it is at the moment(0:00 - 23:00): "))
if Age < 18 and time >= 22:
    print("დროა დაძინების")
elif Age >= 60 and time >= 21:
    print("დასვენება რეკომენდირებულია")
else:
    print("შეგიძლიათ გააგრძელოთ აქტივობა")

#დავალება N4
user_age = int(input("Enter your age: "))
heart_rate = int(input("Enter your heart rate: "))
if user_age < 30 and heart_rate < 140:
    print("შეგიძლიათ მეტი ივარჯიშოთ")
elif user_age >= 30 and heart_rate > 170:
    print("დასვენება გჭირდებათ")
else:
    print("აქტივობის დონე ნორმალურია")

#დავალება N5
User_Age = int(input("Enter your age: "))
if 0 <= User_Age <= 12:
    print("ბევრი ვიტამინიანი საკვები")
elif 13<= User_Age <= 25:
    print("ენერგიის მომცემი საკვები")
elif 26<= User_Age <= 59:
    print("ბალანსირებული რაციონი")
else:
    print("დაბალკაროლიური და მსუბუქი საკვები")
