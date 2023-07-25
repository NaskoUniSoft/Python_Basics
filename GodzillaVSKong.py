movie_budget = float(input())
number_people = int(input())
costume_price_per_person = float(input())

movie_decor = movie_budget * 10/100
total_costume_price = costume_price_per_person * number_people
if number_people > 150:
    total_costume_price = total_costume_price - total_costume_price * 10/100

total_sum_for_movie = movie_decor + total_costume_price

if total_sum_for_movie > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_sum_for_movie - movie_budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {movie_budget - total_sum_for_movie:.2f} leva left.")