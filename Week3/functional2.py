# '''
# In pure functional programming:
#
# 1. everything is a function
# 2. functions are "pure" and have no side effects
# 3. data structures are immutable
# 4. state is preserved inside a function
# 5. recursion is used instead of loops/iteration
#
# Advantages:
#
# 1. Absence of side effects makes your programs more robust
# 2. Programs are more modular and have smaller building blocks
# 3. Easier to test - same parameters return same results
# 4. Easier to fit with parallel or concurrent programming
# 5. Much less namespacing == fewer mistakes and collisions
#
# Disadvantages:
#
# 1. Solutions can look very different and are not as intuitive
# 2. Not equally useful for all types of problems
# 3. I/O are side effects
# 4. Recursion is much more complex to understand than loops/iteration
# 5. In Python recursion is slow
#
# Take away:
#
# Use the good parts!
# 1. Write functions to minimize side effects
# 2. Keep everything contained in a function
# 3. Keep functions small and modular
# 4. Write better tests
# '''
#
# # Pure functional programming languages can have no loops and control structure:
# # Normal statement-based flow control
# '''
# if <cond1>:   func1()
# elif <cond2>: func2()
# else:         func3()
# '''
# # Equivalent functional expression
# '''
# (<cond1> and func1()) or (<cond2> and func2()) or (func3())
# '''
# # Example:
# x = 3
#
# def pr(s):
#     return s
#
#
# x = 5
# print(x == 1 and pr('one')) or (x == 2 and pr('two')) or (pr('other'))
#
#
# pr = lambda s: s
# namenum = lambda x: (x==1 and pr("one")) \
#                 or (x==2 and pr("two")) \
#                 or (pr("other"))
#
# print(namenum(2))
#
# # normal iteration loop construction
# '''
# for element in lst:
#     func(element)
# '''
# # Equivalent functional expression
# '''
# map(func, lst)
# '''
# # Example
#
# def double_it(num_list):
#     new_out = []
#     for num in num_list:
#         new_out.append(num *2)
#     return new_out
#
# print(double_it([1,2,3,4,5,6]))
#
#
# def double(num):
#     return num * 2
#
# print(map(double, list(range(1,7))))
#
# # # OR
# #
# print(map(lambda x: x*2, list(range(1,7)))) # no way to test!

# using a functional approach will flatten code:

# Nested loop for finding big products
def find_bm(lst1, lst2):
    bigmults = []
    for x in lst1:
        for y in lst2:
            if x * y > 25:
                bigmults.append((x,y))
    return bigmults


xs = [1,2,3,4]
ys = [10,15,3,22]

print(find_bm(xs, ys))
