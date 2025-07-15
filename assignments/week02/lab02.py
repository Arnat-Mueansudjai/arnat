
"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
print("|=======Currency_Converter=======|")
choice = int(input("Chose you converts \n1.Dollars(USD) \n2.Baht(THB)" ))
if choice == 1 :
    Usd=int(input("How much money: "))
    THB=Usd*35.5
    print("you have : ",THB,"฿")
if choice == 2 :
    THB=int(input("How much money: "))
    Usd=THB / 35.5
    print("you have : ",Usd,"$")