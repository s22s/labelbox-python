from lb_logger import logger
import unittest

class TestLoggerMessages(unittest.TestCase):
    """
    Test that the logger's out put will match the expected levels set by logger
    """

    def setUp(self):
        self.msg = "Test message""
        self.test_logger = logger
    
    def test_info_msg(self):
        with self.assertLogs(self.test_logger) as assert_log:
            self.test_logger.info(self.msg)
        self.assertEqual(assert_log.output, ['INFO:lb_logger:%s' %(self.msg)])

    def test_warning_msg(self):
        with self.assertLogs(self.test_logger) as assert_log:
            self.test_logger.warning(self.msg)
        self.assertEqual(assert_log.output, ['WARNING:lb_logger:%s' %(self.msg)])    

    def test_error_msg(self):
        with self.assertLogs(self.test_logger) as assert_log:
            self.test_logger.error(self.msg)
        self.assertEqual(assert_log.output, ['ERROR:lb_logger:%s' %(self.msg)])    

    def test_critical_msg(self):
        with self.assertLogs(self.test_logger) as assert_log:
            self.test_logger.critical(self.msg)
        self.assertEqual(assert_log.output, ['CRITICAL:lb_logger:%s' %(self.msg)])           
