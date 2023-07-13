# importing random module
import random

# start game level instrusctions
user_level=input('******Choose Level****** \n 1.Beginner(1-20) \n 2.Intermidiate(1-100) \n 3.Hard(1-1000) \n\n provide level: ')
user_level=int(user_level)
level=0
if user_level==1:
    level=20
elif user_level==2:
    level=100
elif user_level==3:
    leve=1000 
else:
    print('Invalid user input')
    exit(1)
#  correct guess the number
chances= 0
guess_number = random.randint(1,level)
i=0
while i<5:
 user_number= int(input(f'Enter guess number (1 -{level})  : ') )
 chances +=1
 if user_number==guess_number:
  print('Guess is correct')
  print('You won,and you used ' +  str(chances) +' chances'  )
  break
 else:
    print('Guess is wrong')
    
    if user_number > user_level:
          print('Number is out of level range')
    elif user_number > guess_number:
         print('Your guess is too high try again!!')    
    else:
        print('Your guess is too low try again!!')
 i=i+1
print('Program Ended, Thanks for guessing')