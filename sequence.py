#fibonacci með 3 tölum
n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1=0
n2=1
n3=2

print(n2)

if (n>1):
    print(n3)
for i in range (1,n-1):
    n4=n1+n2+n3
    n1=n2
    n2=n3
    n3=n4
    print (n4)
    