hour = int(input())
minutes = int(input())
seconds = 0
minutes = minutes + 15
if minutes >= 60:
    hour += 1
if minutes > 59:
    minutes = minutes % 60

if hour == 24:
    hour = 0

print(f"{hour}:{(minutes):02d}")


# hour = int(input())
# minutes = int(input())
#
# minutes = minutes + 15
# if minutes >= 60:
#     hour = hour + 1
#     minutes = minutes - 60
# if hour > 23:
#     hour = 0
#
#
# print(f"{hour}:{minutes:0>2}")
