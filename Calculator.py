import math

number1 = int(input('enter your number : '))
oper = input('enter your oper : ')

if oper =='cos':
    result = (math.cos(number1))
elif oper =='sin':
    result = (math.sin(number1))
elif oper =='tan':
    result = (math.tan(number1))
elif oper =='cot':
    result = (math.cot(number1))
elif oper =='sqrt':
    result = (math.sqrt(number1))
elif oper =='factorial':
    result = (math.factorial(number1))
else:
    number2 = int(input('enter your number2 : '))  
    if  oper =='-':
        result = number1 - number2
    elif oper =='+':
        result = number1 + number2
    elif oper =='*':
        result = number1 * number2
    elif oper =='/':
        result = number1 / number2

print('result',result)
