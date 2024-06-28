class GardenCenter:
    def __init__(self):
        self.inventory = []
        self.open = True
        self.hours = {"start": 8, "end": 18}
        self.maintenance_services = True

    def shutdown(self):
        """close the garden center"""
        self.open = False

    def openup(self):
        """open the garden center"""
        self.open = True

    def accept_delivery(self, plant):
        self.inventory.append(plant)

    def sell_product(self, product):
        self.inventory.remove(product)
