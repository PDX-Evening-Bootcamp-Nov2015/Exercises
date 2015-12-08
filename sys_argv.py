import sys

print( "IMPORTANT", sys.argv[0])
for item in sys.argv:
    print(item)


def adder(array):
    cat = ''
    for item in array:
        cat += item
    print(cat)

adder(sys.argv)
