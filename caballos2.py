# 5 movimientos

total=0
verga = []

x1 = [[1,6],[1,8],[2,7],[2,9],[3,4],[3,8],[4,3],[4,9],[4,0],[6,1],[6,7],[6,0],[7,2],[7,6],[8,1],[8,3],[9,4],[9,2],[0,4],[0,6]]


for x in range(10):
    for y in range(10):
        for x3 in range(10):
            for x4 in range(10):
                for x5 in range(10):
                    for x6 in range(10):
                        verga.append(x)
                        verga.append(y)
                        verga.append(x3)
                        verga.append(x4)
                        verga.append(x5)
                        verga.append(x6)
                        #print(verga)
                        x2=0
                        x22=0
                        x222=0
                        x2222=0
                        x22222=0
                        ddd = []
                    
                        ddd.append(verga[0])
                        ddd.append(verga[1])

                        for z1 in range(20):
                            if ddd==x1[z1]:
                                x2=1

                        
                        
                        ddd = []
                    
                        ddd.append(verga[1])
                        ddd.append(verga[2])

                        for z1 in range(20):
                            if ddd==x1[z1]:
                                x22=1

                        ddd = []
                        ddd.append(verga[2])
                        ddd.append(verga[3])

                        for z1 in range(20):
                            if ddd==x1[z1]:
                                x222=1


                        ddd = []
                    
                        ddd.append(verga[3])
                        ddd.append(verga[4])

                        for z1 in range(20):
                            if ddd==x1[z1]:
                                x2222=1


                        ddd = []
                    
                        ddd.append(verga[4])
                        ddd.append(verga[5])

                        for z1 in range(20):
                            if ddd==x1[z1]:
                                x22222=1


                        if x2==1 and x22==1 and x222==1 and x2222==1 and x22222==1:
                            total = total+1

                        verga=[]

        

print(total)
