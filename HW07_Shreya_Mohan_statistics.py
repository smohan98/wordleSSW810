import csv
import operator
from HW06_Shreya_Mohan_utility import file_transfer


def file_statistics():
    try:
        letters = {}

        all_words = file_transfer()
        
        for word in all_words:
            word = word.strip()
            for i,letter in enumerate(word):
                if letter not in letters:
                    letters[letter] = [0,0,0,0,0]
                letters[letter][i] += 1

        letters = dict( sorted(letters.items(), key=operator.itemgetter(0)))

        rows = []
        for key in letters:
            prob = [round(number/len(all_words),3) for number in letters[key]]
            temp = [key]+prob
            rows.append(temp)
        
        with open("letterFrequency.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
    except Exception as e:
        print(f"File statistics error: {e}")

def csv_to_dict(filename):
    letters = {}

    with open(filename, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        letters = {rows[0]:[rows[1],rows[2],rows[3],rows[4],rows[5]] for rows in reader}

    return letters

def word_ranking():
    try:
        letters = csv_to_dict('letterFrequency.csv')

        all_words = file_transfer()

        ranks = {}
        
        for word in all_words:
            word = word.strip()
            prod = 1
            for i,letter in enumerate(word):
                prod *= float(letters[letter][i])
            ranks[word] = f"{prod:.14f}"

        sorted_list = sorted(ranks.items(), key=lambda x:x[1],reverse=True)

        with open('wordRank.csv','w') as f:
            writer=csv.writer(f)
            for i,row in enumerate(sorted_list):
                writer.writerow([i+1]+list(row))
        
    except Exception as e:
        print(f"Word ranking error: {e}")