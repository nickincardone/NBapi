import unittest
from nba.utils import clease_season

class TestCleaseSeason(unittest.TestCase):
    def setUp(self):
        pass

    def test_int(self):
        self.assertEqual('1999-00', clease_season(99))
        self.assertEqual('1999-00', clease_season(1999))
        self.assertEqual('2000-01', clease_season(0))
        self.assertEqual('2000-01', clease_season(2000))
        self.assertEqual('1985-86', clease_season(85))
        self.assertEqual('1985-86', clease_season(1985))
        self.assertEqual('2009-10', clease_season(9))
        self.assertEqual('2009-10', clease_season(2009))
        self.assertEqual('2011-12', clease_season(11))
        self.assertEqual('2011-12', clease_season(2011))
        
    def test_str(self):
        self.assertEqual('2000-01', clease_season('2000-2001'))
        self.assertEqual('2014-15', clease_season('2014-15'))
        self.assertEqual('2014-15', clease_season('2014'))
        self.assertEqual('2014-15', clease_season('14'))
        self.assertEqual('2000-01', clease_season('0'))

    def test_bad_input(self):
        self.assertRaises(ValueError, clease_season, ('a'))
        self.assertRaises(ValueError, clease_season, ('1700'))
        self.assertRaises(ValueError, clease_season, (3000))
        self.assertRaises(ValueError, clease_season, (1700))
        self.assertRaises(ValueError, clease_season, (1939))
        self.assertRaises(ValueError, clease_season, (113))
        self.assertRaises(ValueError, clease_season, ([1999]))


if __name__ == '__main__':
    unittest.main()