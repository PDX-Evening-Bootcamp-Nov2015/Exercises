# write a function (is_even(n)) that returns true or false depending on whether
# a number is even or not
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# now write a function (filter_it) that takes a function and a list and returns
# a new list of numbers that are even.

lizt = list(range(2, 78))
#the list comprehension way:
filter_it2 = [num  for num in  lizt  if is_even(num) == False  ]
print (filter_it2)


#
# def filter_it(funct, lizt):
#     new_list = []
#     for i in lizt:
#         if funct(i):
#             new_list.append(i)
#     return new_list
#
# print(filter_it(is_even, liszt))




#
#
#
#
# lizt = list(range(20))
