#Winner is whoever rolls a double first. If the computer and user both roll a double, a singular 
#tie-breaker dice will be rolled to determine the winner. Highest number of the tie breaker wins.

import random
urh = [] #user roll history
crh = [] #computer roll history


D1 = list(range(1,7))
D2 = list(range(1,7))
D3 = list(range(1,7))
D4 = list(range(1,7))
D5 = list(range(1,7)) #This is the tie-breaker die

#print(D1)

def rollDice():
    user_roll = []
    computer_roll = []
    
    result_D1 = random.choice(D1)
    user_roll.append(result_D1)
    result_D2 = random.choice(D2)
    user_roll.append(result_D2)
     
    
    result_D3 = random.choice(D3)
    computer_roll.append(result_D3)
    result_D4 = random.choice(D4)
    computer_roll.append(result_D4)
    

    return user_roll
    return computer_roll

def rollTiebreak():
    user_D5 = random.choice(D5)
    computer_D5 = random.choice(D5)
    
    return user_D5
    return computer_D5
    
#---------------------------------------------------------------------------------------------------------------------------------------    
def main():
    
    while True:
        input("Press enter to roll dice")
        i = 0 #this will represent the current turn number for each roll of the dice
        
        user_roll = rollDice()
        print("User rolled: ", user_roll)
        urh.append(user_roll)
        
        computer_roll = rollDice()
        print("Computer rolled: ", computer_roll)
        crh.append(computer_roll)
        
        #user_roll = [1,1]
        #computer_roll = [1,1]
        #The two lines above are used as a test case to see if the program enters the if-statement below
        
        if user_roll[i] == user_roll[i+1] and computer_roll[i] == computer_roll[i+1]:
            doubleDouble = True
            while doubleDouble:
                input("You both rolled doubles. Press enter to roll a tie-breaker")
                user_tiebreak = rollTiebreak()
                print("User: ", user_tiebreak)
                computer_tiebreak = rollTiebreak()
                print("Computer: ", computer_tiebreak)
            
                if computer_tiebreak == user_tiebreak:
                    active = False #this is used to bring the program back to the doubleDouble comparison.Only decisive wins are allowed for each player
                    
                elif user_tiebreak > computer_tiebreak:
                    print("You win")
                    print("This game's data (in lists): ", urh, crh)
                    break
                    
                else:
                    print("You lose")
                    print("This game's data (in lists): ", urh, crh)
                    break
        
        elif user_roll[i] == user_roll[i+1]:
            print("You win!")
            print("This game's data (in lists): ", urh, crh)
            break  
        
        elif computer_roll[i] == computer_roll[i+1]:
            print("You lose!")
            print("This game's data (in lists): ", urh, crh)
            break
            

if __name__ == "__main__":
    main()
