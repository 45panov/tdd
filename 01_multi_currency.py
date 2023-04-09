class Expression():

    def reduce(self, bank, to):
        return self

    def __add__(self, addend):
        return Sum(self, addend)

    def __mul__(self, multiplier):
        return Money(self._amount * multiplier, self.curr)


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to)._amount + \
                 self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def __mul__(self, multiplier):
        return Sum(self.augend * multiplier, self.addend * multiplier)


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to: str):
        return source.reduce(self, to)

    def add_rate(self, fromm, to, rate): # variable named fromm to avoid operator name from
        self.rates.update({Pair(fromm, to): rate})

    def rate(self, fromm, to):
        if fromm == to: return 1
        return self.rates[Pair(fromm, to)]


class Pair:
    def __init__(self, fromm, to):
        self.fromm = fromm
        self.to = to

    def __eq__(self, other):
        return self.fromm, self.to == other.fromm, other.to

    def __hash__(self):
        return 0


class Money(Expression):
    def __init__(self, amount, curr: str):
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

    def reduce(self, bank, to):
        rate = bank.rate(self.curr, to)
        return Money(self._amount / rate, to)




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
    # sum = Money.dollar(5) + Money.dollar(5)
    # assert Money.dollar(10) == sum, "Money.dollar(5) + Money.dollar(5) must be an equal to Money.dollar(10)"

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


def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate('CHF', 'USD', 2)
    result = bank.reduce(Money.franc(2), 'USD')
    assert Money.dollar(1) == result, "Money.dollar(1) must be equal to result!"


def test_pairs():
    assert Pair('USD', 'CHF') == Pair('USD', 'CHF'), "Pair('USD', 'CHF') must be equal to Pair('USD', 'CHF')"


def test_identity_rate():
    bank = Bank()
    assert 1 == bank.rate('USD', 'USD'), "Bank.rate('USD', 'USD') must be equal to 1!"


def test_mixed_addition():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate('CHF', 'USD', 2)
    result = bank.reduce(five_bucks + ten_francs, 'USD')
    assert Money.dollar(10) == result, "Money.dollar(10) must be equal to result!"

def test_sum_times():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate('CHF', 'USD', 2)
    sum = (five_bucks + ten_francs) * 2
    result = bank.reduce(sum, 'USD')
    assert Money.dollar(20) == result

def test_plus_same_currency_returns_money(): # Test fails.
    sum = Money.dollar(1) + Money.dollar(1)
    assert isinstance(sum, Money), "Variable sum must be an instance of class Money!"


test_multiplication()
test_equality()
test_franc_multiplication()
test_currency()
test_simple_addition()
test_plus_returns_sum()
test_reduce_sum()
test_reduce_money()
test_reduce_money_different_currency()
test_pairs()
test_identity_rate()
test_mixed_addition()
test_sum_times()
# test_plus_same_currency_returns_money() 