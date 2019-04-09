def addition(x, y):
    return x+y


def divided_by_2(x):
    return x/2


def multiple(x, y):
    return x*y


def get_area_trapezium(x, y, h):
    return divided_by_2(multiple(addition(x, y), h))


x = int(input('x?'))
y = int(input('y?'))
h = int(input('h?'))
print(get_area_trapezium(x, y, h))
