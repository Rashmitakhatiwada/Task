# def message(text):
#     print(f"this is  {text}  from the function ")
#
# message("i study python")

# def square_a_no(value):
#     return value**2
#
# print(square_a_no(3))

# def fanc(name):
#     print("hello",name)
#
# print(fanc("jane")) #function itself calls print so feri print garda none auxa


# def custon_sort(my_l):
#
#     b = len(my_l)
#     for i in range(b - 1):
#         for j in range(i + 1, b):
#             if (my_l[i]) > my_l[j]:
#                 my_l[i], my_l[j] = my_l[j], my_l[i]
#     return my_l
#
#
# my_l = [54, 1, 12, 99, 20, 13, 5, 100]
# result=custon_sort(my_l)
# print(result)

# def list_to_int(my_l):
#
#     b = 0
#     for i in my_l:
#         b = b * 10 + i
#     return b
#
#
# my_l =[4, 2, 3,5,7]
# my_new_l =[4, 2, 3,5,7,9,1]
# result=list_to_int(my_l)
# result1=list_to_int(my_new_l)
# print(result)
# print(result1)

#create a new  list and move the repetative number in that list


def repetative_items(nums):

    new_nums=[]
    for i in nums:
        if nums.count(i) > 1 and i not in new_nums:
            new_nums.append(i)
    return new_nums


nums=[3,4,2,2,1,3,3,3]
result= repetative_items(nums)
print(result)