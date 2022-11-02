import pytest
from stack import is_balanced_check

FIXTURES = [('(((([{}]))))', True),
            ('[([])((([[[]]])))]{()}', True),
            ('{{[()]}}', True),
            ('}{}', False),
            ('{{[(])]}}', False),
            ('[[{())}]', False)]


@pytest.mark.parametrize('string, exp_res', FIXTURES)
def test_is_balanced_check(string, exp_res):
    result = is_balanced_check(string)
    assert exp_res == result
