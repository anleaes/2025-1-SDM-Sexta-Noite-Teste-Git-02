class Order:
    def __init__(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client
    
    def __str__(self):
        return f"Order(total_price={self.total_price}, status={self.status}, client={self.client})"
