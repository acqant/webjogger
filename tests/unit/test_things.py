import sys
import pytest
sys.path.insert(0,'./sample_stuff')
from sample_stuff import app



@pytest.fixture(name='some_data')
def var_log_mess():
   """

   :return: None
   """
   return [1]


def test_it():
    """
    test it
    """
    app.HelperLib.get_some_int()
    
