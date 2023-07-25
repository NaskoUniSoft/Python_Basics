from math import ceil

show_name = input()
show_duration = int(input())
break_duration  = int(input())

lunch_duration = 1/8 * break_duration
relax_duration = 1/4 * break_duration

free_time = break_duration - lunch_duration - relax_duration

if free_time >= show_duration:
    print(f"You have enough time to watch {show_name} and left with {ceil(free_time - show_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {ceil(abs(show_duration - free_time))} more minutes.")