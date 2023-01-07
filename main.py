
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love_score = l + o + v + e

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true_score = t + r + u + e

final_total = str(true_score) + str(love_score)


if int(final_total) <= 10 or int(final_total) > 90:
    print(f"Your score is {final_total}, you go together like coke and mentos.")
elif 50 >= int(final_total) >= 40:
    print(f"Your score is {final_total}, you are alright together.")
else:
    print(f"Your score is {final_total}.")
