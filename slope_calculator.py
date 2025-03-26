# (c) 2025 Full Name
# A simple store calculator using functions.


def main():
    rise = float(input("Enter rise (m) : "))
    run = float(input("Enter run (m) : "))
    S = ( rise / run ) * 100
  
    print(f"So, the slope of the road is {S:,.2f}%.")

if __name__ == "__main__":
    main()
