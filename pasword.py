usernam = {
      'samira':'123456',
      'hossain':'147258',
     'sajad':'159632'
   } 
 
enterusername= input('enter your username')
entrpass= input('enter your pass:')
 
     
while enterusername  not in  usernam or usernam[enterusername] != entrpass:
     print('it is not true')
     enterusername= input('enter your username again')
     entrpass= input('enter your pass again:')  

print('you log in  successful')