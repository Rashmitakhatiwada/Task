#1.Write a Python program that accepts an integer (n) and computes the value of nthntnnn + ...
a = int(input("Input an integer : "))
b=0
summ=0
for i in range (a) :
    b= b * 10 + a

    summ = summ +b
print(summ)




#2.    Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
l = input("enter the number")
l1 = int(l)-17

if int(l1) >= 0 :
    print(int(l1) * 2)

else:
    print(int(l1))


#3. Write a Python program to check whether the input number is prime or not.

n = input("enter a number")
if (n == 1):
    print("input is neither prime nor composite")

    for i in range (2,int(n)+1):

        if (int(n) % int(i) == 0):
            print(n, "prime")

        else:
            print(n, "not prime")

