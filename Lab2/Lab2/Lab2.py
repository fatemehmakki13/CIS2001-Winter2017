from Item import Item

class BulkItem(Item):
    def __init__(self, name, sku, price_per_pound, number_of_pounds):
        super().__init__( "(Bulk) " + name, sku, price_per_pound * number_of_pounds )
        self.price_per_pound = price_per_pound
        self.number_of_pounds = number_of_pounds

class TaxableItem(Item):
    def __init__(self, item, tax_rate):
        super().__init__("(Taxable) " + item.name, item.sku, item.cost + item.cost * tax_rate)
        self.tax_rate = tax_rate
        
class PackageItem(Item):
    def __init__(self, name, sku, items):
        super().__init__(name, sku, 0)
        self.items = items
        for item in items:
            self.cost += item.cost

    def __str__(self):
        string = super().__str__()
        for item in self.items:
            string += '\n\t' + (str)(item)
        return string

cookies = Item('Chip Ahoy', '1234', 2.5)
banana = BulkItem('Bananas', '4011', .55, 4)
hot_chocolate_mix = Item('Hot Chocolate Mix', '12345678990', 2)
candy_bar = Item("Chocolate Bar", '34534', 1)
chair = Item('Chair', '123456', 100)
taxable_cookies = TaxableItem(cookies, .06)
taxable_chair = TaxableItem(chair, .06)
taxable_banana = TaxableItem(banana, .06)
gift_basket = PackageItem('Gift Basket', '123456789', [ cookies, banana ] )
chocolate_gift_basket = PackageItem('Chocolate Gift Basket', '245364', [ hot_chocolate_mix, candy_bar ] )
basket_of_baskets = PackageItem('BasketBasket', '35646', [ gift_basket, chocolate_gift_basket ] )

print(banana)
print(taxable_cookies)
print(taxable_chair)
print(taxable_banana)
print( gift_basket )
print( chocolate_gift_basket )
print ( basket_of_baskets )
