trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_count = puzzle_count + doll_count + bear_count + minion_count + truck_count
total_price = puzzle_count * puzzle_price + doll_count * doll_price + bear_count * bear_price \
              + minion_count * minion_price + truck_count * truck_price

if total_count < 50:
    pass
else:
    total_price = total_price - total_price * 25/100

money_for_trip = total_price - total_price * 10/100

if money_for_trip >= trip_price:
    remaining_money = money_for_trip - trip_price
    print(f"Yes! {remaining_money:.2f} lv left.")

if money_for_trip < trip_price:
    needed_money = trip_price - money_for_trip
    print(f"Not enough money! {needed_money:.2f} lv needed.")