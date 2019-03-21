a=input('Enter name for first person : ')
a0='Enter age for '+a+' : '
a1=int(input(a0))

b=input('Enter name for second person : ')
b0='Enter age for '+b+' : '
b1=int(input(b0))

if  a1>b1:
    print(a,' is elder than ',b)
else:
    print(b,' is elder than ',a)
