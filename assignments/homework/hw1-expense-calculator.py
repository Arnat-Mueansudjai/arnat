"""
Personal Finance Calculator
Student: Arnat Mueansudjai
Date: 7/21/2025
Purpose: Calculate monthly budget and savings
"""
income = float(input("User's monthly income in THB: ")) #รับรายได้
rent = float(input("Monthly rent: ")) #รับค่าเช่า
food = int(input("Monthly food budget in THB: ")) #รับค่าอาหาร
transportation = float(input("Monthly transportation expenses: ")) #รับค่าเดินทาง
entertainment = int(input("Monthly entertainment budget: ")) #รับค่าพักผ่อน
emergency = float(input("Percentage to save for emergency percent: ")) #รับค่า %เงินฉุกเฉิน
investment = float(input("Percentage to invest percent: ")) #รับค่า %เงินลงทุน

TotalFixed  = rent + transportation # ค่าใช้จ่ายคงที่(ค่าเช่า+ค่าเดินทาง)
TotalVariable = food + entertainment # ค่าใช้จ่ายไม่คงที่(ค่าอาหาร+ค่าพักผ่อน)
Totalexpenses = TotalFixed  + TotalVariable # ค่าใช้จ่ายร่วม(ค่าใช้จ่ายคงที่+ค่าใช้จ่ายไม่คงที่)
Remaining_Income = income - Totalexpenses # เงินเหลือ(รายได้-ค่าใข้จ่ายร่วม)
Emergency_Fund_Amount = income*(emergency/100) # เงินฉุกเฉิน (รายได้ X % เงินฉุกเฉิน)
Investment_Amount = income*(investment/100) #เงินลงทุน (รายได้ X %เงินลงทุน)
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - investment #เงินออม (เงินเหลือ-เงินฉุกเฉินขเงินลงทุน)
Expense_Ratio = (Totalexpenses/income)*100 # ค่าใช้จ่ายต่อรายได้% ((ค่าใช้จ่าย / รายได้)X100)

print("|=====MONTHLY BUDGET REPORT=====|")
print(f"Income:{income:.2f}THB") # f  หลัง print เพื่อใช้ float
print(f"Fixed Expenses:{TotalFixed:.2f}THB")
print(f"Variable Expenses:{TotalVariable:.2f}THB")
print(f"Total Expenses:{Totalexpenses:.2f}THB")
print(f"Remaining:{Remaining_Income:.2f}THB")

print("|=====SAVINGS BREAKDOWNT=====|")
print(f"Emergency Fund({emergency}%):{Emergency_Fund_Amount:.2f}THB") 
print(f"Investment({investment}%):{Investment_Amount:.2f}THB")
print(f"Available for Savings:{Available_for_Savings:.2f}THB")

print("|=====SAVINGS BREAKDOWNT=====|")
print(f"Expense Ratio:{Expense_Ratio:.2f}%")
