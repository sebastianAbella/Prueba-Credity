def tripleta (val):
    for a in range(0,int(val)):
        for b in range(0,int(val)):
            c = val -a-b
            if a*a + b*b == c*c and a<b and b<c :
                print ('valor de A = '+str(a))
                print ('valor de B = '+str(b))
                print ('valor de C = '+str(c))
                print ('TOTAL = '+str(a+b+c))                
                print ('reultado valor A^2 + B^2 = '+str(a*a + b*b))
                print ('resutado valor C^2 = '+str(c*c))
            
tripleta(1000)