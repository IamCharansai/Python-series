exchange_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.93, 'JPY': 156.3},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'JPY': 1.88},
    'EUR': {'USD': 1.07, 'INR': 89.5, 'JPY': 167.9}
}

def convert_currency(amount, from_currency, to_currency):
    try:
        rate = exchange_rates[from_currency][to_currency]
        converted = amount * rate
        print(f" {amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except KeyError:
        print(" Conversion not supported.")

print("💱 Currency Converter")
from_currency = input("From (USD/INR/EUR): ").upper()
to_currency = input("To (USD/INR/EUR): ").upper()

try:
    amount = float(input("Amount: "))
    convert_currency(amount, from_currency, to_currency)
except ValueError:
    print(" Please enter a valid number.")
