class BudgetTracker:
    def _init_(self):
        self.transactions = {'income': {}, 'expenses': {}}

    def add_income(self, category, amount):
        self.transactions['income'][category] = self.transactions['income'].get(category, 0) + amount

    def add_expense(self, category, amount):
        self.transactions['expenses'][category] = self.transactions['expenses'].get(category, 0) + amount

    def calculate_budget(self):
        total_income = sum(self.transactions['income'].values())
        total_expenses = sum(self.transactions['expenses'].values())
        return total_income - total_expenses

    def analyze_expenses(self):
        return self.transactions['expenses']

    def persist_data(self):
        with open('transactions.txt', 'w') as f:
            f.write(str(self.transactions))

def main():
    tracker = BudgetTracker()
    while True:
        print("1. Add income")
        print("2. Add expense")
        print("3. Calculate budget")
        print("4. Analyze expenses")
        print("5. Save and exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            tracker.add_income(category, amount)
        elif choice == 2:
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
        elif choice == 3:
            print("Remaining budget: ", tracker.calculate_budget())
        elif choice == 4:
            print("Expenses: ", tracker.analyze_expenses())
        elif choice == 5:
            tracker.persist_data()
            break

if _name_ == "_main_":
    main()