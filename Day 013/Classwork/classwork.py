1)  მომხმარებელს შემოატანინეთ თავისი გულის ცემა გააკეთეთ პატარა გულის ცემის სისტემა რომელიც ითვლის რა თქმა უნდა გულის ცემას  თუ 180 ზე მეტია ამ შემთხვევაში მაღალია თუ 160-დან 170 მდე არის ამ შემთვევაში არის ნორმალური თუ 160-ზე ნაკლებია ამ შემთხვევაში დაბალია 

heart_rate = int(input("Enter your heart rate: "))
if heart_rate > 180:
    print("Heart rate is high!")
elif 160<heart_rate<170:
    print("Heart rate is normal.")
else:
    print("Heart rate is low!")