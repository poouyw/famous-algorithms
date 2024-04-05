def karatsuba(x, y):
#baresi chand ragami bodan adad
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
# tedad argam baraye joda krdn
        n = len(str(x))
        n_half = n // 2
        
# joda krdn adad ba asas len adad ma
#        a = int(str(x)[:n_half])
#        print(a)
#        b = int(str(x)[n_half:])
#        print(b)
#        c = int(str(y)[:n_half])
#        print(c)
#        d = int(str(y)[n_half:])
#        print(d)
        a = x//10**(n_half)
        b = x%10**(n_half)
        c = y//10**(n_half)
        d = y%10**(n_half)

#emal zarb karatsuba
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_bc = karatsuba((a+b),(c+d))
#zarb megdar bazgashti
        return (ac * (10**(2*n_half))) + (ad_bc -ac-bd) * (10**(n_half))+bd


k = karatsuba(123,567)
print(k)