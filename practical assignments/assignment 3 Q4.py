num=int(input("Enter a Number :"))
print("---------------------------------")
num_copy=num
add=0
while num_copy>0:
    print("Number before seperation :-",num_copy)
    #seperating last digit from no 
    sep=int(num_copy%10)
    print("seperated no ",sep)
    #getting cube of seperated no
    cube=sep*sep*sep
    print("cube ",cube)
    #adding cube 
    add=add+cube
    print("addition",add)
    #removing last digit from number
    num_copy=int(num_copy/10)
    print("number after seperation",num_copy)
    print("---------------------------------")
    
if(add==num):
    print(num,"is Armstrong number")
else:
    print(num,"is Not Armstrong number")    