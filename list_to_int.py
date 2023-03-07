 #From the given list of integers create a number whose digits are the elements of the list.
my_l= [4,2,3]
b=0
for i in my_l:
     b= b*10+i
print(b,end="")

 #Sort the given list of integers without using python method.

my_l = [54, 1, 12, 99, 20, 13, 5, 100]
b= len(my_l)
for i in range(b-1):
    for j in range(i+1, b):
        if(my_l[i])>my_l[j]:
            my_l[i],my_l[j]=my_l[j],my_l[i]
print (my_l)