"""
PURPOSE: Asks the user for the initial balance or principal,
the interest rate, number of years, and how frequently compounded
(supports the words "daily" for 365, "weekly" for 52,
"monthly" for 12, "quarterly" for 4, and "annually" for 1).

It then displays the total accrued amount.

AUTHOR: Amber Morgan
"""


def get_number_of_compounds(frequency):
    """
    This function takes one of the strings "daily", "weekly", "monthly",
    "quarterly", or "annually" as a parameter and returns the number of times
    per year it represents (365, 52, 12, 4, and 1 respectively).
    """
    compound_type = {"daily": 365, "weekly": 52, "monthly": 12, "quarterly": 4, "annually": 1}
    num_compounds = int(compound_type[frequency])
    return num_compounds


def compound_interest(principal, rate, years, num_compounds):
    """
    Computes the compound interest on an account that starts with 'principal'
    amount of money, the given interest 'rate', over the number of 'years',
    and compounding the given number of times. Returns the computed accrued amount.
    """
    rate_over_time = (rate / 100) / num_compounds
    total_compounds = num_compounds * years
    accrued = principal * ((1 + rate_over_time) ** total_compounds)
    return accrued


def main():
    principal = float(input("Principal: $"))
    interest_rate = float(input("Interest Rate: "))
    years = float(input("Number of Years: "))
    frequency = input("Frequency of Compounds (daily, weekly, monthly, quarterly, or annually): ")
    num_compounds = get_number_of_compounds(frequency)
    accrued = compound_interest(principal, interest_rate, years, num_compounds)
    print("You will have accrued ${:.2f}".format(accrued))


if __name__ == "__main__":
    main()
