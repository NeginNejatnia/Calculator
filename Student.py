name = input('write name :')
familyname = input('write familyname :')
sub1 = int(input('write score1 : '))
sub2 = int(input('write score2 : '))
sub3 = int(input('write score3 : '))

sum = sub1 + sub2 + sub3
average  = sum/3
if average>=17:
    print('Great')
elif 17>average>=12:
    print('Normal')
elif average<12:
    print('fail')