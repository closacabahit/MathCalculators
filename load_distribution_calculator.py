# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    w = float(input("Enter load (m) : "))
    L = float(input("Enter length (m) : "))
    F = w * L

    print(f" So, the total load acting on the beam is {F:,.2f} N.")

if __name__ == "__main__":
    main()
