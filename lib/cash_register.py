class CashRegister:
    def __init__(self, discount=0):
        self._total = 0
        self.discount = discount
        self.cart_items = []

    def get_total(self):
        return self._total

    def set_total(self, value):
        self._total = value

    total = property(get_total, set_total)

    def add_item(self, title, price, quantity=1):
        self._total += price * quantity
        item = {"title": title, "price": price, "quantity": quantity}
        self.cart_items.append(item)

    def apply_discount(self):
        if self.discount > 0:
            self._total -= self._total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self._total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.cart_items:
            last_item = self.cart_items[-1]
            last_item_price = last_item["price"]
            last_item_quantity = last_item["quantity"]
            self._total -= last_item_price * last_item_quantity
        elif last_item_quantity > 1:
            self.cart_items[-1]["quantity"] = last_item_quantity - 1
        else:
            self.cart_items.pop()

    def get_items(self):
        items = []
        for item in self.cart_items:
          title = item["title"]
          quantity = item["quantity"]
          items.extend([title] * quantity)
        return items

    items = property(get_items)
