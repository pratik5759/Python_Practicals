num1=int(input("Enter First No :"))
num2=int(input("Enter Second No :"))
num3=int(input("Enter Third No :"))
num4=int(input("Enter Fourth No :"))

if((num1<num2) and (num1<num3) and (num1<num4)):
    print(num1,"is smallest Amongst all")
elif((num2<num1) and (num2<num3) and (num2<num4)):
    print(num2,"is smallest Amongst all")   
elif((num3<num1) and (num3<num2) and (num3<num4)):
    print(num3,"is smallest Amongst all")
else:
    print(num4,"is smallest Amongst all")      

