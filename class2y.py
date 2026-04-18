class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append({"description": description, "amount": amount})

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def total_income(self):
        return sum(i["amount"] for i in self.incomes)

    def total_expense(self):
        return sum(e["amount"] for e in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"Account owner: {self.firstname} {self.lastname}"
