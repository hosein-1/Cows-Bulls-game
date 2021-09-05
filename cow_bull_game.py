import random

'''Notice : bulls mean correct numbers and cows mean incorrect numbers'''

#generate 3 digit number
generate_number = str(random.randint(100 , 999))

    
def playing():
    '''For each correct number that the user enters , a number add to cows_bulls[1] else a number add to cows_bulls[0]'''

    global cows_bulls
    cows_bulls = [0 , 0]

    user_number = input('Enter three number like this -> (249) :')

    for i in range(len(generate_number)):
        if user_number[i] == generate_number[i]:
            cows_bulls[1] += 1

        else:
            cows_bulls[0] += 1

    return cows_bulls            
 
guesses = 0

while True:
    
    playing()
    guesses += 1

    print('You have '+ str(cows_bulls[0]) + ' cows , and '+ str(cows_bulls[1]) + ' bulls')

    if cows_bulls[1] == 3:
        print('You win after ' + str(guesses) + ' times')
        break

    else:
        print('You lose, try again')



