from _src.runner import TestRun
from _src.reporter import Reporter
#from ConfigParser import SafeConfigParser

if __name__=='__main__':
    TestRun.executeTestRun()
    Reporter.test_results_display()
#    conf_parser= SafeConfigParser()
#    conf_parser.read('/Users/vaikuntj/Work/Testing/JATR/config/config.ini')
#    print conf_parser.sections()