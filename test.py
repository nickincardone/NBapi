import unittest
from nba.utils import clease_season, set_to_dict

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

class TestSetToDict(unittest.TestCase):
    def setUp(self):
        self.example = {
            "name": "LastMeeting",
            "headers": ["GAME_ID", "LAST_GAME_ID", "LAST_GAME_DATE_EST", "LAST_GAME_HOME_TEAM_ID", "LAST_GAME_HOME_TEAM_CITY", "LAST_GAME_HOME_TEAM_NAME", "LAST_GAME_HOME_TEAM_ABBREVIATION", "LAST_GAME_HOME_TEAM_POINTS", "LAST_GAME_VISITOR_TEAM_ID", "LAST_GAME_VISITOR_TEAM_CITY", "LAST_GAME_VISITOR_TEAM_NAME", "LAST_GAME_VISITOR_TEAM_CITY1", "LAST_GAME_VISITOR_TEAM_POINTS"],
            "rowSet": [
                ["0021400967", "0021400845", "2015-02-25T00:00:00", 1610612766, "Charlotte", "Hornets", "CHA", 98, 1610612741, "Chicago", "Bulls", "CHI", 86],
                ["0021400968", "0021300959", "2014-03-12T00:00:00", 1610612755, "Philadelphia", "76ers", "PHI", 98, 1610612758, "Sacramento", "Kings", "SAC", 115]
            ]
        }
        self.result = set_to_dict(self.example)

    def test_correct_values(self):
        self.assertEqual('0021400967', self.result[0]['GAME_ID'])
        self.assertEqual(
            1610612755, self.result[1]['LAST_GAME_HOME_TEAM_ID'])

    def test_correct_num_of_rows(self):
        self.assertEqual(2, len(self.result))

    def test_has_all_keys(self):
        for key in self.result[0]:
            self.assertIn(key, self.example['headers'])
        for key in self.result[1]:
            self.assertIn(key, self.example['headers'])



if __name__ == '__main__':
    unittest.main()