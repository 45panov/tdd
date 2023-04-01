class Expression():
    def __add__(self, other):
        augend = self
        addend = other
        return Sum(augend, addend)

    def reduce(self, to):
        return self


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Bank:
    def reduce(self, source, to: str):
        self.sum = source
        return self.sum.reduce(to)


class Money(Expression):
    def __init__(self, amount, curr: str):
        self._amount = amount
        self.curr = curr

    def __eq__(self, other):
        if self._amount == other._amount and self.curr == other.curr:
            return True
        else:
            return False

    def __mul__(self, multiplier):
        return Money(self._amount * multiplier, self.curr)

    def dollar(amount):
        return Money(amount, 'USD')

    def franc(amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self.curr


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five * 2, "Money.dollar(10) must be equal to five * 2"
    assert Money.dollar(15) == five * 3, "Money.dollar(15) must be equal to five * 3"

    six = Money.franc(6)
    assert Money.franc(12) == six * 2, "Money.franc(12) must be equal to six * 2"
    assert Money.franc(18) == six * 3, "Money.franc(18) must be equal to six * 3"


def test_equality():
    assert Money.dollar(5) == Money.dollar(5), "Dollar(5) == Dollar(5) must be True!"
    assert not Money.dollar(5) == Money.dollar(6), "Dollar(5) == Dollar(6) must be False!"

    assert Money.franc(5) == Money.franc(5), "Franc(5) == Franc(5) must be True!"
    assert not Money.franc(5) == Money.franc(6), "Franc(5) == Franc(6) must be False!"
    assert not Money.franc(5) == Money.dollar(5), "5 Francs are not equal to 5 Dollars"


def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five * 2, "Franc(5) == Franc(5) must be True!"
    assert Money.franc(15) == five * 3, "Franc(5) == Franc(6) must be False!"


def test_currency():
    assert 'USD' == Money.dollar(1).currency(), "Money.dollar(1).currency() must be equal to 'USD'"
    assert 'CHF' == Money.franc(1).currency(), "Money.franc(1).currency() must be equal to 'CHF'"


def test_simple_addition():
    sum = Money.dollar(5) + Money.dollar(5)
    assert Money.dollar(10) == sum, "Money.dollar(5) + Money.dollar(5) must be an equal to Money.dollar(10)"

    five = Money.dollar(5)
    sum = five + five
    bank = Bank()
    reduced = bank.reduce(sum, 'USD')
    assert Money.dollar(10) == reduced, "Money.dollar must be equal to reduced!"


def test_plus_returns_sum():
    five = Money.dollar(5)
    result = five + five
    sum = result
    assert five == sum.augend, "five must be equal to sum.augend"
    assert five == sum.addend, "five must be equal to sum.addend"


def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, 'USD')
    assert Money.dollar(7) == result, "Money.dollar(7) must be equal to result"


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), 'USD')
    assert Money.dollar(1) == result, "Money.dollar(1) must be equal to result"


test_multiplication()
test_equality()
test_franc_multiplication()
test_currency()
# test_simple_addition()
test_plus_returns_sum()
test_reduce_sum()
test_reduce_money()
