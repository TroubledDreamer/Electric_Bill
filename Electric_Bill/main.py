

previousMonth = 0.0
presentMonth = 0.0

check1 = 0
standingCharge = 13.00

print("Welcome to Carlyon Electric bill Calculator\n")

while True:
  try:
      # input a num past and present
      previousMonth = int(input("Enter the reading of the meter for the past reading: "))
      presentMonthR = int(input("Enter the reading of the meter for the Present reading: "))
      #checker

      if (presentMonthR >= previousMonth) and (previousMonth >= 0):
          check = int("1")
      else:
          check = int("t")

      break

  except ValueError:
      print("\nInvalid Inputted: \n1)Reading/s is less than 0 \n2)A non number was entered \n3)or the present reading is less than the past reading\n")
      continue

print("\nPrevious meter reading entered:", previousMonth)
print("Present meter reading entered:", presentMonthR)

presentMonth =  presentMonthR - previousMonth

#caculaton
units2 = presentMonth

if(units2 < 50):
    amount2 = units2 * 0.59

elif(units2 == 50):
    amount2 = 29.50

elif (units2>50 and units2<150):
    amount2 =29.50 + ((units2 - 50) * 0.65)

elif(units2 >= 150):
    amount2 = 94.50 + ((units2 - 150) * 0.68)


print("\nStanding charge: $" , standingCharge)
print("\ntotal bill = $" , amount2 , " + " , standingCharge)
thisMonth = amount2 + standingCharge



print("\nAmount of kwh used in the first meter reading " , previousMonth)
print("\nAmount of kwh used in the second meter reading " , presentMonthR)
print("\nAmount of kwh used" , presentMonth)
print("\nElectricity Bill $"  ,  "{:.2f}".format(thisMonth))
