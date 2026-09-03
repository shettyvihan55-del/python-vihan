

simple caluculator

a = int(input("enter the first number:"))
b = int(input("enter your second number:"))

print("Addition:" , a+b)
print("Subtraction:" , a-b)
print("Multiplication:" , a*b)
print("Division:" , a/b)

#student marks calculation
name = input("enter your name:")
m1=int(input("enter your python marks:"))
m2=int(input("enter your java marks:"))
m3=int(input("enter your SQL marks:"))
total =m1+m2+m3
print("\n---- student report -----")
print("Total marks:" , total)
print("average marks:",total/3)


#shopping bill caluculator
price1 = int(input("enter the price of first item:"))
price2 = int(input("enter  the price of second item:"))
price3 =int(input("enter the price of third item:"))
total = price1+price2+price3
discount = total*0.1
final_price = total-discount
print("\n---- shopping bill -----")
print("TOTAL PRICE:" , total)
print("discount :" ,discount)
print("final price:" ,final_price)


#assignment operator
x = 10
x +=5
print("x after addition:",x)

x -=3
print("x after substraction:",x)
    
x *=2
print("xafter multilication ",x)

x/=3
print("x after division:",x)

#bank balance
balance = 10000

deposit = 5000
balance +=deposit
print("After deposit:", balance)
withdraw =2000
balance -=withdraw
print("after withdraw:",balance)


















































































































