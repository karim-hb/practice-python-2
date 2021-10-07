import math

def add(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def sine(num1):
    return math.sin(math.radians(num1))

def cosine(num1):
    return math.cos(math.radians(num1))

def tang(num1):
    return math.tan(math.radians(num1))

def cotg(num1):
    return 1 / tang(num1)

def log(num1):
    return math.log(num1)

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. sinos\n" \
        "6. cosinos\n" \
        "7. tangant\n" \
        "8. cotangant\n" \
        "9. loagaritm\n")  
  
  

select = int(input("Select operations form 1 t0 9 :"))
if (select >=1 and select <=4):
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
  
    if select == 1:
        print(number_1, "+", number_2, "=",add(number_1, number_2))
    elif select == 2:
        print(number_1, "-", number_2, "=",subtract(number_1, number_2))
    elif select == 3:
        print(number_1, "*", number_2, "=",multiply(number_1, number_2))
    elif select == 4:
        print(number_1, "/", number_2, "=",divide(number_1, number_2))
    
elif (select > 4 and select <= 8):
    number_1 = float(input("enter the degree: "))

    if select == 5:
        print("sinose",number_1,"=" , sine(number_1))
    if select == 6:
        print("cosinose",number_1,"=" , cosine(number_1))
    if select == 7:
        print("tangante",number_1,"=" , tang(number_1))
    if select == 8:
        print("cotangant",number_1,"=" , cotg(number_1))
elif (select == 9):
     number_1 = float(input("enter the number: "))
     print("loagaritm",number_1,"=" , log(number_1))

else:
        print("Invalid input")
