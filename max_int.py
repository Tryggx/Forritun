num_int = int(input("Input a number: ")) 
max_int = 0    # Do not change this line
while num_int>0:
    if num_int>max_int:
        max_int=num_int
        num_int = int(input("Input a number: ")) 

   
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line