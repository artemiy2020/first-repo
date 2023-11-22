length = "2.75"
width = "1.75"
# Перетворення рядкових значень на числа з плаваючою комою
length_float = float(length)
width_float = float(width)

# Розрахунок площі
area = length_float * width_float

# Оформлення результату в рядок
show = f"With width {width_float} and length {length_float} of the room, its area is equal to {area}"

# Вивід результату
print(show)