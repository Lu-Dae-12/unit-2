
answer = input("How was the service? ")
values = [answer]

def tip(bill, tip, service_quality):
    service_quality = answer
    answer == ("great", "good", "okay", "bad")
    
    if service_quality == "great":
        tip_amount = 1.25
    elif service_quality == "good":
        tip_amount = 1.2
    elif service_quality == "okay":
        tip_amount = 1.15
    elif service_quality == "bad":
        tip_amount = 1.0
    else:
        print('error')
        return None

    return bill * tip_amount

bill = float(input("What was the bill? "))
total = tip(bill, None, answer)
print(total)