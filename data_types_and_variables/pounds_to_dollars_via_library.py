from forex_python.converter import CurrencyRates
pounds = int(input())
c = CurrencyRates()
conversion = c.convert('GBP', 'USD', pounds)
print(f'{conversion:.3f}')