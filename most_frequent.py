from collections import Counter

def most_frequent(list):
    most=[word for word, word_count in Counter(list).most_common(5)]
    print (most)

list=[3, 5, 1, 5, 6, 1, 1, 3, 4, 2, 3, 4, 5, 3, 4, 10, 10]

most_frequent(list)