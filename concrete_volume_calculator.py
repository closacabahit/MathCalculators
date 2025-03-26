# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    L = float(input("Enter length (m) : "))
    W = float(input("Enter width (m) : "))
    D = float(input("Enter depth (m) : "))
    V = L * W * D

    print(f"So, you need {V:,.2f} cubic meters of concrete.")

if __name__ == "__main__":
    main()
