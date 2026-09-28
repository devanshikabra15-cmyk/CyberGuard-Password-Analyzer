import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from analyzer import PasswordAnalyzer
from entropy import calculate_entropy, get_entropy_level
from security import calculate_score, check_common_password, get_strength


class TestCyberGuard(unittest.TestCase):

    def setUp(self):
        self.analyzer = PasswordAnalyzer()

    def test_strong_password(self):
        result = self.analyzer.analyze("Cyber@123")
        self.assertEqual(result.score, 5)
        self.assertEqual(result.strength, "VERY STRONG")
        self.assertFalse(result.common_password)

    def test_weak_password(self):
        result = self.analyzer.analyze("abc")
        self.assertEqual(result.score, 1)
        self.assertEqual(result.strength, "WEAK")

    def test_common_password(self):
        self.assertTrue(check_common_password("Password"))
        self.assertTrue(check_common_password("123456"))

    def test_entropy_empty(self):
        self.assertEqual(calculate_entropy(""), 0.0)

    def test_entropy_level(self):
        self.assertEqual(get_entropy_level(20), "LOW")
        self.assertEqual(get_entropy_level(50), "MODERATE")
        self.assertEqual(get_entropy_level(80), "HIGH")

    def test_empty_password_rejected(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze("")

    def test_score_boundaries(self):
        self.assertEqual(get_strength(calculate_score(8, True, True, True, True)), "VERY STRONG")
        self.assertEqual(get_strength(4), "STRONG")
        self.assertEqual(get_strength(3), "MODERATE")
        self.assertEqual(get_strength(2), "WEAK")


if __name__ == "__main__":
    unittest.main()
