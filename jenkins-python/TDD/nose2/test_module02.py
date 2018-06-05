from . import mymath


math_obj = 0


class TestClass01:
    def test_case01(self):
        print("In test_case01()")
        assert mymath.multiply(2, 5) == 7
