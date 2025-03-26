# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    c1 = float(input("Enter initial concentration (g/L) : "))
    c2 = float(input("Enter final concentration (g/L) : "))
    V2 = float(input("Enter initial volume (L) : "))
    V1 = (c1*V2) / c2
   
    print(f"So, you need {V1:.2f} liters of the original slurry.")

if __name__ == "__main__":
    main()
