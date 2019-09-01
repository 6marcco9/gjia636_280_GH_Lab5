import unittest
import logger
from logger import Logger

class Target:
    def _target(self,text):
        self.text = text
    
    def get_target(self):
        return self.text
        

class LoggerTest(unittest.TestCase):   
    
    def test_info(self):
        target = Target()
        log = Logger(target._target)
        log.info("msg")
        
        self.assertEqual("[INFO] msg", target.get_target())
                
    
    def test_error(self):
        target = Target()
        log = Logger(target._target)
        log.error("test")
        
        self.assertEqual("[WARNING] test", target.get_target())

if __name__ == '__main__':
    unittest.main()