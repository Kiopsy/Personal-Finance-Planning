import numpy_financial as npf
import config

class Simulation:
    def __init__(self, config):
        self.current_age = config.CURRENT_AGE
        self.retirement_age = config.RETIREMENT_AGE
        self.income_array = config.INCOME_ARRAY
        self.home_price = config.HOME_PRICE
        self.down_payment_percentage = config.DOWN_PAYMENT_PERCENTAGE
        self.mortgage_rate = config.MORTGAGE_RATE
        self.mortgage_term = config.MORTGAGE_TERM
        self.rent_and_utilities = config.RENT_AND_UTILITIES
        self.child_expenses_start_age = config.CHILD_EXPENSES_START_AGE
        self.child_expenses_per_year = config.CHILD_EXPENSES_PER_YEAR
        self.children = config.CHILDREN
        self.inflation_rate = config.INFLATION_RATE
        self.investment_growth_rate = config.INVESTMENT_GROWTH_RATE
        self.savings_rate = config.SAVINGS_RATE
        self.retirement_goal = config.RETIREMENT_GOAL
        self.savings = 0
        self.retirement_savings = 0

    def estimate_taxes(self, income):
        pass

    def get_annual_income(self):
        pass

    def print_statistics(self):
        # Output the results
        print(f"Year {year}: Projected Income: ${projected_income}, Required Gross Income: ${required_gross_income}, Required Net Income: ${required_net_income}, Expenses: ${annual_expenses}")

    def print_projected_statistics(self):
        pass

    def run_year(self, year):
        projected_income = get_annual_income(INCOME_ARRAY, year - CURRENT_AGE)
        projected_taxes = 

        # Calculate the required gross income to meet expenses and savings
        # Factor in inflation and child expenses
        annual_expenses = RENT_AND_UTILITIES * (1 + INFLATION_RATE) ** (year - CURRENT_AGE)
        if year >= CHILD_EXPENSES_START_AGE:
            annual_expenses += CHILD_EXPENSES_PER_YEAR * CHILDREN * (1 + INFLATION_RATE) ** (year - CHILD_EXPENSES_START_AGE)

        # Adjust for home purchase
        if year == PURCHASE_HOME_AGE:
            mortgage_principal = HOME_PRICE - DOWN_PAYMENT
            annual_mortgage_payment = calculate_mortgage_payment(mortgage_principal, MORTGAGE_RATE, MORTGAGE_TERM) * 12
            annual_expenses = annual_mortgage_payment

        # Calculate savings goal for retirement
        annual_savings_goal = (RETIREMENT_GOAL - retirement_savings) / (RETIREMENT_AGE - year)
        
        # Calculate the required gross income
        required_gross_income = annual_expenses + annual_savings_goal
        required_net_income = calculate_net_income(required_gross_income)

        self.print_statistics()
        self.year += 1
    
    def run_simulation(self):    
        for year in range(CURRENT_AGE, RETIREMENT_AGE + 1):
            self.run_year(year) 

        self.print_projected_statistics()

def estimate_taxes(income):
    # Simplified tax calculation
    if income < 100000:
        return income * 0.25
    elif income < 200000:
        return income * 0.30
    else:
        return income * 0.35

def get_annual_income(income_array, year):
    if year < len(income_array):
        return income_array[year]
    return income_array[-1]

def calculate_net_income(gross_income):
    # Estimate taxes based on gross income
    taxes = estimate_taxes(gross_income)
    # Subtract taxes from gross income to get net income
    net_income = gross_income - taxes
    return net_income

def calculate_annual_expenses(year):
    annual_expenses = RENT_AND_UTILITIES * (1 + INFLATION_RATE) ** (year - CURRENT_AGE)
    if year >= CHILD_EXPENSES_START_AGE:
        annual_expenses += CHILD_EXPENSES_PER_YEAR * CHILDREN * (1 + INFLATION_RATE) ** (year - CHILD_EXPENSES_START_AGE)

    # Adjust for home purchase
    if year == PURCHASE_HOME_AGE:
        mortgage_principal = HOME_PRICE - DOWN_PAYMENT
        annual_mortgage_payment = calculate_mortgage_payment(mortgage_principal, MORTGAGE_RATE, MORTGAGE_TERM) * 12
        annual_expenses = annual_mortgage_payment

def update_investment_balance(balance, contribution, growth_rate):
    return balance * (1 + growth_rate) + contribution

def calculate_mortgage_payment(principal, annual_rate, term_years):
    monthly_rate = annual_rate / 12
    payments = term_years * 12
    return npf.pmt(monthly_rate, payments, -principal)

INCOME_ARRAY = [115000, 120000, 125000, 130000]  # Projected annual income
CHILD_EXPENSES_START_AGE = 30
CHILD_EXPENSES_PER_YEAR = 20000
CHILDREN_COUNT = 2
INFLATION_RATE = 0.02
INVESTMENT_GROWTH_RATE = 0.07
SAVINGS_RATE = 0.20
HOME_PRICE = 2000000
DOWN_PAYMENT_PERCENTAGE = 0.20
MORTGAGE_TERM = 30
MORTGAGE_RATE = 0.04
CURRENT_AGE = 23
PURCHASE_HOME_AGE = 30
RETIREMENT_AGE = 50
RETIREMENT_GOAL = 2000000
ANNUAL_RENT_AND_UTILITIES = 35000  # Annual rent and utilities before buying home


def run_simulation():
    # Simulation loop
    for year in range(CURRENT_AGE, RETIREMENT_AGE + 1):
        # Update income from the array
        income = get_annual_income(income_array, year - current_age)
        net_income = calculate_net_income(income)



        # Adjust expenses for inflation and children
        rent_and_utilities *= (1 + inflation_rate)
        child_expenses_per_year *= (1 + inflation_rate)
        total_expenses = rent_and_utilities
        if year >= child_expenses_start_age:
            total_expenses += child_expenses_per_year * children

        # Calculate savings and investment growth
        annual_savings = net_income * savings_rate - total_expenses
        retirement_savings = update_investment_balance(retirement_savings, annual_savings, investment_growth_rate)

        # Handle home purchase
        if year == purchase_home_age:
            mortgage_principal = home_price - down_payment
            mortgage_payment_annual = calculate_mortgage_payment(mortgage_principal, mortgage_rate, mortgage_term) * 12
            savings -= down_payment

        # Adjust expenses post-home purchase
        if year >= purchase_home_age:
            total_expenses = mortgage_payment_annual + child_expenses_per_year * children

        # Output the results
        print(f"Year {year}: Income: ${income}, Net Income: ${net_income}, Retirement Savings: ${retirement_savings}, Expenses: ${total_expenses}")


def run_simulation():
    for year in range(CURRENT_AGE, RETIREMENT_AGE + 1):
        # Update income from the income array
        projected_income = get_annual_income(INCOME_ARRAY, year - CURRENT_AGE)

        # Calculate the required gross income to meet expenses and savings
        # Factor in inflation and child expenses
        annual_expenses = RENT_AND_UTILITIES * (1 + INFLATION_RATE) ** (year - CURRENT_AGE)
        if year >= CHILD_EXPENSES_START_AGE:
            annual_expenses += CHILD_EXPENSES_PER_YEAR * CHILDREN * (1 + INFLATION_RATE) ** (year - CHILD_EXPENSES_START_AGE)

        # Adjust for home purchase
        if year == PURCHASE_HOME_AGE:
            mortgage_principal = HOME_PRICE - DOWN_PAYMENT
            annual_mortgage_payment = calculate_mortgage_payment(mortgage_principal, MORTGAGE_RATE, MORTGAGE_TERM) * 12
            annual_expenses = annual_mortgage_payment

        # Calculate savings goal for retirement
        annual_savings_goal = (RETIREMENT_GOAL - retirement_savings) / (RETIREMENT_AGE - year)
        
        # Calculate the required gross income
        required_gross_income = annual_expenses + annual_savings_goal
        required_net_income = calculate_net_income(required_gross_income)

        # Output the results
        print(f"Year {year}: Projected Income: ${projected_income}, Required Gross Income: ${required_gross_income}, Required Net Income: ${required_net_income}, Expenses: ${annual_expenses}")

run_simulation()



# New function to estimate the required final year income
def estimate_required_final_income(income_array, final_year, retirement_goal, current_savings, children, inflation_rate, investment_growth_rate, savings_rate, home_price, down_payment, mortgage_rate, mortgage_term, rent_and_utilities, child_expenses_per_year, child_expenses_start_age, purchase_home_age):
    estimated_income = income_array[-1]  # Start with the last known income
    increment = 5000  # Increment to adjust the estimated income

    while True:
        income_array[-1] = estimated_income
        retirement_savings = current_savings
        for year in range(len(income_array)):
            age = current_age + year
            net_income = calculate_net_income(income_array[year])
            total_expenses = rent_and_utilities * (1 + inflation_rate) ** year
            if age >= child_expenses_start_age:
                total_expenses += child_expenses_per_year * children * (1 + inflation_rate) ** (age - child_expenses_start_age)
            if age >= purchase_home_age:
                mortgage_principal = home_price - down_payment
                mortgage_payment_annual = calculate_mortgage_payment(mortgage_principal, mortgage_rate, mortgage_term) * 12
                total_expenses = mortgage_payment_annual

            annual_savings = net_income - total_expenses
            retirement_savings = update_investment_balance(retirement_savings, annual_savings, investment_growth_rate)

        if retirement_savings >= retirement_goal:
            break
        estimated_income += increment

    return estimated_income

# Estimate the required final year income
required_final_income = estimate_required_final_income(
    income_array, target_age, retirement_goal, savings, children, inflation_rate, investment_growth_rate, 
    savings_rate, home_price, down_payment, mortgage_rate, mortgage_term, rent_and_utilities, 
    child_expenses_per_year, child_expenses_start_age, purchase_home_age
)

print(f"Estimated required final year income to meet financial goals: ${required_final_income}")