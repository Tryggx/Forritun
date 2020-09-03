print('Welcome to car rentals!')
str_x=input('Would you like to continue (y/n)? ')
while (str_x == "y"):
    code=input('Customer code (b or d): ')
    dagar=int(input('Number of days: '))
    start=int(input('Odometer reading at the start: '))
    end=int(input('Odometer reading at the end: '))
    miles=end-start
    print('Miles driven: ',miles)
    if (code=="b"):
        b=float(40*dagar)+(0.25*miles)
        print('Amount due: ',b)
    else:
        if (miles<dagar*100):
            miles=0
        else:
            miles=miles-(dagar*100)
        d=float((60*dagar)+miles*0.25)
        print('Amount due: ',d)
    str_x=input('Would you like to continue (y/n)? ')

