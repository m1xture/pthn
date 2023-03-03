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



for a in range(1, 10):
    for b in range(0, 10):
        if 10*a+b == a*b+31:
            print(10*a+b)


# k = int(input('k=?'))
# sum = 0
# for i in range(1,k//2+1):
#     if k%i == 0:
#         sum = sum+i
# if sum == k:print(k,'-доскональне число')
# else:print(k,'не є доскональним числом')