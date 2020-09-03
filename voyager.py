days=int(input('Number of days after 9/25/09: '))
time=(days*24)
Miles=16637000000+(38241*time)
km=Miles*1.609344
au=Miles/92955887.6

print('Miles from the sun: ',round(Miles))
print('Kilometers from the sun: ',round(km))
print('AU from the sun: ',round(au))
