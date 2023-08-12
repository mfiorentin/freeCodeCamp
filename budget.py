# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-budget-app#budget.py

class Category:
  
    def __init__(self, name):
        self.cat_name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": -1*amount, "description": description})
            return True

    def get_balance(self):
        funds = 0
        for transaction in self.ledger:
            funds += transaction["amount"]
        return funds

    def transfer(self, amount, budget_cat):
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, "Transfer to " + budget_cat.cat_name)
            budget_cat.deposit(amount, "Transfer from " + self.cat_name)
            return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def total_withdraw(self):
        total = 0
        for i in self.ledger:
            if i["amount"] < 0:
                total += + i["amount"]
        return "{:.2f}".format(total)

    def __repr__(self):
        result = ""
        ast_length = (30 - len(self.cat_name))/2
        result = int(ast_length) * "*" + str(self.cat_name) + int(ast_length) * "*" + "\n"

        for i in self.ledger:
            description_length = len(str(i["description"]))
            amount = "{:.2f}".format(i["amount"])
            amount_length = len(str(amount))
            if description_length > 23:
                description_length = 23
            else:
                description_length = description_length
            result += i["description"][0:23] + (30-description_length-amount_length)*" " + str(amount) + "\n"

        result += "Total: " + str("{:.2f}".format(self.get_balance()))

        return result


def create_spend_chart(cat_list):
    result = "Percentage spent by category" + "\n"
    total = 0
    perc_list = []
    for i in cat_list:
        total += float(i.total_withdraw())

    for i in cat_list:
        percentage = "{:.2f}".format((float(i.total_withdraw())/total)*100)
        perc_list.append(percentage)

    for x in range(100, -10, -10):
        result += (str(x) + "| ").rjust(5)
        for i in perc_list:
            if x > float(i):
                result += "   "
            else:
                result += "o" + "  "
        result += "\n"

    result += "    " + "-" * ((len(cat_list)-1) + len(cat_list) + 5) + "\n"

    max_length = 0
    for i in cat_list:
        cat_length = len(i.cat_name)
        if cat_length > max_length:
            max_length = cat_length

    for i in range(max_length):
        result += "     "
        for x in cat_list:
            if i < len(x.cat_name):
                result += x.cat_name[i] + "  "
            else:
                result += "   "
        result += "\n"

    result = result.rstrip()
    result += "  "
    return result
