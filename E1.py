y=int(input('Enter Your Required Year:  '))
if(y%400==0)or(y%4==0 and y%100!=0):
    print(f'{y}is Leap Year')
else:
    print(f'{y}is not Leap Year')