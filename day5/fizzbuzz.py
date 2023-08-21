my_range = range(0,101)

for num in my_range:
    string=''
    if(num%3==0):
        string+='Fizz'
    if(num%5==0):
        string+='Buzz'
    if(len(string)>0):
        print(string)
    else:
        print(num)
