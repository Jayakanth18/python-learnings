# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

from random import randint

def list_of_rgb_colors(n):
    rgb_colors=[]
    for _ in range(n):
        value=(f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})")
        rgb_colors.append(value)
    return rgb_colors
    
print(list_of_rgb_colors(5))