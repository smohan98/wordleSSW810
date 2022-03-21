
import unittest
import HW02_Shreya_Mohan as program
import HW03_Shreya_Mohan_dictionary as dictionary
import HW03_Shreya_Mohan_ui as ui
import HW06_Shreya_Mohan_utility as ut
import HW07_Shreya_Mohan_statistics as stats
from unittest.mock import patch
import pathlib as pl


"""Unit tests for wordle"""
"""Unit tests using TestWordle class"""

class TestWordle(unittest.TestCase):
    
    def test_fileReader(self):
        d = dictionary.Dictionary()
        self.assertGreater(len(d.file_reader()),0)
        
    def test_letterChecker(self):
        prog = program.Game()
        st,count =prog.letter_checker('','HAPPY','HAPPY')
        self.assertTrue(count,5)

    def test_letterCheckerFalse(self):
        prog = program.Game()
        st,count =prog.letter_checker('','ARISE','HAPPY')
        self.assertFalse(count,5)

    @patch('builtins.input', side_effect = ['hello'])
    def test_user(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        words_list=d.file_reader()
        u = ui.Info()
        self.assertEqual(u.user(1,["SMALL","HAPPY","WATER"],words_list),(True,'HELLO'))

    
    @patch('builtins.input', side_effect = ['happy'])
    def test_user2(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        words_list=d.file_reader()
        u = ui.Info()
        self.assertEqual(u.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'You have already entered this word.'))

    
    @patch('builtins.input', side_effect = ['happ'])
    def test_user3(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        words_list=d.file_reader()
        u = ui.Info()
        self.assertEqual(u.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Please enter a valid 5 letter word consisting of only alphabets.'))


   
    @patch('builtins.input', side_effect = ['asdfg'])
    def test_user4(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        words_list=d.file_reader()
        u = ui.Info()
        self.assertEqual(u.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Word is not in dictionary'))


    
    @patch('builtins.input', side_effect = ['h23p@'])
    def test_user5(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        words_list=d.file_reader()
        u = ui.Info()
        self.assertEqual(u.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Please enter a valid 5 letter word consisting of only alphabets.'))



    @patch('builtins.input', side_effect = [''])
    def test_user6(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        self.assertIsNotNone(d.word_picker([]))

    

    @patch('builtins.input', side_effect = [''])
    def test_user7(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        self.assertIsNotNone(d.word_picker(["MONEY"]))


    
    @patch('builtins.input', side_effect = ['Month'])
    def test_user8(self, mock_inputs) -> None :
        d = dictionary.Dictionary()
        self.assertIsNotNone(d.word_picker([]))


    
    def test_fileTransfer(self):
        utils = ut.Utility()
        self.assertGreater(len(utils.file_transfer()),0)



    def test_fileStatistics(self):
        if not pl.Path("letterFrequency.csv").resolve().is_file():
            raise AssertionError("File does not exist: %s" % str("letterFrequency.csv"))



    def test_CSVtoDict(self):
        stat = stats.Statistics()
        self.assertTrue(stat.csv_to_dict)

    
    def test_wordRanking(self):
        if not pl.Path("wordRank.csv").resolve().is_file():
            raise AssertionError("File does not exist: %s" % str("wordRank.csv"))


if __name__ == '__main__':
    unittest.main()