class BankAccount:
    exchange_rates = {"USD": 1.0, "EUR": 1.1, "IDR": 0.00007}  # Kurs tetap
    
    def __init__(self, account_holder, balance, currency="USD"):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency
    
    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        return amount * (self.exchange_rates[to_currency] / self.exchange_rates[from_currency])
    
    def __add__(self, amount):
        self.balance += amount
        return self
    
    def __sub__(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance for withdrawal!")
        return self
    
    def apply_interest(self):
        rate = 0.02 if self.balance > 5000 else 0.01
        self.balance += self.balance * rate
        print(f"Applying interest... New Balance = {self.currency} {self.balance:.2f}")
    
    def show_balance(self):
        print(f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance:.2f}")
        if self.balance < 100:
            print("Low Balance Warning!")

# Simulasi akun
john = BankAccount("John", 5000, "USD")
emily = BankAccount("Emily", 1000, "EUR")

# Proses bunga
john.show_balance()
john.apply_interest()
john.show_balance()

# Konversi dan penarikan
amount_in_usd = emily.convert_currency(1000, "EUR", "USD")
print(f"Converted to USD: ${amount_in_usd:.2f}")
if amount_in_usd > emily.balance:
    print("Insufficient balance for withdrawal!")
else:
    emily - amount_in_usd

emily.show_balance()
