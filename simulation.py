from config import *

class Simulation:
    def __init__(self, current_age, current_year, savings, retirement, income_timeline, living_timeline, stopping_age=ENDING_AGE) -> None:
        # Current details
        self.current_age = current_age
        self.current_year = current_year
        self.stopping_age = stopping_age
        self.current_city = None
        self.current_job = None

        # Investments
        self.savings = 0
        self.emergency_fund = 0
        self.retirement_savings = 0
        self.properties = []

        # Life events & timelines
        self.job_timeline = self.sort_timeline(job_timeline)
        self.property_timeline = self.sort_timeline(property_timeline)
        # TODO: add more events like marraige, kids, vacation, etc...
        # buying a car for example
        # getting married
        # Having to pay monthly for my parent's and their retirement

        # maybe break this down by city also with different bonuses

    def sort_timeline(self, timeline):
        # TODO: check correctness
        return sorted(timeline.items(), key=lambda x: x[0])

    def update_life(self):
        # Updates based on timelines
        


        # updates portfolios, morgagaes, everything based on how your life has updated
        
        pass

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

    def calculate_assets(self):
        pass

    def run_year(self):
        while self.current_age < ENDING_AGE:
            self.update_life()

            # get all your incomes
            self.get_annual_expenses()
            self.get_annual_income() # post tax

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
Structure:
- different income streams
    - different rates
    - different money making strategies

- want to do a what if report?
    - calculate things in reverse
"""