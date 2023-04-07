


previousMonth = 0.0
presentMonth = 0.0

upplyCharget = 0.91
inisupplyCharget = 11

supplyCharge = 0.91
minisupplyCharge = 11

check1 = 0


# input a num past and present
while True:
  try:
    previousMonth = int(input("Enter the reading of the meter for the previous month: "))
    presentMonthR = int(input("Enter the reading of the meter for the Present month: "))
    #checker
    previousMonth = -5
    if (presentMonth >= previousMonth) and (previousMonth >= 0):
        check = int("1")
    else:
        check = int("t")



  except ValueError:
      print("Error found in your input, please try again")
      continue

print("Previous month reading entered:", previousMonth)
print("Present month reading entered:", presentMonthR)

presentMonth = previousMonth - presentMonthR

#calculation
units1 = previousMonth

if(units1 < 50):
    amount = units1 * 0.59

elif(units1 == 50):
    amount = 29.50

elif(units1 <= 150):
    amount = 29.50 + ((units1 - 50) * 3.25)

#caculaton
units1 = presentMonth

if(units1 < 50):
    amount = units1 * 0.59

elif(units1 == 50):
    amount = 29.50

elif(units1 <= 150):
    amount = 29.50 + ((units1 - 50) * 3.25)





total = amount + 13.00


print("\nAmount of kwh used in the previous mounth" , previousMonth)
print("\nAmount of kwh used in the present mounth" , presentMonth)
print("\nTotal amount of kwh used" , presentMonthR)
print("\nElectricity Bill = %.2f"  %total)
