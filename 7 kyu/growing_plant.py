# Task Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters
# due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We
# want to know when the height of the plant will reach a certain level.
#
# Example
# For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.

# MY SOLUTION

def growing_plant(up_speed, down_speed, desired_height):
    days = 0
    height = 0
    while height < desired_height:
        days += 1
        height += up_speed
        if height < desired_height:
            height -= down_speed
        else:
            break
    else:
        days += 1
    return days


# DEMONSTRATION

print(growing_plant(100, 10, 910))
print(growing_plant(10, 9, 4))
print(growing_plant(5, 2, 6))
print(growing_plant(5, 2, 0))
