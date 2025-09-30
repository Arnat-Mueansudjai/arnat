"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")

name=input("Enter your name:")
age=int(input("Enter your age:"))
num=input("Enter your phone number:")

name_flag = True
for char in name:
    if char.isalpha() == False or char != " ":
        name_flag = False
        break

age_flag = True
if age < 18 or age > 65:
    age_flag = False

num_flag=True
for char in num:
    if char.isdigit() == False or len(num)!=10:
        num_flag = False

print("\nValidation Results:")
if name_flag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid(not contains only letters and spaces)")

if age_flag:
    print(f"Age: Valid({age} years old)")
else:
    print("Age: Invalid(less than 18 or more than 65)")

if num_flag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid(not10-digit number)")

print("\nFormatted Information:")
print("Name:",name.upper())

if age >= 18 and age<= 30:
    print("Age Group:Young Adult(18-30)")
else: 
    print("Age Group:not Young Adult")

print(f"Phone: +66-{num}")


    

