import sys

av = sys.argv[1]

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()
if not (av.lstrip("-").isdigit()):
    print("AssertionError: argument is not an integer")
    sys.exit()

number = int(sys.argv[1])


if(number % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")