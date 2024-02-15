print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play: ")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What does GPU stand for? ")
if answer.lower() == "grpahics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What does RAM stand for? ")
if answer.lower() == "random acess memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score / 4) * 100) + "%.")