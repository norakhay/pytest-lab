import random
import time


class OrderProcessing:

    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, amount):
        if order_id in self.orders:
            raise ValueError("Order ID already exists")

        if amount <= 0:
            raise ValueError("Order amount must be positive")

        self.orders[order_id] = {"amount": amount, "status": "pending"}
        return self.orders[order_id]

    def process_payment(self, order_id):
        if order_id not in self.orders:
            raise ValueError("Order not found")

        time.sleep(1)

        if random.choice([True, False]):
            self.orders[order_id]["status"] = "paid"
            return True
        else:
            self.orders[order_id]["status"] = "failed"
            return False

    def get_order_status(self, order_id):
        return self.orders.get(order_id, {}).get("status", "not found")
