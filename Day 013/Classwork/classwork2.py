age = int(input())
if age < 0:
    print("wrong age!")
elif age < 13:
    print("Child")
elif 13<=age<=19:
    print("Teen")
elif 20<=age<=59:
    print("Adult")
else:
    print("Pensioner")