from english_words import english_words_lower_alpha_set
from statistics import stdev
import random

word_length = 5

words = [x for x in filter(lambda x: len(x)==word_length, english_words_lower_alpha_set)]

def get_similarity(realword, testword):
    result = ''
    for i, letter in enumerate(testword):
        if letter == realword[i]: result += 'G'
        elif letter in realword:  result += 'Y'
        else:                     result += '_'

    return result

def get_score(wordlist, testword):
    results = {}

    for realword in wordlist:
        x = get_similarity(testword, realword)
        if x not in results: results[x]=0
        results[x]+=1

    results2 = list(results.values()) + [0]
    #results += [0]* (3**word_length - len(results))

    score = 0

    if len(results2)<2:
        if 'G'*word_length in results: score = -100
        else: score = 10000
    else: score = stdev(results2)

    if testword in wordlist: score -= 0.01

    return score

def get_best_word(wordlist):
    testdict = {}

    for word in words:
        testdict[word]=get_score(wordlist,word)

    top = sorted(testdict.keys(),key=lambda x:testdict[x])
    #for x in top[0:10]: print(x, testdict[x])

    return top[0]


def solve(masterword):
    wordlist = [x for x in words]
    current_guess = 'raise'#get_best_word(wordlist)
    i=1
    while True:
        pattern = get_similarity(masterword, current_guess)
        print(current_guess,pattern)
        if current_guess==masterword: return i

        wordlist = [x for x in wordlist if get_similarity(x, current_guess)==pattern]
        current_guess = get_best_word(wordlist)
        i+=1
        #print(wordlist)
        #print('-'*30)

hardwords = {}

for i in range(100):
    wordle = random.choice(words)
    hardwords[wordle] = solve(wordle)
    print()


for x in hardwords:
    if hardwords[x]>=6: print(x,hardwords[x])

print(sum(hardwords.values())/100)