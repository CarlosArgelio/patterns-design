"""
challenge shopping card with singleton
"""

class Product:
    
    def __init__(self, id, name, cost) -> None:
        self._id = id
        self._name = name
        self._cost = cost
    
    def id(self):
        return self._id
    
    def name(self):
        return self._name
    
    def cost(self):
        return self._cost

    def to_dict(self) -> dict:
        # products = []
        return {
            "id": self._id,
            "name": self._name,
            "cost": self._cost
        }

    def __str__(self) -> str:
        return f"Product: {self._id}, {self._name}, {self._cost}"

class ShoppingCard:
    """
    Is a singleton class, is used to manage the shopping card.
    """
    _instance = None
    _products = []
    
    def add_product(self, product):
        self._products.append(product)
    
    def get_products(self):
        products = []
        for product in self._products:
            products.append(product.to_dict())
        return products

    def remove_product(self, id: str):
        for product in self._products:
            if product.id == id:
                self._products.remove(product)
                break
    
    
    def get_unique_products(self, id):
        product = next((p for p in self._products if p.id == id), None)
        return product
    
    @staticmethod
    def get_instance():
        if not ShoppingCard._instance:
            ShoppingCard._instance = ShoppingCard()
        return ShoppingCard._instance


def appSingleton():
    """
    Creates a new singleton instance.
    """
    singleton1 = ShoppingCard.get_instance()
    singleton2 = ShoppingCard.get_instance()

    singleton1.add_product(Product("1", "product-1", 10))
    singleton1.add_product(Product("2", "product-2", 20))
    print(singleton1.get_unique_products("1"))

appSingleton()
