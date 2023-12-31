from enum import Enum
import numpy_financial as npf

class PropertyType(Enum):
    PERSONAL = "personal"
    RENTAL = "rental"
    RENTED = "rented"
    # Add any other property types as needed

class Property:
    def __init__(self, property_type: PropertyType, purchase_price, mortgage_rate, mortgage_term, rental_income, monthly_rent, city):
        self.property_type = property_type
        self.purchase_price = purchase_price
        self.mortgage_rate = mortgage_rate
        self.mortgage_term = mortgage_term
        self.rental_income = rental_income
        self.monthly_rent = monthly_rent
        self.city = city
        self.mortgage_payment = self.calculate_mortgage_payment()

    def calculate_mortgage_payment(self):
        # Only calculate mortgage payment if it's a property you own
        if self.property_type in [PropertyType.RENTAL, PropertyType.PERSONAL] and self.mortgage_rate and self.mortgage_term:
            monthly_rate = self.mortgage_rate / 12
            payments = self.mortgage_term * 12
            return npf.pmt(monthly_rate, payments, -self.purchase_price)
        return 0

    def get_annual_expense_or_income(self):
        if self.property_type == PropertyType.RENTAL:
            return self.rental_income * 12 - self.mortgage_payment * 12
        elif self.property_type == PropertyType.PERSONAL:
            return -self.mortgage_payment * 12
        elif self.property_type == PropertyType.RENTED:
            return -self.monthly_rent * 12  # Annual cost of renting
