def is_friday(day):
    return day.lower() == "tuesday"


day_of_week = input("what day is it? ")
if is_friday(day_of_week):
    print("correct")
else:
    print("incorrect")
