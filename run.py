f = open("../../output/NewGlobal.txt", "r")
o = open("../../output/NewGlobalwithoutduplicates.txt","w")

exist = []

for x in f:
    if x.replace("\n","") not in exist:
        exist.append(x.replace("\n",""))
        o.write(x)

o.close()
f.close()