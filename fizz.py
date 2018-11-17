
n = 3
for i in range(1, n+1):
    print(i)
    tmp = ''
    print(i % 3)   
    if i % 3 == 0:
        tmp = tmp + 'Fizz'
            
    print(n % 5)   
            
    if i % 5 == 0:
        tmp = tmp + 'Buzz'
                
    if (i % 3 != 0) and (i % 5 != 0):
         tmp = tmp + str(i)

    print('tmp', tmp)           
