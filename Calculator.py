def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter the number (0 to calculate): "))
    return [ans,t]
def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0
    ans = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter the number (0 to calculate): "))
    return [ans,t]
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter the number (0 to calculate): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print(" Enter '+' for Addition")
    print(" Enter '-' for Subtraction")
    print(" Enter '*' for Multiplication")
    print(" Enter '/' for Average")
    print(" Enter 'q' for Quit")
    c = input(" ")
    if c != 'q':
        if c == '+':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '-':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '*':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == '/':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid input")
    else:
        break
