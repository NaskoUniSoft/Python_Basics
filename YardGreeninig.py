m2_yard = float(input())

final_price = m2_yard * 7.61
discount = 18 * final_price / 100

print(f"The final price is: {final_price - discount} lv.")
print(f"The discount is: {discount} lv.")