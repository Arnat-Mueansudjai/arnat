"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    even =[]
    odd=[]
    adove = []
    # Get 10 numbers from user
    print("Enter 5 numbers:")
    for i in range(5):
        # Your code here
        number = int(input("Enter number: "))
        numbers.append(number)

        if number %2==0 :
            even.append(number)
        else :
            odd.append(number)
    # Display original list
    print(f"Original numbers: {numbers}")
    # Your code here
    #odd_numbers = 
    # Your code here
    
    # Calculate average
    average = sum(numbers)/5.0
    # Your code here
    adove = []
    for i in range(5):
        if numbers[i]>average :
            adove.append(numbers[i])
    # Numbers greater than average
 
    
   
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")
    print("Above Average: {asove}")
    print("Sum: ",sum(numbers))
    print("Average",average)
    print("Max: ",max(numbers))
    print("Min: ",min(numbers))

    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()