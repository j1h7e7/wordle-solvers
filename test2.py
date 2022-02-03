#from english_words import english_words_lower_alpha_set
from statistics import stdev
import random
import json

word_length = 5

english_words_lower_alpha_set = json.loads(open("words3.txt").readline())

print('favor' in english_words_lower_alpha_set)

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

    results2 = list(results.values())

    score = max(results2)
    if testword in wordlist: score -= 0.1
    return score

def get_best_word(wordlist):
    if len(wordlist)<=2: return wordlist[0]

    testdict = {}

    for word in words:
        testdict[word]=get_score(wordlist,word)

    top = sorted(sorted(testdict.keys()),key=lambda x:testdict[x])
    #for x in top[0:10]: print(x, testdict[x])
    #print(top[0],testdict[top[0]])
    return top[0]


def solve(masterword):
    wordlist = [x for x in words]
    current_guess = 'toeas'#get_best_word(wordlist)
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

solve('favor')
'''
hardwords = {}

for i in range(500):
    wordle = random.choice(words)
    print('-',wordle,'-')
    hardwords[wordle] = solve(wordle)
    print()


for x in hardwords:
    if hardwords[x]>=6: print(x,hardwords[x])

print(sum(hardwords.values())/500)'''