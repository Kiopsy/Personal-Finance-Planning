from config import *

class Simulation:
    def __init__(self, current_age, current_year, savings, retirement, income_timeline, living_timeline, stopping_age=ENDING_AGE) -> None:
        # Current details
        self.current_age = current_age
        self.current_year = current_year
        self.stopping_age = stopping_age
        self.current_city = None
        self.current_job = None
        self.living_property = None

        # Expenses / income
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.annual_income = 0
        self.annual_expenses = 0

        # Investments
        self.savings = 0
        self.emergency_fund = 0
        self.retirement_savings = 0
        self.properties = []

        # Life events & timelines
        self.job_timeline = job_timeline
        self.property_timeline = property_timeline

        # TODO: add more events like marraige, kids, vacation, etc...
        # buying a car for example
        # getting married
        # Having to pay monthly for my parent's and their retirement

        # maybe break this down by city also with different bonuses


    def update_life(self):
        # Updates based on timelines
        self.current_job = self.job_timeline.get_current(self.current_year).pop()

        self.properties = self.property_timeline.get_current(self.current_year)
        self.living_property = next((prop for prop in self.properties if prop.is_living), None)
        if self.living_property == None:
            raise ValueError("Not living in any properties.")
        self.current_city = self.living_property.city
        
        # updates portfolios, morgagaes, everything based on how your life has updated
        # TODO

    def calculate_income(self):
        self.monthly_income = 0

        # Job income

        # Property income
        for prop in self.properties:
            self.monthly_income += prop.get_monthly_income()

        # Investment income
        # TODO

        self.annual_income = self.monthly_income * 12

    def calculate_expenses(self):
        self.monthly_expenses = 0
        # Living expenses


    
        # Property expenses
        for prop in self.properties:
            self.monthly_expenses += prop.get_monthly_expense()

        self.annual_expenses = self.monthly_expenses * 12

    def estimate_taxes(self):
        # retrive from city(s)
        pass

    """
    Asset - Home Equity: The part of the house that you "own" is your equity in
    the home. This is considered an asset. Home equity is calculated as the current
    market value of the house minus the outstanding mortgage balance. For example,
    if your house is worth $300,000 and you owe $200,000 on your mortgage, your
    equity in the house is $100,000.

    Liability - Mortgage: The remaining balance on your mortgage is a liability.
    Continuing the above example, the $200,000 you still owe on the mortgage is
    a liability.
    """
    def calculate_assets(self):
        pass

    def calculate_liabilities(self):
        pass

    def run_year(self):
        while self.current_age < ENDING_AGE:
            self.update_life()

            # get all your incomes
            self.calculate_expenses()
            self.calculate_income() # post tax

            # do youre math on how much you are making, how much you are spending
            monthly_leftover = 0
            annual_leftover = monthly_leftover * 12

            # invest what you can
            # investing simulations
            # see how you can maximize this

            self.print_statistics()

            self.current_age += 1
            self.current_year += 1

    def print_statistics(self):
        # maybe have some print options to print every major year (25, 30, 35, 40, etc...)
        pass
        
"""
- want to do a what if report?
    - calculate things in reverse
"""