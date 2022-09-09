# 15 movimientos
def my_function(x1,efef,m1,m2):
    ddd = []
    ramon = 0
                    
    ddd.append(efef[m1])
    ddd.append(efef[m2])

    for z1 in range(20):
        if ddd==x1[z1]:
            ramon=1
    return ramon
  
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
                                    for x10 in range(10):
                                        for x11 in range(10):
                                            for x12 in range(10):
                                                for x13 in range(10):
                                                    for x14 in range(10):
                                                        for x15 in range(10):
                                                            for x16 in range(10):
                                                                efef.append(x)
                                                                efef.append(y)
                                                                efef.append(x3)
                                                                efef.append(x4)
                                                                efef.append(x5)
                                                                efef.append(x6)
                                                                efef.append(x7)
                                                                efef.append(x8)
                                                                efef.append(x9)
                                                                efef.append(x10)
                                                                efef.append(x11)
                                                                efef.append(x12)
                                                                efef.append(x13)
                                                                efef.append(x14)
                                                                efef.append(x15)
                                                                efef.append(x16)
                                                                #print(verga)
                                                                x2=0
                                                                x22=0
                                                                x222=0
                                                                x2222=0
                                                                x22222=0
                                                                x21=0
                                                                x22=0
                                                                x23=0
                                                                x24=0
                                                                x25=0
                                                                x26=0
                                                                x27=0
                                                                x28=0
                                                                x29=0
                                                                x30=0
                                                                

                                                                x2 = my_function(x1,efef,0,1)
                                                                x22 = my_function(x1,efef,1,2)
                                                                x222 = my_function(x1,efef,2,3)
                                                                x2222 = my_function(x1,efef,3,4)
                                                                x22222 = my_function(x1,efef,4,5)
                                                                x21=my_function(x1,efef,5,6)
                                                                x22=my_function(x1,efef,6,7)
                                                                x23=my_function(x1,efef,7,8)
                                                            
                                                                x24=my_function(x1,efef,8,9)
                                                                x25=my_function(x1,efef,9,12)
                                                                x26=my_function(x1,efef,10,11)
                                                                x27=my_function(x1,efef,11,12)
                                                                x28=my_function(x1,efef,12,13)
                                                                x29=my_function(x1,efef,13,14)
                                                                x30=my_function(x1,efef,14,15)
                                                                

                                                                if x2==1 and x22==1 and x222==1 and x2222==1 and x22222==1 and x21==1 and x22==1 and x23==1 and x24==1 and x25==1 and x26==1 and x27==1 and x28==1 and x29==1 and x30==1:
                                                                    total = total+1

                                                                efef=[]

        

print(total)
