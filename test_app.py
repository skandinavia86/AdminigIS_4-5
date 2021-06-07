from bddb import Clients, Orders, init
import pytest

def test_struc():
    assert len(Clients.select()) >= 10
    assert len(Orders.select()) >=10
    
def test_init():
    assert init('clients', 'orders') == True

def test_column():
    assert Clients.Name == True
    assert Clients.City == True
    assert Clients.Address == True

    assert Orders.Client_id == True
    assert Orders.Amount ==True
    assert Orders.Date == True
    assert Orders.Description == True
