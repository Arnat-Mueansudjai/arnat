"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Arnat",20, "Chonburi", "Thai")  # name, age, city, country
    hobbies = []
    while True : 
        choice = input("Choose option:\n1. Check data\n2. Add hobbies \n3. Remove hobbies \n4. Update age \n5. Exit ")
        # Your code here
        if choice== "1":  
            print("Name: ",person[0])
            print("Age: ",person[1])
            print("City: ",person[2])
            print("Country: ",person[3])
            print("Hobbies: ",hobbies)
        
        elif choice== "2":
            hobby = input("What is your hobbies?: ")
            hobbies.append(hobby)
        
        elif choice== "3" :
            hobbies.pop()
        
        elif  choice== "4" :
            person_list =list(person)
            age = input("How old are you?: ")
            person_list[1] = age
            person=tuple(person_list)
        
        elif  choice== "5" :
            print("Thank you for using.")
            break
        
        else :
            print("This not choice please chose 1-5!!! ")


if __name__ == "__main__":
    personal_info_manager()