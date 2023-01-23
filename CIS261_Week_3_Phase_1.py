#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def GetHoursWorked():
    Tothours = float(intput("Enter Working Hours: "))
    return TotHours 
#write the GetHourlyRate function
def GetHourlyRate():
    GetHourlyRate = float(input("Enter hourly rate: "))
    return hourlyrate
# write the GetTaxRate function
def GetTaxRate():
    GetTaxRate = float(input("Enter tax rate: "))
    return taxrate



def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    # taxrate needs to be formatted as percentage
    print("hourly rate: " , f"{hourly rate, .1.5f")
    print("Total gross pay: Rs.{pay:.2f} ")
    print("tax rate: " , f"tax rate")
    print(f"Total tax applicable at \
                    ₹{total_income} is ₹{tax}")
    print("net pay: ", f"net pay")
 
    def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total Gross pay: {Totgrosspay}")
    print(f"Total tax pay: {Tottax}")
    print(f"Total net pay: {Totnetpay}")
if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        Gethoursworked = Gethoursworked()
        if (Gethoursworked.upper() =="END"):
            break
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        Gethourlyrate = Gethourlyrate()
        if (Gethourlyrate.upper() =="END"):
            break 
        # write the code to assign to taxrate the return value from GetTaxRate 
        GetTaxRate = GetTaxRate()
        if (GetTaxRate.upper() == "END"):
            break
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        # write the code to increment the other total variables with the appropriate values
        TotGrossPay += 1
        TotTax += 1
        TotNetPay +=1
        


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)




