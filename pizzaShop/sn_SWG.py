import random

def gameproject(machine,you):
    if machine == you:
       return None
    
    elif machine == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
            
    elif machine == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif machine == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False




print("Machine Turn: Enter Water for(w),Snake for(s) and Gun for(g):")
Computer = random.randint(1,3)
if Computer == 1:
    machine = 'w'

elif Computer == 2:
    machine = 's'

elif Computer == 3:
    machine = 'g'

you = input("Your Turn : Enter Water for(w),Snake for(s) and Gun for(g):  ")
game = gameproject(machine,you)

print(f"machine choose {machine}")
print(f"You choose {you}\n")


if game == None:
    print("The game is a Tie")
elif game:
    print("You Win!")
else:
    print("You Lose!")
    

