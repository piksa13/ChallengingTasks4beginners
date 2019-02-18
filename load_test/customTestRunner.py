# import unittest
#
#
# class TimeLoggingTestRunner(unittest.TextTestRunner):
#
#     def __init__(self, slow_test_threshold=0.3, *args, **kwargs):
#         self.slow_test_threshold = slow_test_threshold
#
#         return super().__init__(
#             resultclass=TimeLoggingTestResult,
#             *args,
#             **kwargs,
#         )
#
#     def run(self, test):
#         result = super().run(test)
#         self.stream.writeln(
#             "\nSlow Tests (>{:.03}s):".format(
#                 self.slow_test_threshold))
#         for name, elapsed in result.getTestTimings():
#             if elapsed > self.slow_test_threshold:
#                 self.stream.writeln(
#                     "({:.03}s) {}".format(
#                         elapsed, name))
#         return result
#
