g =open("C:/Users/Hp Laptop/Desktop/scores.txt","r")
w =open("C:/Users/Hp Laptop/Desktop/outpo.txt","w")
series =[]
c = []
pn =[]
final =[]
for line in g.readlines():
    series.append(line)
    line = line.split(':')
    if pn ==[]:
        pn.append(line[0])
        pn.append(line[1])
    elif line[0] not in pn and line[1] not in pn:
        pn.append(line[0])
        pn.append(line[1])
    elif line[0] not in pn:
        pn.append(line[0])
    elif line[1] not in pn:
        pn.append(line[1])
    c.extend(line)
k =[[ 0 for a in range(6)] for v in range(len(pn)) if pn[v]!='\n']
for p in range(len(pn)):
    for L in range(len(series)):
        Ln = series[L].split(':')
        if pn[p]==Ln[0]:
            Rn = Ln[2].split(',')
            for R in range(len(Rn)):
                k[p][3] += int(Rn[R][0])
                k[p][5] += int(Rn[R][2])
                if int(Rn[R][0])>int(Rn[R][2]):
                    k[p][2] +=1
                elif int(Rn[R][0])<int(Rn[R][2]):
                    k[p][4] +=1
        if pn[p]==Ln[1]:
            Rn = Ln[2].split(',')
            for R in range(len(Rn)):
                k[p][3] += int(Rn[R][2])
                k[p][5] += int(Rn[R][0])
                if int(Rn[R][0])>int(Rn[R][2]):
                    k[p][4] +=1
                if int(Rn[R][0])<int(Rn[R][2]):
                    k[p][2] +=1
for p in range(len(pn)):
    for L in range(len(series)):
        Ln = series[L].split(':')
        if pn[p]==Ln[0]:
            Rn = Ln[2].split(',')
            if len(Rn) == 5 or len(Rn)==4:
                for r in range(len(Rn)):
                    fsw,fsl= 0,0
                    if Rn[r][0]>Rn[r][2]:
                        fsw +=1
                    if  Rn[r][0]<Rn[r][2]:
                        fsl +=1
                if fsw>fsl:
                    k[p][0] +=1
            if len(Rn) ==3 or len(Rn)==2:
                for z in range(len(Rn)):
                    tsw,tsl =0,0
                    if Rn[z][0]>Rn[z][2]:
                        tsw +=1
                    if Rn[z][0]<Rn[z][2]:
                        tsl +=1
                if tsw>tsl:
                    k[p][1]+=1
    tsw,tsl = 0,0
    fsw,fsl = 0,0
p =0
ss =0
info = ['\n', 'names','5SMW','3SMW','TSW','TGW','TSL','TGL','\n']
info = ' '.join(info)
w.writelines(info)
final.append('\n')
while p < len(pn):
    while ss<len(k):
        final.append(pn[p])
        for s in range(len(k[ss])):
            final.append(k[ss][s])
        final.append('\n')
        ss +=1
        p +=1
for st in range(len(final)):
    if type(final[st]) != str:
        final[st] = str(final[st])
final = ' '.join(final)
print("Now You can open output.txt file to see result")
w.writelines(final)
g.close()
w.close()