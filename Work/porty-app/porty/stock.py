class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price) -> None:
       self.name = name
       self.shares = shares
       self.price = price 
    
    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num
        return self.shares
