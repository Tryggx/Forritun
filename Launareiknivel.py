# Persónuafsláttur á árinu 2020 verður 655.538 kr., eða  54.628 kr. á mánuði.


pay_hour=int(input("Sláðu inn laun á tímann ")) #miðast við á launaseðli (2579,19kr)
hrs=int(input("Sláðu inn fjölda unna tíma "))
yfir_hrs=int(input("Sláðu inn fjölda yfirvinnutíma "))
yfir_pay=int(input("Sláðu inn Laun á yfirvinnutíma ")) #miðað við launaseðill (4760,55)
laun_fyrir = (pay_hour*hrs)+(yfir_hrs*yfir_pay)
laun_eftir = 0
persona = 54628
lifeyrir = laun_fyrir*0.04
if laun_fyrir < 336916: #fyrsta skattþrep
    laun_eftir = laun_fyrir*0.3504
    laun_eftir = laun_fyrir - laun_eftir - lifeyrir + persona
    print("Laun eftir skatt eru ", laun_eftir)
elif 336916 < laun_fyrir < 945873: #Seinna Skattþrep
    laun_eftir = (laun_fyrir - 336916)*0.3719
    laun_eftir = laun_fyrir-laun_eftir
    laun_eftir = laun_eftir - 118055 - lifeyrir + persona
    print("Laun eftir skatt eru ", laun_eftir)
elif laun_fyrir > 945873: #þriðja skattþrep
    laun_eftir = (laun_fyrir-945873)*0.4624
    laun_eftir = laun_fyrir - laun_eftir
    laun_eftir = laun_eftir - 118055 - 437371 - lifeyrir + persona
    print("Laun eftir skatt eru ", laun_eftir)


