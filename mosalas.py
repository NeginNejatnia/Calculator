a = float(input('side first :'))
b = float(input('side second :'))
c = float(input('side third :'))

if a<b+c and b<a+c and c<a+b:
    print ('Yes,we have triangle')
#elif a==b and b==c:
#    print ('Motesavi Azla')
#elif a==b or a==c or b==c:
#    print ('Motesavi saghein')

else:
    print ('No,we Do not have triangle')

