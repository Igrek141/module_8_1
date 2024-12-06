def add_everything_up(a, b):
    try:
        res = round((a + b), 3)
    except:
        res = (f'{a}{b}')
    return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))