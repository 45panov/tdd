class Money:
    def __init__(self, amount: int, curr: str):
        self._amount = amount
        self.curr = curr

    def __eq__(self, other):
        if self._amount == other._amount and self.curr == other.curr:
            return True
        else:
            return False

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self.curr

    def times(self, multiplier):
        return Money(self._amount * multiplier, self.curr)


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2), "False!"
    assert Money.dollar(15) == five.times(3), "False!"

    six = Money.franc(6)
    assert Money.franc(12) == six.times(2), "False!"
    assert Money.franc(18) == six.times(3), "False!"


def test_equality():
    assert Money.dollar(5) == Money.dollar(5), "Dollar(5) == Dollar(5) must be True!"
    assert not Money.dollar(5) == Money.dollar(6), "Dollar(5) == Dollar(6) must be False!"

    assert Money.franc(5) == Money.franc(5), "Franc(5) == Franc(5) must be True!"
    assert not Money.franc(5) == Money.franc(6), "Franc(5) == Franc(6) must be False!"
    assert not Money.franc(5) == Money.dollar(5), "5 Francs are not equal to 5 Dollars"


def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five.times(2), "Franc(5) == Franc(5) must be True!"
    assert Money.franc(15) == five.times(3), "Franc(5) == Franc(6) must be False!"


def test_currency():
    assert 'USD' == Money.dollar(1).currency(), "Money.dollar(1).currency() must be equal to 'USD'"
    assert 'CHF' == Money.franc(1).currency(), "Money.franc(1).currency() must be equal to 'CHF'"


test_multiplication()
test_equality()
test_franc_multiplication()
test_currency()
