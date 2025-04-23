def main():
    degree_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    degree_celsius = (degree_fahrenheit - 32) * 5 / 9
    print(f"{degree_fahrenheit} degrees Fahrenheit is equal to {degree_celsius:.2f} degrees Celsius.")



if __name__ == '__main__':
    main()