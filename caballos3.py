# 8 movimientos

total=0
efef = []

x1 = [[1,6],[1,8],[2,7],[2,9],[3,4],[3,8],[4,3],[4,9],[4,0],[6,1],[6,7],[6,0],[7,2],[7,6],[8,1],[8,3],[9,4],[9,2],[0,4],[0,6]]


for x in range(10):
    for y in range(10):
        for x3 in range(10):
            for x4 in range(10):
                for x5 in range(10):
                    for x6 in range(10):
                        for x7 in range(10):
                            for x8 in range(10):
                                for x9 in range(10):
                                    efef.append(x)
                                    efef.append(y)
                                    efef.append(x3)
                                    efef.append(x4)
                                    efef.append(x5)
                                    efef.append(x6)
                                    efef.append(x7)
                                    efef.append(x8)
                                    efef.append(x9)
                                    #print(verga)
                                    x2=0
                                    x22=0
                                    x222=0
                                    x2222=0
                                    x22222=0
                                    x21=0
                                    x22=0
                                    x23=0

                                    ddd = []
                                
                                    ddd.append(efef[0])
                                    ddd.append(efef[1])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x2=1

                                    
                                    
                                    ddd = []
                                
                                    ddd.append(efef[1])
                                    ddd.append(efef[2])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x22=1

                                    ddd = []
                                    ddd.append(efef[2])
                                    ddd.append(efef[3])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x222=1


                                    ddd = []
                                
                                    ddd.append(efef[3])
                                    ddd.append(efef[4])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x2222=1


                                    ddd = []
                                
                                    ddd.append(efef[4])
                                    ddd.append(efef[5])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x22222=1

                                    ddd = []
                                
                                    ddd.append(efef[5])
                                    ddd.append(efef[6])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x21=1

                                    ddd = []
                                
                                    ddd.append(efef[6])
                                    ddd.append(efef[7])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x22=1
                                    
                                    ddd = []
                                
                                    ddd.append(efef[7])
                                    ddd.append(efef[8])

                                    for z1 in range(20):
                                        if ddd==x1[z1]:
                                            x23=1



                                    if x2==1 and x22==1 and x222==1 and x2222==1 and x22222==1 and x21==1 and x22==1 and x23==1:
                                        total = total+1

                                    efef=[]

        

print(total)