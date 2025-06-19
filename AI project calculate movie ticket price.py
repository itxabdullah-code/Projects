age=int(input("enter your age: "))
no_ticket=int(input("enter number of tickets: "))
price=0
if(age<18):
    price=8
    if(no_ticket<3):
        price= price*no_ticket
    else:
        price=price*no_ticket
        price=price-(price*10/100)
    print(price)
elif age>=18 and age<=60:
    price=15
    if(no_ticket<3):
        price= price*no_ticket
    else:
        price=price*no_ticket
        price=price-(price*10/100)
    print(price)
else:
    price=10
    if(no_ticket<3):
        price= price*no_ticket
    else:
        price=price*no_ticket
        price=price-(price*10/100)
print(f"\nAge= {age}\nTotal number of tickets= {no_ticket}\nTotal price= {price}")        
        