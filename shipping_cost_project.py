# Build a program that will take the weight of ta package and determine the cheapest way to ship that package. Whether it be Ground Shipping, Premium Ground or (NEW) drone!

def shipping(weight):

    # weight = 4.8
    ground_shipping_flat_charge = 20.00
    premium_ground_shipping = round(125.00, 2)
    drone_flat_shipping_cost = 0

    # Cost for Ground Shipping
    if weight > 10:
        price = 4.75
    elif weight > 6 and weight <= 10:
        price = 4.00
    elif weight > 2 and weight <= 6:
        price = 3.00
    elif weight <= 2:
        price = 1.50

    total_ground_shipping_cost = round(
        price * weight + ground_shipping_flat_charge, 2)
    print(f"The cost for ground shipping is: {total_ground_shipping_cost}")

    # Cost for Premium Ground
    print(
        f"The cost for premium ground shipping is: {premium_ground_shipping}")

    # Cost for Drone Shipping

    if weight > 10:
        price = 14.25
    elif weight > 6 and weight <= 10:
        price = 12.00
    elif weight > 2 and weight <= 6:
        price = 9.00
    elif weight <= 2:
        price = 4.50

    total_drone_shipping = round(weight * price + drone_flat_shipping_cost, 2)

    print(f"The cost of drone shipping is: {total_drone_shipping}")


shipping(4.8)
