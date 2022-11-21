class Property():
    def __init__(self,name):
        self.name = name
        self.total_income = []
        self.total_expenses = []
        self.total_cashflow =[]
        self.annual_cashflow= []
        self.total_investment= []


    def income(self):
        while True: # user wont be able to bypass the code by entering a mistake 
            try:
                income_amount1= float(input('What are you expecting monthly for rent? ')) 
                income_amount2= float(input('What are you expecting monthly for laundry usage? '))  
                income_amount3= float(input('What are you expecting monthly for storage usage? '))
                income_amount4= float(input('Enter addtional monthly add-on? '))
            except ValueError:
                continue
            else:
                break 
        self.total_income.append(income_amount1 + income_amount2 + income_amount3 + income_amount4)
      
        print(f'Your total income: ${self.total_income}')


    def expense(self):
        while True:
            try:
                expense_amount1= float(input('Enter your expected monthly Property Tax? '))
                expense_amount2= float(input('Enter your expected monthly for Insurance on property? '))
                expense_amount3= float(input('Enter monthly amount for Utilities your will to pay if any? '))
                expense_amount4= float(input('Money towards vacancy if any? '))
                expense_amount5= float(input('Money towards CAPEX(For Example: repairs, updates or improvements on property) if any ? '))
                expense_amount6= float(input('Money towards Property Management if any? '))
                expense_amount7= float(input('What is this Property Mortgage monthly? '))
            except ValueError:
                continue
            else:
                break 
        self.total_expenses.append(expense_amount1 + expense_amount2 + expense_amount3 + expense_amount4 + expense_amount5 + expense_amount6 + expense_amount7)
        print(f'Your total Expenses: ${self.total_expenses}')

    def cashflow(self):
        self.total_cashflow = list(map(lambda x,y: x-y, self.total_income, self.total_expenses))
        print(f'Your monthly Cash Flow : ${self.total_cashflow}')
        self.annual_cashflow = list(map(lambda x: x * 12, self.total_cashflow))
        print(f'Your Annual Cash Flow: ${self.annual_cashflow} ')

    def roi(self):
        while True:
            try:
                invest_amount1= float(input('How much was your down payment? '))
                invest_amount2= float(input('What is your closing cost? '))
                invest_amount3= float(input('What is your Rehab Budget? '))
            except ValueError:
                continue
            else:
                break
        self.total_investment.append(invest_amount1 + invest_amount2 + invest_amount3)
        print(f'Total Investment: {self.total_investment}')

        roi= list(map(lambda x,y: (x / y) * 100,self.annual_cashflow, self.total_investment))
        print(f'Your Cash on Cash Return On Investment: {roi}%')

    def runner(self):
        while True:
            user_choice= input('Do you want to check Return on Investment(yes/no)? ').lower()
            if user_choice == "yes":
                self.income()
                self.expense()
                self.cashflow()
                self.roi()
            elif user_choice == 'no':
                print('Thanks for using our Investment calculator.')
                break
            else:
                print('Invalid Option')



condo = Property('Kevons inn')
# condo.income()
# condo.expense()
# condo.cashflow()
# condo.roi()
condo.runner()











