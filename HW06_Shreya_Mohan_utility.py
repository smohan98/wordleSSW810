import random
import os
import logging

def file_transfer():
    src_file = 'words.txt'
    src_dir = os.getcwd()
    src_file_location = os.path.join(src_dir, src_file)
    dest_file_location = os.path.join(src_dir, 'new_words.txt')
    words= []
    try:
        with open(src_file_location, 'r') as f1:
            with open(dest_file_location, 'w') as f2:
                for word in f1:
                    if len(word.strip()) == 5:
                        f2.write(word)
                        words.append(word)
    except Exception as e:
        write_logs(f"ERROR : File Error {e}",True)
    return words

def write_logs(message,log_type_error=False):
    logging.basicConfig(filename="gameplay.log",format="%(asctime)s %(message)s", filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if log_type_error: 
        logger.error(message) 
    else:
        logger.info(message) 