class Item:
    def __init__(self, name, sku, cost):
        self.name = name
        self.sku = sku
        self.cost = cost

    def __str__(self):
        return "Name: " + self.name + " - SKU: " + self.sku + " Cost: " + (str)(self.cost)