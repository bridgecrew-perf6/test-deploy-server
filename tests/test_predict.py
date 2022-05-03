import unittest
import cProfile
from app.routers.predictServer import predict

class TestPredict(unittest.TestCase):

    def test_predict(self):
        assert predict(1,1,1,1,True) == 0.0

"""
    def test_profiling(self):
        cProfile.run('predict(1,1,1,1,True)', filename='predict_profile.out')
"""

