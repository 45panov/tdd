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
        return Dollar(amount, 'USD')

    def franc(amount):
        return Franc(amount, 'CHF')

    def currency(self):
        return self.curr

    def times(self, multiplier):
        return Money(self._amount * multiplier, self.curr)


class Dollar(Money):
    def __init__(self, amount, curr=None):
        super().__init__(amount, curr)

    # def times(self, multiplier):
    #     return Money(self._amount * multiplier, self.curr)


class Franc(Money):
    def __init__(self, amount, curr=None):
        super().__init__(amount, curr)

    # def times(self, multiplier):
    #     return Money(self._amount * multiplier, self.curr)


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2), "False!"
    assert Money.dollar(15) == five.times(3), "False!"

    six = Money.franc(6)
    assert Money.franc(12) == six.times(2), "False!"
    assert Money.franc(18) == six.times(3), "False!"


def test_equality():
    assert Dollar(5) == Dollar(5), "Dollar(5) == Dollar(5) must be True!"
    assert not Dollar(5) == Dollar(6), "Dollar(5) == Dollar(6) must be False!"

    assert Franc(5) == Franc(5), "Franc(5) == Franc(5) must be True!"
    assert not Franc(5) == Franc(6), "Franc(5) == Franc(6) must be False!"
    assert not Franc(5, 'CHF') == Dollar(5, 'USD'), "5 Francs are not equal to 5 Dollars"


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2), "Franc(5) == Franc(5) must be True!"
    assert Franc(15) == five.times(3), "Franc(5) == Franc(6) must be False!"


def test_currency():
    assert 'USD' == Money.dollar(1).currency(), "Money.dollar(1).currency() must be equal to 'USD'"
    assert 'CHF' == Money.franc(1).currency(), "Money.franc(1).currency() must be equal to 'CHF'"

def test_different_class_equality():
    assert Money(10, 'CHF') == Franc(10, 'CHF'), "Object Money(10, 'CHF') must be equal to Franc(10, 'CHF')"

test_multiplication()
test_equality()
test_franc_multiplication()
test_currency()
test_different_class_equality()