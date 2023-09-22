import getpass
import re
import datetime

current_user=""

class User:
    rigestered_users=[]
    def __init__(self, first_name,last_name ,email,password,mobile_phone):
        
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.mobile_phone=mobile_phone
        self.__class__.rigestered_users.append(self)

    def user_add(self):
        file = open('backup.txt','w')
        for instance in self.__class__.rigestered_users:
            file.write(f"{instance.first_name}-{instance.last_name}-{instance.email}-{instance.password}-{instance.mobile_phone}\n")
        file.close()

class Project:
    projects=[]
    def __init__(self,title,details,total_target,start_date,end_date,owner):
        self.title=title
        self.details=details
        self.total_target=total_target
        self.start_date=start_date
        self.end_date=end_date
        self.owner=owner
        self.__class__.projects.append(self)
    @classmethod
    def project_add(cls):
        file = open('backup_project.txt','w')
        for instance in cls.projects:
            file.write(f"{instance.title}_{instance.details}_{instance.total_target}_{instance.start_date}_{instance.end_date}_{instance.owner}\n")
        file.close()             

def register_user():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")
        password = getpass.getpass("Enter your password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        mobile_phone = input("Enter your mobile phone number: ")

        #name validation
        if not re.match(r'^[a-zA-Z_]', first_name):
            print("enter valid name")
            return
        if not re.match(r'^[a-zA-Z_]', last_name):
            print("enter valid name")
            return
        



        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address format.")
            return
        
        

        # Validate password match
        if password != confirm_password:
            print("Passwords do not match.")
            return

        # Validate Egyptian phone number format (e.g., +0xxxxxxxxx)
        if not re.match(r'^(010|011|012|015)[0-9]{8}$', mobile_phone):
            print("Invalid Egyptian phone number format.")
            return

        # Save user registration data to storage (e.g., file or database)
        
        
        
        for user in User.rigestered_users:
            if email==user.email: 
              print("alredy exist user")
              return
        newuser=User(first_name,last_name,email,password,mobile_phone)
        newuser.user_add()
        print("Registration successful!")


# User login
def login_user():
    
    email = input("Enter your email address: ")
    password = getpass.getpass("Enter your password: ")
    for user in User.rigestered_users:
           if email==user.email:
               if user.password==password:
                   
                   print(f"you are successfuly loge in with =>{user.first_name}")
                   return user.first_name 

               else:
                   print("wrong user passowrd")
                   return

    print("no user with that email")   
    return ""
             
              
               
            
    
    # Validate user credentials against stored data

    print("Login successful!")


# Project creation
def create_project(current_user):
    print(f"user name is ({current_user})")
    if current_user=="":
        print("please log in first")

        return
    
    title = input("Enter the project title: ")
    details = input("Enter project details: ")
    total_target = float(input("Enter the total target amount: "))
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")

    # Validate date format and logic
    try:
       

      
      

        # Convert the user input to datetime objects.
       start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
       end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

        # Subtract the two datetime objects and print the difference in days.
       difference = start_date-end_date
       print(f"The difference between the two dates is {difference} ")

       if end_date <= start_date:
            print("End date should be later than the start date.")
            return
    except ValueError:
        print("Invalid date format.")
        return
    
    # Save project data to storage
    

    for project in Project.projects:
           if project.title==title:
               print(" sorry this project is alredy exist")
               return
    new_Project=Project(title,details,total_target,start_date_str,end_date_str,current_user)           
    new_Project.project_add()
    print("Project created successfully!")

#load users from file 

def load():
        file= open('backup.txt','r')
        for line in file:
            line=line.split('-')
            firs_name=line[0]
            last_name=line[1]
            email=line[2]
            password=line[3]
            phone=line[4].replace("\n","")
            neweser=User(firs_name,last_name,email,password,phone)
def load_project():
        file= open('backup_project.txt','r')
        for line in file:
            line=line.split('_')
            title=line[0]
            details=line[1]
            total_target=line[2]
            start_date=line[3]
            end_date=line[4]
            user=line[5].replace("\n","")
            new_Project=Project(title,details,total_target,start_date,end_date,user)           
def printuser():
    newuser=User
    for user in newuser.rigestered_users:
      print(user.email)

def show_project(current_user):
    print(f"user name is ({current_user})")
    if current_user=="":
        print("please log in first")
    print("<<< the system projects are >>>")    
    newproject=Project
    for project in newproject.projects:
        print(f"{project.title} start in {project.start_date} end`s in {project.end_date}created by {project.owner} ")
    print("done")    

def delete_project(project_name,current_user):
    for project in Project.projects:
        if project_name == project.title:
            if current_user==project.owner:
                Project.projects.remove(project)

                Project.project_add()
                print("project deleted sucess")
                
                return main_menu
                
            print(f"only owner can re,ove the project {project_name}")
            return main_menu
    
    return main_menu
# Main menu
def main_menu():
    load_project()
    load()
    printuser()
   
    
    print("Welcome to the Fundraising Console App!")
    print("1. Register")
    print("2. Login")
    print("3. Create Project")
    print("4. Shwo project")
    print("5. delete progect")
    print("6. Exit")
  
    while True:
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            current_user=""
            current_user = login_user()
        elif choice == "3":
            try:
              create_project(current_user)
            except:
                print("log in first ><")
            
        elif choice == "4":
            try:
             show_project(current_user)
            except: 
                print("log in to view projects")
        elif choice == "5":
            
            project_name=input("enter project title to remove>> ")
            
            delete_project(project_name,current_user)    
             
            
        elif choice == "6":
            print("Goodbye!")        
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point of the application
if  __name__ == "__main__":
    main_menu()