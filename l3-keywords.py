#keywords
#break
a = input("Enter a word...")
length_of_a = len(a)
for i in a:
    if(i == 'A'):
        print("A is found")
        break
    else:
        print("A is not found")
 ## This else block is optional; it's executed if the loop completes without a break
        
#activity2
'''x = int(input("Enter a number :"))
for x in range(10):
    if x % 20 == 0:
        print("Twist ...")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("buzz5")
    elif x % 3 == 0:
        print("buzz3")
    else:
        print(x) '''  
       
#The pass keyword in Python is used as a placeholder for future code. It is often used in places where syntax requires a statement but you don't want to execute any code, such as in an empty function, class, or loop 
#x = int(input("Enter a number :"))
for x in range(10):
    if x % 2 != 0:
        pass #get only odd values
    else:
        print(x)

#activity3: continue is going to skip, that one iteration

var = 10           #initialise         
while var > 0:     #iterate loop         
   var = var - 1
   if var == 5:       
      continue        #continue statement
     
   print ('\nCurrent variable value :', var)
print ("\nGood bye!")


for i in range(1,10):
    if i %3 == 0:
        continue
    print(i)

print("I printed only numbers which are not divisible by 3")


#ACP
price = 2.50
#define a function to calculate the difference between the amount given and price mentioned
def calculate_change(amount_given):
	return amount_given - price

c = calculate_change(10.00)
print("Change the customer is due", c)


    
        