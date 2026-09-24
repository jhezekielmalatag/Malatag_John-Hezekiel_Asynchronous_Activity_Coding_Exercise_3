# REFLECTION

1. What error occurred when trying to access atm.__pin directly? Why does Python behave this way?

An AttributeError occurred when I try to access atm.__pin directly. Python behaves this way because __pin uses two underscores, which causes name twisting. The Python changes the internal name to something like _ATM__pin, so it cannot normally be accessed directly using atm.__pin.

2. How did using @property allow you to change internal data structures or add validation without altering the public API for the caller?

Using @property gave me access the balance using account.balance while keeping the actual balance stored internally as _balance. I could also add validation to prevent negative balances without changing how the caller accesses the balance. This made the code easier to control while keeping the same simple interface.

3. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?

The ATM demonstrated abstraction by providing simple methods such as check_balance(), perform_deposit(), and perform_withdrawal(). The user does not need to know how the BankAccount validates transactions or stores the transaction history. The ATM hides those details and provides a simpler way to interact with the bank account.

