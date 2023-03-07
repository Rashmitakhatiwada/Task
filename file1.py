#  #1. “Python + is + an + awesome + language”. Split the given string to get a list and join to get another string “Python is an awesome language”

s= ("python is an awesome language")
x=s.split()
print(x)
y=" " .join(x)
print(y)

#. write a Python program to create a dictionary from a string. Track the count of the letters from the string.
#Input = “broadway”
#Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}

# def string_dict(s):
#
#     dic={}
#     for i in s:
#         if i in dic:
#             dic[i] +=1
#         else:
#             dic[i]=1
#     return dic
#
# s= ("broadway")
# result= string_dict(s)
# print(result)


#3.Write a Python program to combine two dictionaries by adding values for common keys.
#output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

# def combined_dict(d1,d2):
#
#     d3={}
#     for i,j in d1.items():
#         for x,y in d2.items():
#             if i==x:
#                 d3[i]=(j+y)
#     return d3
#
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# result = combined_dict(d1,d2)
# print(result)

#4.  Write a program to check whether a string is anagram or not. An anagram of a string is another string that contains
#the same characters, only the order of characters can be different. For example, "silent" and "listen" are an anagram of each other.


# def isanagram(s1,s2):
#
#     if len(s1)==len(s2):
#         s_s1 = sorted(s1)
#         s_s2= sorted(s2)
#         if s_s1==s_s2:
#             return "is anagram "
#         else:
#             return "not anagram"
#     else:
#         return "not anagram"
#
# s1= input("enter first string")
# s2= input("enter second string")
# result = isanagram(s1,s2)
# print(result)

# #Check whether a number is palindrome or not.Palindrome numbers are those which remain same even on reversing.
# #Examples - 111, 131, 222, 212 etc.
#
# def ispalendrome(n):
#     revers= str(n)[::-1]
#     if n == revers:
#         return "it  is palendrome"
#     else:
#         return "it is not a palendrome"
#
#
# n=input(str("enter the number"))
# result = ispalendrome(n)
# print(result)