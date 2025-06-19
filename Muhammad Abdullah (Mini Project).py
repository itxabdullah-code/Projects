global categories,balance,description
with open("D:\\data.txt","w") as f:
    f.write("Expenses File With Muhammad Abdullah\n")
    f.close() 
def add(amount,category,description):
    amount1=int(amount)
    global total
    total=0
    total=total+amount1
    category1=category
    description1=description
    with open("D:\\data.txt","a") as f:
        f.write(f"Amount= {amount1} ,Category= {category1} ,Description= {description1}\n")
        f.close()
def view():
    try:
        with open("D:\\data.txt","r+") as f:
            print(f.read())
            f.close()
    except FileNotFoundError as fn:
        print(fn)        
def cal():
    # print(f"Total expenses are: {total}")
    sum=0
    with open("D:\\data.txt","r") as f:
        for line in f:
            single= line.split()
            for digit in single:
                if digit.isdigit():
                    sum=sum + int(digit)    
    print("Total Budget = ",sum,"\n")
def call():
    sum=0
    with open("D:\\data.txt","r") as f:
        for line in f:
            single= line.split()
            for digit in single:
                if digit.isdigit():
                    sum=0
                    sum=sum+digit    
    print("Total Budget = ",sum,"\n")
def main():
    print("1. Adding")
    print("2. viewing")
    print("3. calculating")   
    print("4. Exit") 
    value=int(input("enter integer value: "))
    try:
        value=int(value)
    except ValueError as ve:
        print(ve)
    while(value!=4 and value<=4):
        if value==1:
            amount=input("Enter amount: ")
            category=input("Enter category: ")
            description=input("Enter description: ")
            add(amount,category,description)
            main()
        elif value==2:
            view()
            main()
        elif value==3:
            cal()
            main()
        elif value==4:
            break
        else:
            print("Invalid input")
main()