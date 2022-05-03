import unittest
from app.routers.predictServer import predict
import asyncio

class TestPredict(unittest.TestCase):

    def test_predict(self):
        print("Hiii")
        assert asyncio.run(predict(1,1,1,1,True)) == 0.0
