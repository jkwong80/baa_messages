from baa_messages.util import get_time
import unittest
import time

class TestUtilities(unittest.TestCase):
    def test_get_time(self):
        t = time.time()

        x = get_time(t)
        self.assertEqual(x / 1e6, t)
        # self.assert(True)

if __name__=="__main__":
    unittest.main()
