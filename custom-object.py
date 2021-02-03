# Chris Moody - Module 3 - Custom Object - File 4

class Purchase(object):
    def __init__(self, amount):
            self.amount = amount
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent / 100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent / 100.0

    def calculateTotal(self, taxPercent, tipPercent): 
        return self.amount + self.calculateTax(taxPercent) + self.calculateTip(tipPercent)
    
purch = Purchase(100.0)
taxPercent = 7.5
tipPercent = 20.0

print("\n\n")
print("Tax: ", purch.calculateTax(taxPercent))
print("Tip: ", purch.calculateTip(tipPercent))
print("Total: ", purch.calculateTotal(taxPercent, tipPercent) )
print("\n\n")