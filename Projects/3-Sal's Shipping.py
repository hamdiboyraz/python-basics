def ground_shipping(weight):
    if weight <= 2:
        x = 1.5
    elif 2 < weight <= 6:
        x = 3
    elif 6 < weight <= 10:
        x = 4
    else:
        x = 4.75
    cost = 20 + x * weight
    # return 20+x*weight yapmış

    return cost
    # print(x)
    # print(cost)
    # return x 2. return neden çalışmıyor ?


print(ground_shipping(8.4))

premium_ground_shipping = 125


def drone_shipping(weight):
    if weight <= 2:
        x = 1.5 * 3
    elif 2 < weight <= 6:
        x = 3 * 3
    elif 6 < weight <= 10:
        x = 4 * 3
    else:
        x = 4.75 * 3
    cost = x * weight

    return cost


print(drone_shipping(1.5))

def cheapest_method(weight):
    if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
        cost = ground_shipping(weight)
        method = "ground shipping"
    elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
        cost = drone_shipping(weight)
        method = "drone shipping"
    else:
        cost = premium_ground_shipping
        method = "premium ground shipping"

    print("The cheapest option available is $%.2f with %s." % (cost, method))
    #bunu aşağıda print(cheapest ile nasıl yapılır ??


cheapest_method(4.8)
cheapest_method(41.5)
