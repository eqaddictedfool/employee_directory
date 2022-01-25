import csv

def newhire():
    # new user input
    first_name = input("Enter user's first name: ")
    last_name = input("Enter user's last name: ")
    userID = input("Enter user's ID: ")
    title = input("Enter user's title: ")


    
            # field names 
    fields = ['First Name', 'Last Name', 'userID', 'Title', 'Status'] 
    
            # data rows of csv file 
    rows = [first_name,last_name,userID,title,"True"], 

    
            # writing to csv file 
    with open('employee_list.csv', 'w') as csvfile: 
            # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
            # writing the fields 
    csvwriter.writerow(fields) 
        
            # writing the data rows 
    csvwriter.writerows(rows)

menu=True
while menu:
    print ("""
    1.Add an employee
    2.Update an employee
    3.remove an employee
    4.exit
    """)
    menu=input("what would you like to do?")
    if menu == "1":
        newhire()

    elif menu == "2":
        pass

    elif menu == "3":
        pass

    elif menu == "4":
        pass

    elif menu != "":
        print("Invalid option")

    

    






menu()