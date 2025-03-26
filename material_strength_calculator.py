# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    applied_force = float(input("Enter force (N) : "))
    cross_sectional_area = float(input("Enter area (m^2) : "))
    sigma = applied_force / (cross_sectional_area)

    print(f"So, the stress on the beam is {sigma:,.2f} Pa.")

if __name__ == "__main__":
    main()
