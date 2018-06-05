from mypackage.mymathlib import *


class TestClass01:
    def test_case01(self):
        print("In test_case01()")
        assert mymathlib().sub(5, 3) == 2
