class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):
    s = self.category.center(30, '*') + "\n"
    for item in self.ledger:
      a = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      s += a + "\n"
    s += 'Total: ' + str(self.get_balance())
    return s

  def deposit(self, amount, description=''):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)

  def withdraw(self, amount, description=''):
    temp = {}
    if self.check_funds(amount):
      temp['amount'] = -amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return (balance)

  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  total = sum(spend)
  percentage = [i / total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    s += " "
  s += "\n" + "    "

  for i in percentage:
    s += "-" * 3
  s += "-"

  cat_lenght = []
  for category in categories:
    cat_lenght.append(len(category.category))
  max_lenght = max(cat_lenght)

  for k in range(max_lenght):
    s += "\n    "
    for c in range(len(categories)):
      if k < cat_lenght[c]:
        s += " " + categories[c].category[k] + " "
      else:
        s += "   "
    s += " "

  return s
