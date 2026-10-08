def is_friday(day):
    return day.lower() == "saturday"


day_of_week = input("what day is the best? ")
if is_friday(day_of_week):
    print("correct")
else:
    print("incorrect")
