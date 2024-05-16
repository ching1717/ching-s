1 ~ 100 中的所有奇數和

【1】
sum = 0 
for x in range(1, 101): 
    if x %2 !=0:
        sum = sum + x 

print(sum)

【2】
sum = 0 
for x in range(1, 101): 
    if x %2 !=0:
        continue
    sum = sum + x 

print(sum)

【3】
sum = 0 
for x in range(1, 101,2): 
    sum = sum + x 

print(sum)

409012428 徐怡晴

印星星(一)
*
**
***
****
n=4
for i in range(1,n+1):
     print('*'*i)

印星星(二)
****
***
**
*
n=4
for i in range(n,0,-1):
     print('*'*i)