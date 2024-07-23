def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = round((5 / 9) * (fahrenheit - 32))
    return celsius


def main():
    for i in range(1, 31):
        print(f'{i} celsius : {celsius_to_fahrenheit(i)}')
    for i in range(1, 61):
        print(f'{i} fahrenheit : {celsius_to_fahrenheit(i)}')


if __name__ == "__main__":
    main()
