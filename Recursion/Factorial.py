def fact(x):
    if x <= 1:
        return 1
    return x*fact(x-1)
   
for i in range(6):
    print(fact(i),end = ' ')
# a=[2,3,4,5]
# for i in a:
#     print(list(i+1 for i in a))



    