day = int(input("Day:"))
month = str(input("Month:"))

if  (month == ("march") and day >= 20) or month == ("april"or  "may") or (month =="june" and day <21):
  print("Seasons:Spring")
elif (month == ("june") and day>=21) or  month == ("july"or "august" ) or (month =="september" and day<22) :
  print("Seasons:Summer")
elif (month == ( "september")and day >= 22) or month == ("october"or "november") or (month == "december" and day <21):
  print("Seasons:Fall")
elif (month == ( "december")and day >= 21) or month == ("january"or "february") or (month == "march" and day<20)  :
  print("Seasons:Winter")


