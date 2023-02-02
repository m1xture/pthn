a = float(input( 'a=? ' ))
b = float(input( 'b=? ' ))

if abs (a/b-b/ (a-b) ) <0.001:
    print( 'Так' )
else:
    print( 'Ні' )