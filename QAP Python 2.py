# A program to help calculate employee payroll
# Author: Tanner Jones
# Date Written: Jan,13th 2023

#Gathing Information From user
EmpName = input("What is the employee's name: ")
HoursWorked = float(input("How Many Hours Was Worked: "))
Widget1 = int(input("How many Widgets produced on Monday:"))
Widget2 = int(input("How many Widgets produced on Tuesday:"))
Widget3 = int(input("How many Widgets produced on Wednsday:"))
Widget4 = int(input("How many Widgets produced on Thursday:"))
Widget5 = int(input("How many Widgets produced on Friday:"))


#Setting Constants
Hourly = 17.50
Commission = 0.35
IncomeTax = 0.21
CPP = 0.0495
EI = 0.016
Union = 15.00

#Performing Required Calculations
HourlyPay = HoursWorked * Hourly
TotalWidgets = Widget1 + Widget2 + Widget3 + Widget4 + Widget5
WidgetCommission = TotalWidgets * Commission
Grosspay = HourlyPay + WidgetCommission
IncomeTaxPay = Grosspay * IncomeTax
IncomeTaxPay = round(IncomeTaxPay,2) #Rounding to remove erroneous
CPPPay = Grosspay * CPP
CPPPay = round(CPPPay,2)
EIPay = Grosspay * EI
EIPay = round(EIPay,2)
TotalDeuct = IncomeTaxPay + CPPPay + EIPay + Union
TotalDeuct = round(TotalDeuct,2)
NetPay = Grosspay - TotalDeuct
NetPay = round(NetPay,2)

#Displaying Required Outputs
print()
print("Employee's Name:", EmpName)
print("Hours Worked:", HoursWorked)
print("Total Widgets Produced For Week:", TotalWidgets)
print()
print("-"*50) #seperating inputs, calculatioons, outputs for readability
print()
print("The Regular Pay For This Pay Period Is:", HourlyPay)
print("Commission Earned:", WidgetCommission)
print("Gross Pay Earned:", Grosspay)
print()
print("-"*50)
print()
print("Income Tax Deductions:", IncomeTaxPay)
print("CPP Deductions:", CPPPay)
print("EI Deductions:", EIPay)
print("Union Fees:", Union)
print("Total Deductions:", TotalDeuct)
print()
print("Net Pay:", NetPay)
