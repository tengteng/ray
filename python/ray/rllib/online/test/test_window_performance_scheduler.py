from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

import ray


# TODO(teng.t): Write unit test for WindowPerformanceScheduler.
class WindowPerformanceSchedulerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    ray.init(num_cpus=1)
    unittest.main(verbosity=2)
