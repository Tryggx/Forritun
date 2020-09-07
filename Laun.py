
target=int(input("Sláðu inn markmið ")) #markmið miðast við eftir skatt 
is_pay=str(input('Er tímagjald vitað? (y/n) ')) # tímagjald miðast við eftir skatt 
pay=0
if is_pay=="y":
    pay_hour=int(input("Sláðu inn tímagjald "))
    hrs = target/pay_hour
    print("með",pay_hour,"á tímann þarf",int(hrs),"tíma til að ná markmiði")
elif is_pay=="n":
    for i in range(1900,2900,100):
        hrs=target/i
        print("fyrir ",target, "þarf",int(hrs), "tíma", "með",int(i), "á tímann")
        pay=hrs*i
        if pay>=target:
            print(round(hrs,2))

