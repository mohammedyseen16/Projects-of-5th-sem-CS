def leap(year):
    return (((year%400==0) and (year%100!=0)) or (year%4==0)) ;


year = int(input('enter year'))

if (leap(year)) :
  print('leap year')
else:
   print('not a leap year')