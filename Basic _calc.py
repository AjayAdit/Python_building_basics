# define a func needed: add, sub,mul,div
#print options to the user
# ask for values
# call the functions
# while loop to continue the program until user wants to exit

def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" +str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" +str(answer))

def mul(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" +str(answer))

def div(a,b):
    answer = a*b
    print(str(a) + "/" + str(b) + "=" +str(answer))

while True:
    print("A.Additiopn")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == 'a' or choice =='A':
        print("Addition")
        a = int (input("Input the 1st number:"))
        b = int (input("Input the 2nd number:"))
        add(a,b)

    elif choice == 'b' or choice =='B':
        print("Subtration")
        a = int (input("Input the 1st number:"))
        b = int (input("Input the 2nd number:"))
        sub(a,b)

    elif choice == 'c' or choice =='C':
        print("Multiply")
        a = int (input("Input the 1st number:"))
        b = int (input("Input the 2nd number:"))
        mul(a,b)

    elif choice == 'd' or choice =='D':
        print("Divide")
        a = int (input("Input the 1st number:"))
        b = int (input("Input the 2nd number:"))
        div(a,b)

    elif choice == 'e' or choice =='E':
        print("Exit")
        quit()
    else:
        print("Wrong Input")




    


