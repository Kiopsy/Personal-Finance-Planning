class City:
    def __init__(self, name, state_tax_rate, local_tax_rate, cost_of_living, average_rent, sales_tax_rate):
        self.name = name

        # Taxes
        self.state_tax_rate = state_tax_rate
        self.local_tax_rate = local_tax_rate
        self.sales_tax_rate = sales_tax_rate

        # Cost of living
        self.cost_of_living = cost_of_living
        self.grocery_cost = grocery_cost
        self.average_rent = average_rent

    def estimate_taxes(self):
        pass

    def calculate_total_tax_rate(self):
        return self.state_tax_rate + self.local_tax_rate

    def calculate_annual_cost_of_living(self, annual_income):
        return annual_income * self.cost_of_living

    # Additional methods for specific calculations related to the city can be added here
