expenses= []

def add_expense():
    amount= int(input("\nEnter your amount of expense : "))
    category= input("Enter your expense category : ")
    description= input("Write something about your expense : ")
    date=input("Enter date (yyyy/mm/dd) : ")
    
    expense= { "amount": amount,
                        "category": category,
                        "description": description,
                        "date": date
    }
    expenses.append(expense)
    print("\nYour expense has been added succesfully")
    
def show_expenses():
    if not expenses :
        print("\nThere is no expenses to show : ")
        
    for expense in expenses:
        print("\n1. Amount : ",expense["amount"],
            "\n2. Category : ",expense["category"],
            "\n3. Description : ",expense["description"],
            "\n4. Date : ",expense["date"] )


def search_expense():
    if not expenses:
        print("\nSorry!There is no expense you can search")
    categoryy=input("Enter category you want to search : ")
    for expense in expenses:  
        if expense["category"]==categoryy:
            print("\n1. Amount : ",expense["amount"],
            "\n2. Category : ",expense["category"],
            "\n3. Description : ",expense["description"],
            "\n4. Date : ",expense["date"] )
        else :
                print(f"\nInvalid category! There is no expense named {categoryy}")
        
def delete_expense():
    show_expenses()
    if not expenses:
        print("\nThere is no expense to delete")
    
    categoryy=input("\nEnter category you want to delete from your record : ")
    for expense in expenses:
        if expense["category"]==categoryy:
            expenses.remove(expense)
            print("\nYour expense has been deleted succesfully")
        
def total_expense():
    if not expenses:
        print("\nYour expense list is empty")
        
    total=sum(expense["amount"]  for expense in expenses)
    print("Your total expense is : ",total)
       
def update_expense():
    if not expenses :
        print("\nThere no expense to update")
    
    categoryy=input("Enter category of your expense you want to update : ")    
    for expense in expenses:
        if expense["category"]==categoryy:
            expense["amount"]= int(input("Enter new amount : "))
            expense["description"]=input("Enter new description : ")
            expense["date"]=input("Enter new date : ")     
            
        else :
            print(f"Invalid category ! There is no expense named {categoryy}")


while True:
    
    print("""
    \n____________________
    \n1. Add expense
    \n2. Show expense
    \n3. Search expense(by category)
    \n4. Dlete expense
    \n5. Update expense
    \n6. Total expense
    \n7. exit"""
    )
    
    choice=input("\nPlease choose by serial number what you want to do : ")
    
    if choice =="1":
        add_expense()
    elif choice=="2":
        show_expenses()
    elif choice=="3":
        search_expense()
    elif choice=="4":
        delete_expense()
    elif choice=="5":
        update_expense()
    elif choice=="6":
        total_expense()
    elif choice=="7":
        print("Good bye sir")
    else :
        print("Invalid choice ! Please choose between 1-7.")