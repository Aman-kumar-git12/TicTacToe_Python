import os
ls = [1,2,3,4,5,6,7,8,9]
def pattern():
    os.system('cls' if os.name == 'nt' else 'clear')
    n = 12
    x = 0
    for i in range(n+1):
        for j in range(n+1):
            if i == 4 or i == 8 or j == 4 or j == 8:
                print("*", end = " ")
            elif( i == 2 or i == 6 or i == 10) and (j == 2 or j == 6 or j == 10):
                print(ls[x], end = " ")
                x+=1
            else:
                print(" ", end = " ")
        print()
        
def verifyUserInput(k):
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if k not in l:
        return False
    k = int(k)
    if ls[k - 1] == 'O' or ls[k - 1] == 'X':
        return False
    return True

def update(k, i):
    if i % 2 == 0:
        ls[k - 1] = 'X'
    else:
        ls[k - 1] = 'O'
        
        
def won():
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in w:
        if ls[a] == ls[b] == ls[c]:
            return ls[a]
    return False
       

i = 0 
pattern()
while i < 9:
    print("User 1 Turn" if i % 2 == 0 else "User 2 Turn")
    print("Enter your Choice (1-9):", end=" ")
    k = input()

    if not verifyUserInput(k):
        pattern()
        print("You Entered Invalid Input")
        continue

    update(int(k), i)
    pattern()

    winner = won()
    if winner:
        if winner == "X":
            print("User 1 won🏆")
        elif winner == "O":
            print("User 2 won🏆")
        break  # Stop the game when a winner is found

    i += 1

if not won():
    print("Game is draw 🫂🫂")