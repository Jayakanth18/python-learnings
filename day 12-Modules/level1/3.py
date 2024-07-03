# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)

from random import randint

def gen_rgb():
    return f"{'rgb'}({randint(0,255)},{randint(0,255)},{randint(0,255)})"

print(gen_rgb())
print(gen_rgb())
print(gen_rgb())
print(gen_rgb())
