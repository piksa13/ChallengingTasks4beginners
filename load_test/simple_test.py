'''
unittest.TestCase hooks
> setUpClass
    > setUp
        > test_*
    > tearDown
> tearDownClass
'''

import time
import unittest

SLOW_TEST_THRESHOLD = 0.3

class SlowTestCase(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print(f'{self.id()} ({round(elapsed, 3)})s')

    def test_fast(self):
        self.assertEqual(1, 1)

    def test_slow(self):
        time.sleep(0.5)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
