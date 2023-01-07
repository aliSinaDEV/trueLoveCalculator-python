
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Calculate first given name
t_name1 = name1.lower().count("t")
r_name1 = name1.lower().count("r")
u_name1 = name1.lower().count("u")
e_name1 = name1.lower().count("e")

l_name1 = name1.lower().count("l")
o_name1 = name1.lower().count("o")
v_name1 = name1.lower().count("v")

true_in_name1 = t_name1 + r_name1 + u_name1 + e_name1
love_in_name1 = l_name1 + o_name1 + v_name1 + e_name1

# Calculate Second given name
t_name2 = name2.lower().count("t")
r_name2 = name2.lower().count("r")
u_name2 = name2.lower().count("u")
e_name2 = name2.lower().count("e")

l_name2 = name2.lower().count("l")
o_name2 = name2.lower().count("o")
v_name2 = name2.lower().count("v")

true_in_name2 = t_name2 + r_name2 + u_name2 + e_name2
love_in_name2 = l_name2 + o_name2 + v_name2 + e_name2


total_true = true_in_name2 + true_in_name1
total_love = love_in_name2 + love_in_name1
final_total = str(total_true) + str(total_love)


if int(final_total) <= 10 or int(final_total) > 90:
    print(f"Your score is {final_total}, you go together like coke and mentos.")
elif 50 >= int(final_total) >= 40:
    print(f"Your score is {final_total}, you are alright together.")
else:
    print(f"Your score is {final_total}.")
