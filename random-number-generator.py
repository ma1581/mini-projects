# import random
# import math
# i=int(input("Enter start:"))
# j=int(input("Enter end:"))
# lt=[]
# for a in range(i,j+1):
#     lt.append(int(a))
# m=1
# w=[]
# p=100/len(lt)
# for i in lt:
#     w.append(p)
# #w=tuple(w)
# while m!=0:
#     gen=random.choices(lt,weights=w)
#     gen=int(gen[0])
#     ind=lt.index(gen)
#     print(gen,"(",math.trunc(w[ind]),"%)",end=" ")
#     prob=w[ind]/2
#     w[ind]=w[ind]-prob
#     prob=prob/(len(w)-1)
#     for p,item in enumerate(w):
#         if p!=ind:
#             w[p]=w[p]+prob
#     w=list(map(lambda a:round(a,1),w))
#     m=int(input("Generate:"))
import random
ch=1 
while ch!=0:
    print(random.randrange(1,10))
    ch=int(input("Generate:"))


