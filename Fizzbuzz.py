x_int=int(input("Slaðu inn tölu "))
for i in range(x_int,100):
    if i%5==0 and i%3==0:
        print('Fizz Buzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0: 
        print('Fizz')
    else:
        print(i)
    