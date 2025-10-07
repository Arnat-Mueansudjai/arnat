"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temp_1 = [23.5,25.0,27.0,32.0,34.0,28.0,30.0]
    #for i in range (7):
    #   temp=float(input("Day ",i,":"))
    #   temp_1.append(temp)
    return temp_1
def analyze_temps(list):
    sum1=sum(list)
    avg_temp = sum1/7
    max_temp=max(list)
    min_temp=min(list)
    print(sum1,avg_temp,max_temp,min_temp)
    return avg_temp,max_temp,min_temp

def display_analysis(avg1,max1,min1):
    print("Exaple Output:\nTemperature Analysis for the Week:")
    print(f"Average: {avg1:.1f}C\nHighest: {max1:.1f} C\nLowest: {min1:.1f}C")
temp_list=get_temperatures()
result=analyze_temps(temp_list)
display_analysis(result[0],result[1],result[2])
