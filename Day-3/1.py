a="1"
b="1"
print(a+b) #output will be 11 as print treats a and b as string for ex if a had hello and b had world then a+b would be simply helloworld , we can avoid this in above manner 
print(int(a)+int(b))#typecasting

c=1 
d =2 
print(c+d)#this will give required int output

#typecasting 
#conversion of one datatype to other datatype is called as typecasting 

#implicit TypeCasting
e=1   #int
f=2.4 #float

print(e+f)#it will give float as a output as python automatically converts to another data type to prevent data loss 
