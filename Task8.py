# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('введите размер  школодаки n - '))
m = int(input('введите размер  школодаки m - '))
k = int(input('введите  количество долек k - '))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Можно разделить одним разломом')
else:
    print('Нельзя разделить одним разломом')