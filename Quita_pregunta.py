import json

def PascalPiramid(cont):
    # definción de variables
    piramid =[]
    # recorrido de numero de filas de la piramide 
    for ind in range(0,int(cont)):
        # verifica si el arreglo de la piramide es mayor a uno 
        if int(len(piramid)) >= int(1):
            if len(piramid) == 1:
                piramid.insert(1,[{ "num": len(piramid) }, { "num": len(piramid) }] )
            elif len(piramid) > 1 :
                # recorre la ultima posicion de la piramide para operar e insertar
                totals = []
                totals.insert(0 , { "num": 1 })
                for act  in range(0,len(piramid[len(piramid)-1])):
                    # valida si existe una posicion nueva y contruye la nueva fila
                    if  act+1 <= len(piramid[len(piramid)-1])-1:
                        val_old = json.dumps(piramid[len(piramid)-1][act])
                        val_new = json.dumps(piramid[len(piramid)-1][act+1])
                        vold = json.loads(val_old)
                        vnew = json.loads(val_new)
                        total = int(vold["num"]) + int(vnew["num"])
                        totals.insert(0,{"num": total})
                totals.insert(0, { "num": 1 })
                piramid.insert(len(piramid),totals)
        else:
            piramid.insert(0,[{"num":1}])
    calculateDivisible(piramid)
    
def calculateDivisible(piramid):
    number_divitrue = 0
    number_divifalse = 0
    #trae todas las filas y lee los numeros
    for item in range(0,len(piramid)):
        #print(len(piramid[item]))
        for nums in range(0,len(piramid[item])):
            val = json.dumps(piramid[item][nums])
            valnumb = json.loads(val)
            modular = int(valnumb["num"]) % 7 
            #valida de los numeros cuales son divisibles
            if modular == 0:
                number_divitrue = number_divitrue + 1    
            else:
                number_divifalse = number_divifalse + 1
                
    print('numeros divisibes = '+ str(number_divitrue))
    print('numeros NO divisibes = '+ str(number_divifalse))

PascalPiramid(100)
