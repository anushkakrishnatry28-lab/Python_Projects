def contact():
    contacts=[]
    a=int(input("Enter the number of contacts:- "))
    for i in range(0,a):
        dict={
            "contact_name":input("Enter the name:- "),
            "contact_no":int(input("Enter the number:- ")),
            "email":input("Enter the email:- ")}
        contacts.append(dict)
        
    while True:
        operation=int(input("1. Add\n2. Update\n3. Delete\n4. Search\n5. View\n6. Exit\nEnter your  choice"))
        if operation==1:
            dic={"b":input("Enter the name:- "),
                 "c":int(input("Enter the number:- ")),
                 "d":input("Enter the email:- ")}
            contacts.append(dic)
            print("Contact added successfully")
        elif operation==2:
            update=input("Enter the name want to update:- ") 
            for j in contacts:
                if j["contact_name"]==update:
                    j["contact_name"]=input("Enter the contact:- ")
                    j["contact_no"]=int(input("Enter the number:- ")) 
                    j["email"]=input("Enter the email:- ")                   
                    print("Contact updated successfully")
        elif operation==3:
            delete=input("Enter the name want to delete:- ")
            for k in contacts:
                if k["contact_name"]==delete:
                    contacts.remove(k)
        elif operation==4:
            search=input("Enter the name want  to search:- ")
            for h in contacts:
                if h["contact_name"]==search:
                    print(h["contact_name2"],h["contact_no"],h["email"])
        elif operation==5:
            print(contacts)
        else:
            print("You are exit")
            break                
                            
contact()                  
            
            