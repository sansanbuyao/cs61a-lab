def time_to_retire(self, amount):
    """Return the number of years until balance would grow to amount."""
    assert self.balance > 0 and amount > 0 and self.interest > 0
    years = math.ceil(math.log(amount / self.balance, 1 + self.interest))
    return years
