class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
            pass
    
    def tearDown(self):
        pass
        
    def run(self):
        # result.testStarted()
        self.setUp()
        exec("self." + self.name + "()")
        self.tearDown()
        # method = getattr(self, self.name)
        # method()
    
    # def tearDown(self):
    #     pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
       
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    
    def tearDown(self):
        self.log = self.log + "tearDown "

    def setUp(self):
        self.wasRun = None
        # self.wasSetUp = 1
        self.log = "setUp "
        
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    # def testRunning(self):
    #     self.test.run()
    #     assert self.test.wasRun, "self.test.wasRun must be True"

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log, "\"setUp testMethod tearDown \" must be equal to self.test.log"
        
# TestCaseTest("testRunning").run()
TestCaseTest("testTemplateMethod").run()