# Create a class for the shoe shop with the following parameters:
# Shoe type
# Shoe color
# Shoe total quantity in stock
# Shoe Unit Price
# Taxes
# Selling price
# Number of shoes that have been sold

# Calculate the following:
# 1. The shoe cost.
# 2. The Profit per shoe
# 3. The profit received after selling some shoes.
# 4. The profit percentage.


class ShoeShop:

    def __init__(self, shoe_type, color, total_quantity, unit_price):
        self.shoe_type = shoe_type
        self.color = color
        self.total_quantity = total_quantity
        self.unit_price = unit_price

    def shoe_cost(self, taxes):

        """This will calculate the shoe cost.

        args:
        taxes: These should be integers because their value is a percentage.
        Example: taxes = 30 which is equivalent to 30%.

        return
        Float number the shoe cost"""

        cost = (taxes/100 + 1) * self.unit_price
        return cost

    def profit(self, selling_price, taxes):

        """This will calculate the shoe profit per item.

        args:
        selling_prce: the selling price of the shoe, it can be an integer or
        a float
        taxes: These should be integers because their value is a percentage.
        Example: taxes = 30 which is equivalent to 30%.

        return
        Float number the shoe profit"""

        profit_per_item = selling_price - self.shoe_cost(taxes)
        return profit_per_item

    def profit_per_type_color(self, sold_quantity, selling_price, taxes):

        """This will calculate the shoe profit specifying the color and
            type.

        args:
        sold_quantity: an integer, the number of shoes that have been sold.
        selling_prce: the selling price of the shoe, it can be an integer or
        a float
        taxes: These should be integers because their value is a percentage.
        Example: taxes = 30 which is equivalent to 30%.

        return
        A string showing the shoe profit in US$"""

        total_profit = sold_quantity * self.profit(selling_price, taxes)
        return f"Total Profit in US$ for {self.shoe_type} shoe type \
color {self.color} = {total_profit}"

    def profit_percentage(self, selling_price, taxes):

        """This will calculate the shoe profit percentage, showing their type
        and color.

        args:
        selling_prce: the selling price of the shoe, it can be an integer or
        a float
        taxes: These should be integers because their value is a percentage.
        Example: taxes = 30 which is equivalent to 30%.

        return
        A string showing the shoe profit percentage rounded to two digits"""

        profit_per = self.profit(selling_price, taxes) / self.shoe_cost(taxes)
        return f"Profit Percentage for {self.shoe_type} shoe type \
color {self.color} = {round(profit_per * 100, 2)}%"


# Creating an instance.
heels = ShoeShop("Heels", "red", "30", 70, "Henry Smith")

shoe_cost = heels.shoe_cost(30)
# print("Shoe cost =", shoe_cost)

profit_per_item = heels.profit(100, 30)
# print(profit_per_item)

heels_red_total_profit = heels.profit_per_type_color(15, 100, 30)
# print(heels_red_total_profit)

total_profit_percent = heels.profit_percentage(100, 30)
print(total_profit_percent)
