# keywords:
def add(x,y):
    return x + y

addition = add(2,3)
print(addition)

#break :

a = input("Enter your Name : ")

for i in a:
    if i =="A":
        print("Found A")
        break
    else:
        print(" Not Found A")
        
#pass

x = int(input("Enter a number: "))

for x in range(1,5):
    if(x % 2 == 0):
        pass 
    else:
        print("Iam in else")
        
#continue

var  = 10

while (var > 0):
    var = var-1
    if var == 5:
        continue
    
    print(f"The value of a variable is : {var}")
print("Good bye")

