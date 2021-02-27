f = open("../../output/NewGlobal.txt", "r")
o = open("../../output/NewGlobalwithoutduplicates.txt","w")

exist = []
dup = []
cont = 0
for x in f:
    if x.replace("\n","") not in exist:
        exist.append(x.replace("\n",""))
        o.write(x)
    else:
        dup.append(x.replace("\n",""))
        print(x)
        
d = open("duplicates.txt","w")

print(exist)
print(dup)

for x in exist:
    d.write(x)

o.close()
f.close()
d.close()