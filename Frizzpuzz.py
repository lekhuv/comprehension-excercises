result =[('frizzbuzz') if(i%15 ==0) else 'buzz'if i%5 ==0 else 'frizz' if i%3 ==0 else i for i in range(0,100)]

for x in range(1, 101):
    if x%15 == 0:
        print('fizzbuzz')
    elif x%5 == 0:
        print('buzz')
    elif x%3 == 0:
        print('fizz')
    else:
        print(x)