name = input("Type your name: ")
print("Welcome ", name, "to this adventure")

answer = input("You are on a Dirt Road, it has come to and end and and you can go to left or right. Which way do you want to go ?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost.")
    else:
        print('Not a vaid option')
elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or go back ? : ").lower()
    if answer == "back":
        print("You go back and loose.")
    elif answer == "cross":
        answer = input("you corssed the bridge and met a strager. Do you talk to them? Yes or No? ").lower()
        if answer == "yes":
            print("You talked to the stranger and he gave you gold. YOU WIN!!!")
        elif answer == "no":
            print("You ignored the stranger, you lost!")
        else:
            print("You lost!!")
    else:
        print("Not a valid option")
else:
    print('Not a vaid option')


print("Thank you for Playing!")