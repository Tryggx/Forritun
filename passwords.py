pss=(input('Enter a new password: '))
litill=0
stor=0
tolur=0
for i in (pss):
    if (i>='a' and i<='z'):
        litill=litill+1
    if (i>='A' and i<='Z'):
        stor=stor+1
    if ord(i)>=48 and ord(i)<=57:
        tolur=tolur+1
lengd=litill+stor+tolur
if 6<lengd<20 and litill>0 and stor>0 and tolur>0:
    print('Valid password of lenght ',lengd)
else:
    if !=(6<lengd<20):
        print('Invalid length')
    if !=(litill>0):
        print('At least one lower case letter needed')
    if !=(stor>0):
        print('At least one upper case letter needed')
    if !=(tolur>0):
        print('At least one number needed')

