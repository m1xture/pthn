# a = float(input( 'a=? ' ))
# b = float(input( 'b=? ' ))

# if abs (a/b-b/ (a-b) ) <0.001:
#     print( 'Так' )
# else:
#     print( 'Ні' )



# n=int(input('n=?'))
# s = 0
# while n>0:
#     d = n%10
#     s = s+d
#     n = n//10

# print('s = ', s)



# for a in range(1, 10):
#     for b in range(0, 10):
#         if 10*a+b == a*b+31:
#             print(10*a+b)


# k = int(input('k=?'))
# sum = 0
# for i in range(1,k//2+1):
#     if k%i == 0:
#         sum = sum+i
# if sum == k:print(k,'-доскональне число')
# else:print(k,'не є доскональним числом')


# todo: Інтернет Магазин Smart. Ivanov M.V.


s = int(input('ВВедіть суму покупки'))
v=0
if s<500:
    v=0
elif s>-500 and s<1000:
    v-s/100*5
else:
    v=s/100*10
r=s-v
print('Вітаємо в нашому інтернет-магазині')
print('Товарний чек')
print('Сума покупки-', s, 'грн')
print('Сума снижки-', v, 'грн')
print('Вам потрібно сплатити-', r, 'грн')
print('Дякуємо за покупку')


# todo: Кількість речень. Ivanov M.V.


w=input('Введіть текст:')
k=0
n=len(w)
for i in range(n):
    l=str(w[i])
    if l=='.' or l=='?':
        k=k+1
        print('Кількість речень:',k)


# todo: НСД. Ivanov M.V.


a=int(input('a='))
b=int(input('b='))
while a*b !=0:
    if a>=b:
        a=a%b
    else:
        b=b%a
nsd=a+b
print('Найбільший спільний дільник', nsd)