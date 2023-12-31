from config import *

class Simulation:
    def __init__(self, income_timeline, living_timeline) -> None:
        self.savings = 0
        self.retirement_savings = 0
        self.investment_properties = []

        self.income_timeline = income_timeline
        self.living_timeline = living_timeline

        self.current_age = CURRENT_AGE
        self.current_year = CURRENT_YEAR

        self.current_city = None # somthing

        self.current_income = 0
        self.current_living_situation = None
        # maybe break this down by city also with different bonuses
        
    def set_annual_income(self):
        # TODO: check correctness
        sorted_timeline = sorted(self.income_timeline.items(), key=lambda x: x[0], reverse=True)
        for year, income in sorted_timeline:
            if year <= self.current_year:
                self.current_income = income
                break

    def set_living_situation(self):
        # TODO: check correctness
        sorted_timeline = sorted(self.living_timeline.items(), key=lambda x: x[0], reverse=True)
        for year, living_situation in sorted_timeline:
            if year <= self.current_year:
                self.current_living_situation = living_situation
                break

    def get_annual_expenses(self):
        pass

    def estimate_taxes(self):
        # retrive from city(s)
        pass

    def run_year(self):
        while self.current_age < ENDING_AGE:
            self.set_annual_income()
            self.set_living_situation()





            monthly_leftover = 0
            annual_leftover = monthly_leftover * 12

            # invest what you can

            self.current_age += 1
            self.current_year += 1

    def print_statistics(self):
        pass
        
"""
Structure:
- different income streams
    - different rates
    - different money making strategies

- want to do a what if report?
    - calculate things in reverse
"""