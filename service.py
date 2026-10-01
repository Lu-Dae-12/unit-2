answer = input("How was the service? ")
values = [answer]

def tip(bill, tip, service_quality):
    service_quality = answer
    answer == ("great", "good", "okay", "bad")
    
    if service_quality == "great":
        total = bill * (1 + tip * 1.25)
    elif service_quality == "good":
        total = bill * (1 + tip * 1.2)
    elif service_quality == "okay":
        total = bill * (1 + tip * 1.15)
    elif service_quality == "bad":
        total = bill * (1 + tip)
    else:
        print('error')
        return None

    return total
        