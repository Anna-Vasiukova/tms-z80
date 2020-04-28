s = input()
x=list(s)
if (x[::1])==(x[::-1]):
    print ('polindrom')
else:
    print('not polindrom')


