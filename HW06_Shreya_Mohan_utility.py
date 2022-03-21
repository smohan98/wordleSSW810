import random
import os
import logging

class Utility:

    def __init__(self):
        self.words = []

    def __str__(self):
            return f'Utility: ({self.words})'

    def file_transfer(self):
        src_file = 'words.txt'
        src_dir = os.getcwd()
        src_file_location = os.path.join(src_dir, src_file)
        dest_file_location = os.path.join(src_dir, 'new_words.txt')
        self.words= []
        try:
            with open(src_file_location, 'r') as f1:
                with open(dest_file_location, 'w') as f2:
                    for word in f1:
                        if len(word.strip()) == 5:
                            f2.write(word)
                            self.words.append(word)
        except Exception as e:
            self.write_logs(f"ERROR : File Error {e}",True)
        return self.words

    def write_logs(self,message,log_type_error=False):
        if not os.path.exists("gameplay.log"):
            file = open('gameplay.log','a+')
        logging.basicConfig(filename="gameplay.log",format="%(asctime)s %(message)s", filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        if log_type_error: 
            logger.error(message) 
        else:
            logger.info(message) 