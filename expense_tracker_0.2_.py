import json
from collections import Counter
from datetime import date

def add_expenses() :
    try :
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
            
        #take info
        name=input("Enter expense name : ")
        amount= input("Enter expense amount : ")
        category=input("Enter expense category : ")
        while True :
            if not name :
                name=input("\nPlease name expense anything :")
                if not name :
                    print("Empty name is not acceptable  ")
                    continue
            try :
                 amount=float(amount)
            except ValueError :
                  amount=input("Enter expense amount again : ")
                  continue
            if not amount :
                amount=float(input("Enter expense amount : "))
                continue
            if amount<=0 :
                 amount=float(input("Please enter a positive number as amount : "))
                 continue
                   
            if not category :
                category=input("Enter category : ")
                if not category :
                    print("Empty category is not acceptable ")
                    continue
            break
        #create a expense
        expense = {
        "name" : name,
        "amount" : amount,
        "category" : category,
        "date" : str(date.today())
        }
        #add the expense to expnses
        expenses.append(expense)
        #update on json folder
        with open("expenses.json","w") as file :
                json.dump(expenses, file, indent=4)
    except FileNotFoundError :
         print("File not found ")
    else :
        print("Expense added successfully")
    finally :
         print("Returning to homepage ")
    
def show_expenses() :
    try :
        #open the folder as read mode
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
        if expenses :
            for position,expense in enumerate(expenses, start=1):
                print("\n====EXPENSES====")
                print(f"{position}. ",
                f"{expense['name']} ~~",
                f"{expense['amount']} ~~",
                f"{expense['category']} ~~",
                f"{expense['date']}")
                
        else :
             print("There is no expenses to show")
    except FileNotFoundError :
        print("File not found")
    finally :
        print("Returning to home page")
        
def total_expenses() :
    try :
        #open the folder as read mode
        with open("expenses.json", "r") as file :
            expenses= json.load(file)
            total=0
            if expenses :
                for expense in expenses :
                    total=total+expense["amount"]
    except FileNotFoundError :
        print("File not found")
    except ValueError :
        print("Enter a number as amount")
    else :
        print("Total expense : ",total)
    finally :
        print("Returning to homepage")
"""
~~~~~Different way to search expense


def search_expense() :
    try :
        with open("expenses.json", "r") as file :
            expenses= json.load(file)
            if expenses :
                namee=input("Enter expense name you want to find : ")
                for expense in expenses :
                    if expense["name"].lower() ==namee.lower() :
                            print(f"\n {expense['name']}~~{expense['amount']}~~{expense['category']}")
                    else :
                        print("No expenses to search")
    except FileNotFoundError :
        print("File not found ")
"""
        
def search_expense():
        try :
            #open the folder as read mode
            with open("expenses.json", "r") as file :
                expenses = json.load(file)
                
                search=input("Enter the name of expense you want to search : ")
                found = False 
                for expense in expenses :
                    if search.lower() in expense["name"].lower() :
                        print("===Search Result===")
                        print(
                            f"{expense['name']} ~~",
                            f"{expense['amount']} ~~",
                            f"{expense['category']}")
                        found=True
                if not found :
                         print("\nInvalid expense name")
        except FileNotFoundError :
                print("File not found")
        finally :
            print("Returning to homepage")
        
def delete_expense() :
   try :
        #open the folder as read mode
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
        show_expenses()
        number = int(input("Enter the serial number of expense you want to delete : "))
        if 1<=number<=len(expenses) :
            deleted_expense=expenses.pop(number-1)
            #open the folder as write mode
            with open("expenses.json", "w") as file :
                    json.dump(expenses, file, indent = 4)
                    print(f"Deleted : {deleted_expense['name']}",
                    f"~~{deleted_expense['amount']}",
                    f"~~{deleted_expense['category']}")
        else :
           print("\nInvalid expense number")
   except FileNotFoundError :
           print("File not found")
   except ValueError :
       print("Please enter a valid number as number ")
   finally :
       print("Retutning to homepage")

def update_expense():
    try :
        with open("expenses.json", "r") as file :
            expenses= json.load(file)
            if expenses :
                show_expenses()
               
                found= False
                choice = input("Enter the name of expense  you want to update : ")
                for expense in expenses :
                    if choice.lower()==expense["name"].lower() :
                        #take new details
                        new_name=input("Enter your new expense name : ")
                        new_amount=input("Enter your new expense amount : ")
                        new_category=input("Enter your new expense category : ")
                        while True :
                            if not new_name :
                                new_name=input("Enter new expwnse name : ")
                                if not new_name :
                                    print("Enter new expense name : ")
                                    continue
                            try :
                                new_amount=float(new_amount)
                            except ValueError :
                                new_amount=input("Enter new expense amount : ")
                                continue
                            if not new_amount :
                               new_amount=input("Enter expense amount : ")
                               continue
                            elif new_amount<=0 :
                                 new_amount=input("Please enter new amount any positive number : ")
                                 continue
                            if not new_category :
                                new_category=input("Enter new category : ")
                                if not new_category :
                                    print("Empty category is not acceptable ")
                                    continue
                        break
                        
                        
                        #update the dictionary  
                        expense["name"]=new_name
                        expense["amount"]=new_amount
                        expense["category"]=new_category
                        
                        #open the folder as write mode
                        with open("expenses.json", "w") as file :
                                json.dump(expenses, file, indent=4)
                                found = True
                if not found :
                        print("\nInvalid expense name ")
            else :
                   print("\nYour expense tracker is empty . Please add some expense")
    except FileNotFoundError :
             print("File not found")
    except ValueError :
          print("Please enter a valid number as amount")
    else :
        print("Expense updated successfully")
    finally :
        print("Returning to the home page")

def show_categories() :
     try :
          with open("expenses.json", "r") as file :
               expenses=json.load(file)
               categories=[] 
               if expenses :
                    for expense in expenses :
                         categories.append(expense["category"])
                    unique_categories=set(categories) 
                    print("\nYour categories are : ",unique_categories)
                    while True :
                        print("If you want to count how many repetation has each categories then type 1 & for exit type 2 ")
                        
                        choice = input("Enter your choice : ")
                        if choice == "1":
                            print(Counter(categories))
                        elif choice=="2":
                            print("Home page")
                            break
                        else :
                            print("Invalid choice")
               else :
                     print("\nEmpty expenses")
     except FileNotFoundError :
          print("\nFile not found")
     finally :
         print("Returning to the homepage")

def amount_info():
    try :
          with open("expenses.json", "r") as file :
                  expenses=json.load(file)
                  print("\n1. Total expense\n2. Highest expense\n3. Minimum expense")
                  choice=input("Enter what you want to know : ")
                  amounts=[]
                  for expense in expenses :
                          amounts.append(expense["amount"])
                  if choice=="1" :
                          total=sum(amounts)
                          print("Total expense : ",total)
                  elif choice =="2":
                          highest_expense =max(amounts)
                          print("Highest expense : ",highest_expense)
                  elif choice == "3" :
                          lowest_expense= min(amounts)
                          print("Lowest expense : ",lowest_expense)
                  else :
                          print("Please choice valid number")
    except FileNotFoundError :
          print("File not found")
    finally :
          print("Returning to the homepage")
          
def compare_info() :
    try :
          with open("expenses.json","r") as file :
              expenses=json.load(file)
              if not expenses :
                   print("\nThere is no expenses to show")
                   return
              any_above_1000= any(expense["amount"] >1000 for expense in expenses )
              all_above_10= all(expense["amount"]>= 10 for expense in expenses)
              if any_above_1000 :                                                                 print("\nIs there any expense amout above 1000 ? : ",any_above_1000)
              else :
                  print("\nThere is no expense amount above 1000")
              if all_above_10 :
                  print("\nIs all expense amount above 10 :", all_above_10)
              else :
                  print("\nNot all of expenses amount are above 10")
    except FileNotFoundError :
        print("File not found")
    finally :
        print("Returning to the homepage")
        
def search_by_date() :
    try :
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
            if not expenses :
                print("Your expense tracker is empty")
                return
            datee=input("Enter date (yyyy-mm-dd) : ")
            found=False
            for position,expense in enumerate(expenses,start=1) :
                if datee==expense["date"] :
                    print(f"{position}. {expense['name']} ~~ {expense['amount']} ~~ {expense['category']}")
                    found=True
            if not found :
                print("Invalid date ")
    except FileNotFoundError :
        print("File not found")
    finally :
        print("Returning to home page")
        
def search_between_date() :
    try :
            with open("expenses.json", "r") as file :
                expenses=json.load(file)
            if not expenses :
                print("Your expense tracker is empty")
                return
            start_date=input("Enter start date (yyyy-mm-dd) :")
            end_date=input("Enter end date (yyyy-mm-dd) : ")
            found=False
            for position,expense in enumerate(expenses,start=1) :
                if start_date<=expense["date"]<=end_date :
                    
                    print(f"{position}. {expense['name']} ~~ {expense['amount']} ~~ {expense['category']}")
                    found = True
            if not found :
                 print("Invalid dates")
    except FileNotFoundError :
             print("File not found")
    finally :
         print("Returning to homepage")
         
def monthly_report() :
    try :
         with open("expenses.json", "r") as file :
             expenses=json.load(file)
         if not expenses :
             print("Your expense tracker is empty")
             return
         year = input("Enter year : ")
         month=input("Enter month : ")
         found=False
         monthly_total=0
         for position, expense in enumerate(expenses, start =1) :
             if year +"-" + month==expense["date"][0:7] :
                 print(f"{position}. {expense['name']} ~~ {expense['amount']} ~~ {expense['categoey']} ~~ {expense['date']}")
                 monthly_total=monthly_total +expense["amount"]
              
                 found =True      
         if not found :
             prin-t("No data found in this month")
         print("Total monthly expense : ",monthly_total)
    except FileNotFoundError :
             print("File not found")
    finally :
          print("Returning to homepage")
             
def category_month_report():
    try :
          with open("expenses.json", "r") as file :
             expenses=json.load(file)
          if not expenses :
             print("Your expense tracker is empty")
             return
          year=input("Enter year : ")
          month=input("Enter month : ")
          categoryy=input("Enter category : ")
          found=False
          total=0
          for position,expense in enumerate(expenses, start=1) :
             if year+"-"+month==expense["date"][0:7] and categoryy==expense["category"] :
                 print(f"{position}. {expense['name']} ~~ {expense['amount']} ~~ {expense['category']} ~~ {expense['date']}")
                 total=total+expense["amount"]
                 found=True
          if not found :
             print("There is no expense match with your information ")
          print("Your total expense : ",total)
    except FileNotFoundError :
        print("File not found")
    finally :
        print("Returning to homepage")
        
def category_result() :
    try :
          with open("expense.json", "r") as file :
             expenses=json.load(file)
          if not expenses :
             print("Your expense tracker is empty")
             return
          categoryy=input("Enter category : ")
          found=False
          all_amount=[]
          print(f"====={categoryy.upper()} RESULT=====") 
          for position,expense in enumerate(expenses,start=1) :
              if categoryy==expense["category"] :
                 print(f"{position}. {expense['name']} ~~ {expense['amount']} ~~ {expense['category']} ~~ {expense['date']}")
                 all_amount.append(expense["amount"])
                 found=True
          print("Total amount : ",sum(all_amount))
          print("Minimum amount : ",min(all_amount))
          print("Maximum amount",max(all_amount))
          print("Average amount : ",sum(all_amount)/len(all_amount))
          if not found :
             print(f"There is no expense category named {categoryy}")
    except FileNotFoundError :
             print("File not found")
    finally :
             print("Returning to homepage")
             
def category_spending_rank():
    try :
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
        if not expenses :
            print("Your expense tracker is empty")
            return
        categories=[]
        for expense in expenses :
            categories.append(expense["category"])
        category_count=Counter(categories)
        category_totals={}
        for category in category_count :
           total=0
           for expense in expenses :
               if category==expense["category"] :
                   total=total+expense["amount"]
           category_totals[category]=total
        print("====CATEGORY SPENDING====")
        for category, total in category_totals.items() :
             print(f"{category} : {total}")
        highest = max(category_totals, key= category_totals.get)
        lowest=min(category_totals, key= category_totals.get)
        total_spending=sum(category_totals.values())
        avg_spending=total_spending/len(category_totals)
        print("====SPENDING DETAILS====")
        print("\nHighest spending : ", highest)
        print("Amount : ",category_totals[highest])
        print("\nLowest spending : ", lowest)
        print("Amount : ",category_totals[lowest])
        print("\nTotal spending : ", total_spending)
        print("\nAverage spending : ",avg_spending)
    except FileNotFoundError :
         print("File not found")
    finally :
         print("Returning to homepage")
         
def category_ranking() :
    try :
         with open ("expenses.json", "r") as file :
             expenses=json.load(file)
         if not expenses :
             print("Your expense tracker is empty")
             return
         categories=[]
         for expense in expenses :
             categories.append(expense["category"])
         category_count=Counter(categories)
         category_totals={}
         for category in category_count :
             total=0
             for expense in expenses :
                 if category==expense["category"] :
                     total=total+expense["amount"]
             category_totals[category]=total
         sorted_categories = sorted(category_totals, key= category_totals.get, reverse=True)
         print("====CATEGORY RANKING====")
         for position,(category,amount) in enumerate(sorted_categories, start=1):
             print(f"{position}. {category} : {category_totals[category]}")
    except FileNotFoundError :
         print("File not found")
    finally :
         print("Returning to homepage")
         
def category_rank_percentage() :
    try :
         with open("expenses.json", "r") as file :
             expenses=json.load(file)
         if not expenses :
             print("Your expense tracker in empty")
             return
         categories=[]
         for expense in expenses :
             categories.append(expense["category"])
         category_count=Counter(categories)
         category_totals={}
         for category in category_count :
             total=0
             for expense in expenses :
                 if category==expense["category"] :
                     total=total+expense["amount"]
             category_totals[category]=total
         total_spending=sum(category_totals.values())
         sorted_category=sorted(category_totals, key= category_totals.get, reverse=True)
         print("====CATEGORY RANKING====")
         for position,category in enumerate(sorted_category, start=1) :
              amount=category_totals[category]
              percentage=amount/total_spending*100
              print(f"{position}. {category}  |  {category_totals[category]}  |  {percentage : .1f}")
    except FileNotFoundError :
         print("File not found")
    finally :
         print("Returning to homepage")
         
def highest_spending_day() :
    try :
        with open("expenses.json", "r") as file :
            expenses=json.load(file)
        if not expenses :
            print("Your expense tracker is empty")
            return
        dates=[]
        for expense in expenses :
            dates.append(expense["date"])
        indi_date=Counter(dates)
        all_date={}
        for date in indi_date :
            total=0
            for expense in expenses :
                if date==expense["date"] :
                    total=total+expense["amount"]
            all_date[date]=total
        sorted_date=sorted(all_date, key=all_date.get,reverse= True)
        print("    Each Day Spending")
        for position,date in enumerate(sorted_date, start=1) :
            print(f"{position}. {date}  |  {all_date[date]}")
        highest=max(all_date, key = all_date.get)
        lowest=min(all_date, key= all_date.get)
        print("\n\nHighest spending date : ",highest,"  |  amount : ",all_date[highest])
        print("Lowest spending date : ",lowest,"  |  amount : ",all_date[lowest])
    except FileNotFoundError :
            print("File not found")
    finally :
            print("Returning to homepage")
            
def filtering_expense_amount() :
    try :
         with open("expenses.json", "r") as file :
             expenses=json.load(file)
         if not expenses :
             print("Your expense tracker is empty")
             return
         categoryy=input("Enter category : ")
         min_amount=input("Enter minimum amount : ")
         while True :
             if not categoryy :
                 categoryy=input("Enter category : ")
                 if not categoryy :
                     print("Empty category is not acceptable")
                     continue
             try :
                 min_amount=float(min_amount)
             except ValueError :
                 min_amount=input("Enter minimum amount : ")
                 continue
             if min_amount<=0 :
                 min_amount=input("Enter any positive amount : ")
                 continue
             break
         filtered_expense=[]
         for expense in expenses :
             if categoryy==expense["category"] and min_amount<=expense["amount"] :
                 filtered_expense.append(expense)
         sorted_expense=sorted(filtered_expense, key=lambda expense : expense["amount"], reverse=True)
         print(f"For {categoryy} & minimum amount : {min_amount} we have : ")
         for position,expense in enumerate(sorted_expense, start=1) :
             print(f"{position}. {expense['name']}  |  {expense['category']}  |  {expense['amount']}")
    except FileNotFoundError :
        print("File not found")
    finally :
        print("Returning to homepage ")
        
def spending_summery() :
 try :
  with open("expenses.json", "r") as file :
      expenses=json.load(file)
  if not expenses :
      print("Your expense tracker is empty")
      return
  min_amount=input("Enter minimum amount : ")
  if min_amount.lower()=="all" :
      print("Your all expenses are : \n")
      for position,expense in enumerate(expenses,start =1) :
          print(f"{position}. {expense['name']}  |  {expense['category']}  |  {expense['amount']}  |  {expense['date']}")
      highest=max(expense["amount"] for expense in expenses)
      lowest=min(expense["amount"] for expense in expenses)
      sum_amount=sum(expense["amount"] for expense in expenses)
      avg_amount=sum_amount/len(expenses)
      print("\nHighest expense : ",highest,"\nLowest expense : ",lowest,"\nTotal expense : ",sum_amount,"\nAverage amount : ",avg_amount)      
          
  elif min_amount != "all" :
   while True :
    try :
        min_amount=float(min_amount)
    except ValueError :
        min_amount=input("Enter minimum amount : ")
        continue
    if min_amount<=0 :
        min_amount=input("Please enter any positive amount : ")
        continue
    break
   sum_expense=[]
   for expense in expenses :
       if min_amount<=expense["amount"] :
           sum_expense.append(expense)
   sorted_expense = sorted(sum_expense, key= lambda expense : expense["amount"], reverse=True)
   for position,expense in enumerate(sorted_expense, start=1) :
       print(f"{position}. {expense['name']}  |  {expense['category']}  |  {expense['amount']}  |  {expense['date']}")
   if sorted_expense :
    highest=max(expense["amount"] for expense in  sorted_expense)
    lowest=min(expense["amount"] for expense in sorted_expense)
    expense_num=len(sorted_expense)
    total_expenses=sum(expense["amount"] for expense in sorted_expense)
    avg_amount=total_expenses/len(sorted_expense)
    print("\nTotal expense : ",total_expenses)
    print("Highest expense : ",highest)
    print("Lowest expense : ",lowest)
    print("Expense number : ",expense_num)
    print("Average amount : ",avg_amount)
   if not sorted_expense :
        print("\nTotal expense : 0")
 except FileNotFoundError :
      print("File not found")
 finally :
      print("Returning to homepage")
      
  
#home page                                                    
while True :
    print("=====EXPENSE TRACKER=====")
    print("\n1. Add expense\n2. View expense\n3. Total expense\n4. Search expense\n5. Delete expense\n6. Update expense\n7. Show categories\n8. Amount info\n9. Compare information\n10.Search by date\n11. Search between date\n12. Monthly report\n13. Category month report\n14. Category result\n15. Category spending rank\n16. Category ranking\n17. Category rank percentage\n18. Highest spending rank\n19. Filtering expense amount\n20. Spending summery\n21. Exit ")
    
    choice=input("\nWhat do you want to do ?  ")
    if choice == "1":
        add_expenses()
    elif choice=="2":
        show_expenses()
    elif choice=="3":
        total_expenses()
    elif choice=="4":
        search_expense()
    elif choice=="5":
        delete_expense()
    elif choice=="6":
        update_expense()
    elif choice=="7":
        show_categories()
    elif choice=="8":
        amount_info()
    elif choice=="9":
        compare_info()
    elif choice=="10":
        search_by_date()
    elif choice=="11" :
        search_between_date()
    elif choice=="12":
        monthly_report()
    elif choice=="13":
        category_month_report()
    elif choice=="14":
        category_result()
    elif choice=="15" :
        category_spending_rank()
    elif choice=="16" :
        category_ranking()
    elif choice=="17" :
        category_rank_percentage()
    elif choice=="18" :
        highest_spending_rank()
    elif choice=="19" :
        filtering_expense_amount()
    elif choice=="20" :
        spending_summury()
    elif choice=="21" :
        print("Goodbye ")
        break
    else :
        print("Please choose between 1-21")