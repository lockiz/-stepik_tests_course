import pickle
import sys

input_words = [i.strip() for i in sys.stdin.readlines()]

with open(input_words[0], mode='rb') as file_read:
    f = pickle.load(file_read)
    print(f(*input_words[1:]))
