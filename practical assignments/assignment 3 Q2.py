num=int(input("Enter a Number :"))
add=0
seprated=0
while num>0:
    seprated=int(num%10)
    add=add+seprated
    num=int(num/10)
print("the addition is ",add)    
