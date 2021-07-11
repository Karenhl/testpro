import pytest

from testpro.Calcutator import Calcutator


class TestCal(object):

    def setup_class(self):
        print("计算开始")
        self.calc = Calcutator()

    @pytest.mark.parametrize('x,y,exceptnum', [
        (1, 1, 2),
        (2, 2, 4)
    ])
    def test_add(self, x, y, exceptnum):
        assert self.calc.add(x, y) == exceptnum

    @pytest.mark.parametrize('x,y,exceptnum', [
        (1, 1, 1),
        (4, 2, 2)
    ])
    def test_div(self, x, y, exceptnum):
        assert self.calc.div(x, y) == exceptnum

    def teardown_class(self):
        print("计算结束")
