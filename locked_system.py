# Write a short program that simulates a lock system. A user should be able to enter the correct username and password when prompted to do so.   
#  The user gets three tries to enter the correct username and password. If the user does not enter the correct username and password in those
#  three login attempts, display to the screen “LOGIN ATTEMPT FAILED: ACCOUNT IS NOW LOCKED.” If the user is able to enter the correct username
#  and password, display to the screen “LOGGING INTO ACCOUNT…” 

print('Welcome to the Lock System!')
username=['samira','sajjad','hossain']
password=['Ss147258','Sn123456','123456']
num_tries=0
while num_tries<3:
 user=input('User inputs username : ')
 passwd=input('User inputs password  : ')
 num_tries +=1
 if user in username and passwd in password:
     print(f'LOGGING INTO ACCOUNT... {user}!')
     break
 else:
     print(f'Incorrect username or password!')
else:
    print(f'LOGIN ATTEMPT FAILED. ACCOUNT IS NOW LOCKED.!')