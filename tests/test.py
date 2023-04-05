import unittest

from get_response_risklevel import get_response_risklevel

class TestResponse(unittest.TestCase):
    def test_high(self):
        request_json_high = {
            "YearsAtCompany": 1,              
            "EmployeeSatisfaction": 0.1,      
            "Position": "Non-Manager",        
            "Salary": 4,                     
        }
        self.assertEqual(get_response_risklevel(request_json_high), "High", "Should be High")

    def test_low(self):
        request_json_low = {
            "YearsAtCompany": 10,
            "EmployeeSatisfaction": 10.5,
            "Position": "Manager",
            "Salary": 5,
        }
        self.assertEqual(get_response_risklevel(request_json_low), "Low", "Should be Low")


if __name__ == '__main__':
    unittest.main()