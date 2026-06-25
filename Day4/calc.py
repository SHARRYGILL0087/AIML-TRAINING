a = float(input("Enter a ->"))
o = input("Enter + - * / -> ")
b = float(input("Enter b ->"))

if(o=="+") :
    print(a+b)
elif(o=="-") :
    print(a-b)
elif(o=="*") :
    print(a*b)
elif(o=="/"):
    if(b==0) :
        print("Not Defined")
    else :
        print(a/b)
else :
    print("Invalid Operator")