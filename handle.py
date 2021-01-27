def checkYear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Yes, {} is a leap year".format(year))
        return
    else:
      print("Yes, {} is a leap year".format(year))
      return
  print("No, {} is not a leap year".format(year))

year = input("Enter year: ") 
while(year.isdigit() == 0):
  year = input("Invalid number, Enter year: ")
year = int(year)
checkYear(year)