# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    c1 = float(input("Enter initial concentration (g/L) : "))
    c2 = float(input("Enter final concentration (g/L) : "))
    V1 = float(input("Enter initial volume (L) : "))
    V2 = (c1*V1) / c2
   
    print(f"So, you need {V2} liters of the original slurry.")

if __name__ == "__main__":
    main()
