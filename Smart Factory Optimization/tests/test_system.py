import unittest
from downtime_prediction import predict_downtime

class TestDowntimePrediction(unittest.TestCase):
    def test_low_risk(self):
        data = {"temperature": 50, "vibration": 1.0}
        self.assertEqual(predict_downtime(data), "Low Risk")
    
    def test_high_risk(self):
        data = {"temperature": 90, "vibration": 4.0}
        self.assertEqual(predict_downtime(data), "High Risk")

if __name__ == "__main__":
    unittest.main()