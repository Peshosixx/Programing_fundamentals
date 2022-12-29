balls = int(input())
highest_value = 0
correct_weight = 0
correct_time = 0
correct_quality = 0
for i in range(balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (weight / time) ** quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        correct_weight = weight
        correct_time = time
        correct_quality = quality
print(f"{correct_weight} : {correct_time} = {highest_value:.0f} ({correct_quality})")

