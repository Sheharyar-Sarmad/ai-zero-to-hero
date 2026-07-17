# Offline Currency Converter - Convert to ALL currencies

rates = {
    "USD": 1, "EUR": 0.92, "PKR": 280.0, "GBP": 0.81, "INR": 83.5, "JPY": 136.0,
    "AUD": 1.57, "CAD": 1.34, "CHF": 0.91, "CNY": 7.27, "NZD": 1.68, "SGD": 1.35,
    "AED": 3.67, "SAR": 3.75, "MYR": 4.56, "THB": 34.1, "IDR": 15000, "KRW": 1330,
    "TRY": 26.5, "RUB": 91.3, "ZAR": 19.5, "BRL": 5.0, "MXN": 17.7, "EGP": 30.8,
    "NOK": 10.0, "SEK": 10.5, "DKK": 7.0, "PLN": 4.4, "ILS": 3.7, "HKD": 7.8,
    "TWD": 31.5, "VND": 24000, "PHP": 56.0, "KWD": 0.31, "QAR": 3.64, "OMR": 0.38,
    "BHD": 0.38, "CLP": 800.0, "COP": 4950.0, "NGN": 770.0, "KES": 145.0,
    "GHS": 12.0, "BDT": 111.0, "LKR": 362.0, "MMK": 2100.0,
    "NPR": 134.0, "UZS": 11000.0
}


def show_available_currencies():
    print("\nAvailable currencies:")
    for i, currency in enumerate(sorted(rates.keys()), start=1):
        print(f"{currency}", end="  ")
        if i % 10 == 0:
            print()
    print("\n")


def convert_to_all(amount, from_currency):
    if from_currency not in rates:
        return None

    results = {}

    # Convert input amount to USD first
    usd_amount = amount / rates[from_currency]

    # Convert USD to all currencies
    for currency, rate in rates.items():
        results[currency] = usd_amount * rate

    return results


def main():
    print("=== Offline Currency Converter (All Currencies) ===")

    while True:
        show_available_currencies()

        try:
            amount = float(input("Enter amount: "))
            from_currency = input(
                "Enter currency code (e.g., USD, PKR, EUR): "
            ).strip().upper()

            results = convert_to_all(amount, from_currency)

            if results is None:
                print("❌ Invalid currency code! Please try again.")
            else:
                print(f"\n💱 {amount} {from_currency} converted to all currencies:\n")
                
                for currency, value in sorted(results.items()):
                    print(f"{currency}: {value:.2f}")

            again = input("\nDo another conversion? (y/n): ").strip().lower()

            if again != "y":
                print("Thanks for using the converter!")
                break

        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()