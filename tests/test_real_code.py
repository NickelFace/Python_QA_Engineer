from src.Account import Account


def test_account_create():
    a = Account("Mr.X", 0)
    assert isinstance(a, Account)
    assert a.balance == 0
    assert a.owner == "Mr.X"
