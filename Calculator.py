import math
type = input('enter your type : ')
number1 = float(input('enter your number : '))

if   type=='cos':
   oper = input('enter operation : ')
elif type=='sin':
   oper = input('enter operation : ')
elif type=='tan':
   oper = input('enter operation : ')
elif type=='cot':
   oper = input('enter operation : ')
elif type=='sqrt':
   oper = input('enter operation : ')
elif type=='factorial':
   oper = input('enter operation : ')

else:
    oper = input('enter operation : ')
    number2 = int(input('enter your number2 : '))

if  oper=='-':
    result = number1 - number2
elif oper=='+':
    result = number1 + number2
elif oper=='*':
    result = number1 * number2
elif oper=='/':
    result = number1 / number2
elif oper=='cos':
    result = (math.cos(math.radians(number1)))
elif oper=='sin':
    result = (math.sin(math.radians(number1)))
elif oper=='tan':
    result = (math.tan(math.radians(number1)))
elif oper=='cot':
    result = (math.cot(math.radians(number1)))
elif oper=='sqrt':
    result = (math.sqrt(number1))
elif oper=='factorial':
    result = (math.factorial(number1))

print('result',result)

