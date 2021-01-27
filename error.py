def checkYear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Yes, {} is a leap year".format(year))
        return
    else:
      print("Yes, {} is a leap year".format(year))
      return
  print("No, {} is a leap year".format(year))

year = input("Enter year: ") 
year = int(year)
checkYear(year)