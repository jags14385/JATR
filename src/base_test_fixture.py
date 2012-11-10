class BaseTestFixture:
    
    @classmethod
    def setUp(cls):
        print "Setup method Test Level /Method Level in BaseTestFixture"
        
    @classmethod
    def setUp_class(cls):
        print "Setup method Class Level BaseTestFixture"
        
    @classmethod
    def tearDown(cls):
        print "TearDown method Test Level /Method Level BaseTestFixture"
        
    @classmethod
    def tearDown_class(cls):
        print "TearDown method Class Level BaseTestFixture"  