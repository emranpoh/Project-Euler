import math

count = 0

# for i in range(1,300,1):
#     totalCount = 0

#     d = math.log(i)/math.log(4)

#     thisone = ""

#     for n in range(1,int(d)+1,1):
        
#         u = 4**(n+1)

#         y = (i+(u-1-((i+u-1)%u)))/u
#         thisone += str(y) + " "
#         totalCount += y


#     if(d > 0):
#         if((4**int(d)) == i):
#             x = (4**d)
#             count += 1
#             totalCount -= 1
#             print "Need to minus ----->",i,d,x,count,totalCount

#     print i,"\t",d,"\t",int(d)+1,"\t",thisone,"(",totalCount,")"

for i in range(1,50,1):

    totalCount = 0

    d = math.log(i)/math.log(4)

    for n in range(1,int(d)+1,1):
        
        u = 4**(n+1)

        y = (i+(u-1-((i+u-1)%u)))/u

        totalCount += y

    if((d > 0) and (4**int(d)) == i):
        totalCount -= 1

    if(totalCount == 0):
        totalCount = 1

    print i,"\t",totalCount