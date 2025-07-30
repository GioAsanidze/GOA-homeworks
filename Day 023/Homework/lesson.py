#დავალება N1
word = input("please enter word: ")
while word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" and word[len(word)-1] == "a" or word[len(word)-1] == "e" or word[len(word)-1] == "i" or word[len(word)-1] == "o" or word[len(word)-1] == "u" or word[len(word)-1] == "y":
    word = input("please enter word: ")
word = input("please sumbit word: ")
print("Well done")

#დავალება N2
word1 = "აეიოუ"
list = []
for i in range(5):
    guess = input("შეიყვანე სიტყვა რომლის პირველი და ბოლო ასოები არის თანხმოვანი: ")
    if guess[0] not in word1 and guess[-1] not in word1:
        list.append(guess)
print(list)

#დავალება N3
guess2 = input("გთხოვთ შეიყვანოთ სიტყვა: ")
word2 = "აეიოუ"
count = 0
while guess2[0] in word2 or guess2[-1] in word2:
    guess2 = input("გთხოვთ შეიყვანოთ სიტყვა: ")
    count += 1
print("შენ სცადე " + str(count) + "-ჯერ")

#დავალება N4
word3 = "აეიოუ"
for i in range(10):
    guess = input("შეიყვანე სიტყვა რომლის პირველი და ბოლო ასოები არის თანხმოვანი: ")
    if guess[0] not in word3 and guess[-1] not in word3:
        print(guess)

#დავალება N5
word4 = "აეიოუ"
guess3 = input("გთხოვთ შეიყვანეთ სიტყვა: ")
while guess3[0] in word4 or guess3[-1] in word4:
    count_even = 0
    count_odd = 0
    for i in guess3:
        if i in word4:
            count_even += 1
        else:
            count_odd += 1
    print(f"სიტყვაში არის {count_even} ხმოვანი და {count_odd} თანხმოვანი.")
    guess3 = input("გთხოვთ შეიყვანეთ სიტყვა: ")