 #From the given list of integers create a number whose digits are the elements of the list.
my_l= [4,2,3]
new_l=0
for i in my_l:
    print(i,end="")

 #Sort the given list of integers without using python method.

my_l = [15, 26, 15, 1, 23, 64, 23, 76]

for i in range(len(my_l)):
    for j in range(i+1, len(my_l)):
        if(my_l[i])>my_l[j]:
            my_l[i],my_l[j]=my_l[j],my_l[i]
print (my_l)