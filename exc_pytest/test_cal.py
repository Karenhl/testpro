# coding=utf-8
import pytest

from testpro.exc_pytest.Calcutator import Calcutator


class TestCal(object):

    def setup_class(self):
        print("计算开始")
        self.calc = Calcutator()

    @pytest.mark.parametrize('x,y,exceptnum', [
        (1, 1, 2),
        (-2, 2, 0)
    ], ids=["正数相加", "负数相加"])
    @pytest.mark.run(order=-1)
    def test_add(self, x, y, exceptnum):
        assert self.calc.add(x, y) == exceptnum

    @pytest.mark.parametrize('x,y,exceptnum', [
        (1, 1, 1),
        (4, -2, -2)
    ], ids=["正数相除", "负数相除"])
    @pytest.mark.run(order=1)
    def test_div(self, x, y, exceptnum):
        assert self.calc.div(x, y) == exceptnum

    def teardown_class(self):
        print("计算结束")
