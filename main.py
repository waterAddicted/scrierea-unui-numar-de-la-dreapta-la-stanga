'''
Varianta 1
100-->1
'''

n = int(input())
r = 0
while n:
    r = r * 10 + n % 10
    n = n // 10
print(r) 


'''
Varianta 2 M1
100-->001
'''
a = int(input())
while a:
    print(a%10,end='')
    a //= 10
print('\n')
'''
Varianta2 M2
'''
b = input()
for i in range(len(b)-1,-1,-1):
    print(b[i],end='')
