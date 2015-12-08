# write a function (mult) that takes two numbers and returns the result
# of multiplying those two numbers together
def mult(num1,num2):
    return num1 * num2
# now write a function(apply_it) that takes three arguments: a function,
# and two arguments and returns the result of calling the function with
# the two arguments
def apply_it(funct, arg1, arg2):
    return funct(arg1, arg2)

print(apply_it(mult, 3, 4))
