class Compensation:
    def __init__(self, base, stock, bonus) -> None:
        self.base = base
        self.stock = stock
        self.bonus = bonus

    @property
    def base(self):
        return self.base
    
    @property
    def stock(self):
        return self.stock
    
    @property
    def bonus(self):
        return self.bonus

class Job:
    def __init__(self, title, company, start_date, end_date, annual_salary, bonus_structure, benefits, retirement_plan):
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.annual_salary = annual_salary
        self.bonus_structure = bonus_structure  # Could be a fixed amount, a percentage, or conditional
        self.benefits = benefits  # Such as health insurance, stock options, etc.
        self.retirement_plan = retirement_plan  # 401(k) contribution details, pension plans, etc.

        self.compensation_timeline = compensation_timeline

    def update_salary(self):
        pass
    
    # Additional methods to calculate annual income, potential bonuses, etc.
    def calculate_annual_income(self):
        pass

    def calculate_bonuses(self):
        pass

class Business:
    def __init__(self) -> None:
        pass