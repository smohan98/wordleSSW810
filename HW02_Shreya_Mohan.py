import HW03_Shreya_Mohan_ui as ui
import HW03_Shreya_Mohan_dictionary as dictionary
# from HW06_Shreya_Mohan_utility import write_logs
# from HW07_Shreya_Mohan_statistics import file_statistics,word_ranking
import HW06_Shreya_Mohan_utility as util
import HW09_Shreya_Mohan_helper as helper
import HW07_Shreya_Mohan_statistics as stat
import HW12_Shreya_Mohan_database as db


class Game:

    def __init__(self):
        self.words = []
        self.d = dictionary.Dictionary()
        self.utils = util.Utility()
        self.helper = helper.Helper()
        self.stats = stat.Statistics()
        self.u = ui.Info()
        self.db_logger = db.SqliteDatabase()

    def __str__(self):
        return f'Game: ({self.d}, {self.utils}, {self.stats}, {self.u})'

    def letter_checker(self, stmt, wordle, word):
        try:
            count = 0
            for i, ch in enumerate(wordle):
                if ch in word and ch not in wordle[:i]:
                    if word[i] == ch:
                        stmt += f"{ch}"
                        count += 1
                    else:
                        stmt += f"{ch}`"
                else:
                    stmt += f'{ch}"'
            return stmt, count
        except Exception as e:
            print(f"Error: {e}")

    def wordle_checker(self, win, guess, used_words):
        try:
            print('''WORDLE rules:
            > Enter a 5 letter word
            > You have to guess the Wordle in maximum tries
            > A correct letter turns green
            > A correct letter in the wrong place turns yellow
            > An incorrect letter turns gray
            ''')
            good, bad, correct = [], [], ''
            prev = []
            attempts = 6

            # all_words = self.d.file_reader()

            all_words = self.helper.possible_words(good, bad, correct, prev)
            wordle = all_words[0].lower()
            prev.append(wordle.lower())
            word = self.d.word_picker(used_words).lower()
            self.utils.write_logs(f"RANDOM WORD CHOSEN FOR THE GAME: {word}")
            self.db_logger.insert_in_game_main(word)
            used_words.append(word)

            # While loop that works till 6 attempts are made
            while attempts:
                # check,wordle = self.u.user(attempts,prev,all_words)

                all_words = self.helper.possible_words(
                    good, bad, correct, prev)
                wordle = all_words[0].lower()
                prev.append(wordle.lower())
                self.utils.write_logs(f'AUTO ENTERED: "{wordle.upper()}"')
                print(
                    f"Attempt #{7-attempts}\n Entered Word : {wordle.upper()}\n")
                # print(wordle)
                if word.strip() == wordle.strip():
                    win += 1
                    guess[6-attempts] += 1
                    self.utils.write_logs(
                        f"USER ENTERED THE CORRECT WORD: {wordle.upper()}")
                    print("Correct Word")
                    self.db_logger.insert_in_game_details(
                        attempt=7-attempts, wordle=word, input_word=wordle, log="")
                    return win, guess, used_words
                elif word != wordle:
                    # reduces the count after every valid attempt
                    attempts -= 1
                    # prev.append(wordle)
                    stmt = ""
                    # string comparison and checking the position of each character
                    stmt, count = self.letter_checker(stmt, wordle, word)
                    good, bad, correct = self.helper.good_bad_correct_generate(
                        wordle, word, stmt)
                    self.db_logger.insert_in_game_details(
                        attempt=6-attempts, wordle=word, input_word=wordle, log="")
                else:
                    print(wordle)

            print("Oops, you are out of chances. Better luck next time!")
            print(f"THE CORRECT WORD WAS: {word.upper()}")
            self.utils.write_logs(f"USER RAN OUT OF CHOICES")
            return win, guess, used_words
        except Exception as e:
            print(f"Error: {e}")

    def main(self, n):
        try:
            games_played = 0
            win = 0
            guess = [0]*6
            used_words = []
            self.stats.file_statistics()
            self.stats.word_ranking()
            while n:
                n -= 1
                games_played += 1
                win, guess, used_words = self.wordle_checker(
                    win, guess, used_words)
                print(f"GAMES PLAYED : {str(games_played)}")
                self.utils.write_logs(f"GAMES PLAYED : {str(games_played)}")
                print(f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
                self.utils.write_logs(
                    f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
                db_guess = ""
                for i in range(len(guess)):
                    print(f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")
                    self.utils.write_logs(
                        f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")
                    db_guess += f"{guess[i]}, "
                self.db_logger.insert_in_game_statistics(
                    win_status=win, number_of_games=games_played, win_percentage=f"{str((win*100)/games_played)} %", guesses=db_guess)

        except Exception as e:
            print(f"There has been an error: {e}")


if __name__ == "__main__":
    g = Game()
    g.main(4)
    g.db_logger.analyze("2022-04-28 00:00:00.000000",
                        "2022-04-29 00:00:00.000000")
    g.db_logger.end()
