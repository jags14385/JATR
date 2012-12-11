from _src.runner import TestRun
from _src.reporter import Reporter

if __name__=='__main__':
    TestRun.executeTestRun()
    Reporter.test_results_display()