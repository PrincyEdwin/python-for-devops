import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Okay we ill create an instance")
elif type == "t2.medium":
    print("It will cost you 2 dolars")
elif type == "t2.large":
    print("It will cost you 4 dollars")
else:
    print("Please provide a valid instance")

