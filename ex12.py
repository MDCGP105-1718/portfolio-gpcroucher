def hotel_cost(nights):
    return nights * 70

def plane_ticket_cost(city, classmultiplier):
    if city == "New York":
        return 2000 * classmultiplier
    elif city == "Auckland":
        return 790 * classmultiplier
    elif city == "Venice":
        return 154 * classmultiplier
    elif city == "Glasgow":
        return 65 * classmultiplier

def rental_car_cost(days):
    if days > 7:
        return 30 * days - 50
    elif days > 3:
        return 30 * days - 30
    else:
        return 30 * days

def total_cost(city, days):
    return hotel_cost(days - 1) + plane_ticket_cost(city, 1) + rental_car_cost(days)
