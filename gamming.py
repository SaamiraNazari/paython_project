# This program will ask the user to guess the correct password. If the user 
# does not enter the correct password in 3 attempts, they lose the game. 
num_of_attempts=0
password = "159357"
print('welcome to the guessing game')
while num_of_attempts < 3:
    user_guess = input('enter your guess')
    num_of_attempts += 1
    if password == user_guess:
        print('you guessed right')
        break
    else:
        print('wrong guess')
        continue
else:
    print('you loose')