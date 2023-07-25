budget = float(input())
videocard_qty = int(input())
processor_qty = int(input())
ram_qty = int(input())
'''
boooooooooooooooooooooom
'''
videocard_price = 250
processor_price = 35/100 * videocard_qty * videocard_price
ram_price = 10/100 * videocard_price * videocard_qty

total_price = videocard_qty * videocard_price + processor_qty * processor_price + ram_qty * ram_price

if videocard_qty > processor_qty:
    total_price = total_price - total_price * 15/100

if total_price > budget:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
else:
    print(f"You have {budget - total_price:.2f} leva left!")