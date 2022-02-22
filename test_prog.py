
import unittest
import HW02_Shreya_Mohan as program
import HW03_Shreya_Mohan_dictionary as dictionary
import HW03_Shreya_Mohan_ui as ui
from unittest.mock import patch

class TestWordle(unittest.TestCase):
    
    def test_fileReader(self):
        self.assertGreater(len(dictionary.file_reader()),0)
        
    def test_wordPicker(self):
        self.assertIsNotNone(dictionary.word_picker())
    
    def test_letterChecker(self):
        st,count =program.letter_checker('','HAPPY','HAPPY')
        self.assertTrue(count,5)

    def test_letterCheckerFalse(self):
        st,count =program.letter_checker('','ARISE','HAPPY')
        self.assertFalse(count,5)

    @patch('builtins.input', side_effect = ['hello'])
    def test_user(self, mock_inputs) -> None :
        words_list=dictionary.file_reader()
        self.assertEqual(ui.user(1,["SMALL","HAPPY","WATER"],words_list),(True,'HELLO'))

    
    @patch('builtins.input', side_effect = ['happy'])
    def test_user2(self, mock_inputs) -> None :
        words_list=dictionary.file_reader()
        self.assertEqual(ui.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'You have already entered this word.'))

    
    @patch('builtins.input', side_effect = ['happ'])
    def test_user3(self, mock_inputs) -> None :
        words_list=dictionary.file_reader()
        self.assertEqual(ui.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Please enter a valid 5 letter word consisting of only alphabets.'))


   
    @patch('builtins.input', side_effect = ['asdfg'])
    def test_user4(self, mock_inputs) -> None :
        words_list=dictionary.file_reader()
        self.assertEqual(ui.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Word is not in dictionary'))


    
    @patch('builtins.input', side_effect = ['h23p@'])
    def test_user5(self, mock_inputs) -> None :
        words_list=dictionary.file_reader()
        self.assertEqual(ui.user(1,["SMALL","HAPPY","WATER"],words_list),(False,'Please enter a valid 5 letter word consisting of only alphabets.'))


if __name__ == '__main__':
    unittest.main()