from art import logo_cal
print(logo_cal)

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {"+": add,
           "-": minus,
           "*": mul,
           "/": div}

user = input("What's the first numer?: ")

for symbol in operation:
    print(symbol)
