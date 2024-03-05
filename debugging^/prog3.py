"""
Computes compound interest using the compound interest formula.

AUTHOR: Amber Morgan
"""


def main():
    principal = float(input("Principal: $"))
    interest_rate = float(input("Interest Rate (APY): "))
    compounds_per_year = int(input("Compounds per year (e.g. 12 if monthly): "))
    years = int(input("Number of years collecting interest: "))
    compounding_rate = (interest_rate / 100) / compounds_per_year
    future_balance = principal * (1 + compounding_rate) ** (compounds_per_year * years)
    print("You will have ${:.2f}".format(future_balance))


if __name__ == "__main__":
    main()
