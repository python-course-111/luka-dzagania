def calculator():
    a=int(input('seiyvane riccxvi1:'))
    b=int(input('seiyvane riccxvi2:'))
    d=['-','*','**','+','/']
    c=input('seiyvane nisani:')
    while c not in d:
        c=input('seiyvane nisani:')
    try:
        if c=='+':
            return(a+b)
        elif c=='-':
            if a>b:
                return(a-b)
            elif a<=b:
                return(b-a)
        elif c=='/':
            if a>b:
                return(a/b)
            elif a<=b:
                return(b/a)
        elif c=='*':
            return(a*b)
        elif c=='**':
            return(a**b)
    except:
        return('error')
    
print(calculator())