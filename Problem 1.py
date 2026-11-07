
def main():
    P0 = float(input("Enter the amount to finance: $"))
    r = float(input("Enter the annual interest rate (e.g., 0.02 for 2%): "))
    k = int(input("Enter the number of compounding periods per year: "))
    N = int(input("Enter the number of years: "))

    filename = input("Enter the output file name: ")

    rate = r / k
    periods = N * k

    if rate == 0:
        payment = P0 / periods
    else:
        payment = P0 * rate / (1 - (1 + rate) ** (-periods))

    with open(filename, "w") as file:
        file.write("\nAMORTIZATION SCHEDULE\n")
        file.write("-" * 83 + "\n")
        file.write(f"Loan Amount: ${P0:,.2f}\n")
        file.write(f"Annual Interest Rate: {r:.2%}\n")
        file.write(f"Payment per Period: ${payment:,.2f}\n")
        file.write(f"Loan Term: {N} years\n")
        file.write("-" * 83 + "\n")

        file.write(f"{'Payment #':>10} {'Payment':>13} {'Interest':>13} "
                   f"{'Principal':>13} {'Balance':>15}\n")
        file.write("-" * 83 + "\n")

        balance = P0

        for period in range(1, periods + 1):
            interest = balance * rate
            principal = payment - interest
            balance -= principal

            if period == periods or abs(balance) < 0.005:
                balance = 0.0

            file.write(f"{period:>10} "
                       f"${payment:>12,.2f} "
                       f"${interest:>12,.2f} "
                       f"${principal:>12,.2f} "
                       f"${balance:>14,.2f}\n")

        file.write("-" * 83 + "\n")

    print(f"Amortization report saved to {filename}")


if __name__ == "__main__":
    main()
