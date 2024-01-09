print("           CALCULATOR\n")
try:
    n1=int(input("Enter Operand 1: "))
    n2=int(input("Enter Operand 2: "))
except ValueError:
    print("\n!!Wrong Input!!")
    exit()
ch="y"
res=0
while ch=="y":
    op=input("\nEnter Operator: ")
    if op=="+":
        res=n1+n2
    elif op=="-":
        res=n1-n2
    elif op=="*":
        res=n1*n2
    elif op=="/":
        try:
            res=n1/n2
        except ZeroDivisionError:
            print("Cannot Divide by Zero")
    elif op=="%":
        res=n1%n2
    elif op=="^" or op=="**":
        res=n1**n2
    else:
        print("\n!!Wrong Input!!")
        exit()
    print("\nResult is: ",res)
    ch=input("\nPerform more Calculation (y/n): ")
    if ch=='y':
        p=input("On Previous Result (y/n): ")
        if p=='y':
            n1=res
            n2=int(input("\nEnter Operand 2: "))
        else:
            res=0
            n1=int(input("\nEnter Operand 1: "))
            n2=int(input("Enter Operand 2: "))
    else:
        exit()
    

    
