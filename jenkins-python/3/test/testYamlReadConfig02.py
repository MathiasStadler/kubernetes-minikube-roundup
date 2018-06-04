from YamlReadConfig import YamlReadConfig
from nose.tools import with_setup, timed, raises
import os
import inspect
import time


math_obj = 0


def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")
    global math_obj
    math_obj = YamlReadConfig()


def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")
    global math_obj
    del math_obj


class TestClass01:

    @classmethod
    def setUpClass(cls):
        """called once, before any test in the class"""
        print("In setUpClass()...")

    def setUp(self):
        """called before every test method"""
        print("\nIn setUp() method...")

    def whereWeAre(self):
        print("File => %s" % os.path.basename(__file__))
        print("CLass => %s" % self.__class__.__name__)
        print ("def => %s" % inspect.stack()[1][3])

    def tearDown(self):
        """called after every test method"""
        print("In tearDown() method...")

    @classmethod
    def tearDownClass(self):
        """called once, after all tests, if setUpClass() successful"""
        print ("\nIn tearDownClass()...")

    def setup_function(self):
        """setup_function(): use it with @with_setup() decorator"""
        print("\nsetup_function()...")

    def teardown_function(self):
        """teardown_function(): use it with @with_setup() decorator"""
        print("\nteardown_function()...")

    # Test Cases
    def test_case01(self):
        self.whereWeAre()
        assert YamlReadConfig().getConfigValue('server') == 'localhost'

    def test_case02(self):
        self.whereWeAre()
        assert YamlReadConfig().getConfigValue('user') == 'admin'

    @with_setup(setup_function, teardown_function)
    def test_case03(self):
        print("In test_case03()...")

    @raises(TimeExpired)
    @timed(.1)
    def test_caseTimed(self):
        time.sleep(.2)
        raise TimeExpired("This test passes")
