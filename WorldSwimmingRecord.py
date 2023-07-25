record_in_second = float(input())
distance_in_m = float(input())
times_per_m = float(input())

water_resist_distance = distance_in_m // 15
delay_by_water_resist = water_resist_distance * 12.5

time_without_delay = distance_in_m * times_per_m

final_time = time_without_delay + delay_by_water_resist

if record_in_second <= final_time:
    print(f"No, he failed! He was {final_time - record_in_second:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")