a,b = 0,1
number=int(input('Enter the number : '))
print('The first ',str(number),'fibonacci numbers are -')
print(a)
while b<number:
        print(b)
        a, b = b, a + b

