class BankAccount:
    
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder
        
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        
        self._balance = initial_deposit
        self._transactions = []
        
    @property
    def balance(self):
        return self._balance
            
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
            
        self._balance = new_balance
            
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
            
        self._balance += amount
        self._transactions.append(f"Deposited: {amount}")
            
        return self._balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
            
        if self._balance < amount:
            raise ValueError("Insufficient funds.")
            
        self._balance -= amount
        self._transactions.append(f"Withdrew: {amount}")
            
        return amount
        
    def get_transaction_history(self):
        return self._transactions.copy()
        

class ATM:
    
    def __init__(self, bank_account):
        if not isinstance(bank_account, BankAccount):
            raise TypeError("ATM requires a BankAccount.")
        
        self._account = bank_account
        
        # Double underscore for name mangling
        self.__pin = "1234"
        
        self._is_authenticated = False
        
    def authenticate(self, entered_pin):
        if entered_pin == self.__pin:
            self._is_authenticated = True
            return True
        
        return False
    
    def check_balance(self):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        
        return self._account.balance
    
    def perform_deposit(self, amount):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
      
        try:
            new_balance = self._account.deposit(amount)
            print(f"Deposit successful. New balance: {new_balance}")
        except ValueError as error:
            print(f"Deposit failed: {error}")
        
            
    def perform_withdrawal(self, amount):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        
        try:
            withdrawn_amount = self._account.withdraw(amount)
            print(f"Withdrawal successful. Amount withdrawn: {withdrawn_amount}")
        except ValueError as error:
            print(f"Withdrawal failed: {error}")
            
    def print_mini_statement(self):
        if not self._is_authenticated:
            raise PermissionError("Authentication required.")
        
        transactions = self._account.get_transaction_history()
        
        print("\n--- Mini Statement ---")

        for transaction in transactions[-3:]:
            print(transaction)

        print("----------------------")


if __name__ == "__main__":
    
    print("== Bank Account Test ==")
    
    account = BankAccount("John Doe", 5000.0)
    
    print(f"Account Holder: {account.account_holder}")
    print(f"Initial Balance: {account.balance}")
    
    # Test valid balance modification
    account.balance = 6000.0
    print(f"Updated Balance: {account.balance}")
    
    # Test invalid balance modification
    try:
        account.balance = -100.0
    except ValueError as e:
        print("Invalid balance:", e)
        
    # Create ATM
    atm = ATM(account)
    
    # Test direct access to private PIN
    try:
        print(atm.__pin)
    except AttributeError:
        print("Direct access to atm.__pin failed because of name mangling.")
    
    print("Authenticating with correct PIN...")
    
    if atm.authenticate("1234"):
        print("Authentication successful.")
        
        print(f"Current Balance: {atm.check_balance()}")
        
        atm.perform_deposit(1000.0)
        
        atm.perform_withdrawal(500.0)
        
        print("Final Balance:", atm.check_balance())
        
        atm.print_mini_statement()
        
    else:
        print("Authentication failed.")