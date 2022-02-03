import json
from statistics import stdev
import random

english_words_lower_alpha_set = json.loads(open("words3.txt").readline())

word_length = 5

words = [x for x in filter(lambda x: len(x)==word_length, english_words_lower_alpha_set)]

def get_similarity(realword, testword):
    result = ['','','','','']
    for i, letter in enumerate(testword):
        if letter == realword[i]: result[i] = 'G'
        if letter not in realword: result[i] = '_'

    for i, letter in enumerate(testword):
        if result[i]!='': continue

        if len([x for x in realword if x==letter]) > len([i for i in range(word_length) if result[i] in ['G','Y'] and testword[i]==letter]):
            result[i] = 'Y'
        else: result[i] = '_'

    return "".join(result)

def get_score(wordlist, testword):
    results = {}

    for realword in wordlist:
        x = get_similarity(realword, testword)
        if x not in results: results[x]=0
        results[x]+=1

    results2 = list(results.values())

    score = max(results2)
    if testword in wordlist: score -= 0.1
    return score

def get_best_words(wordlist):
    if len(wordlist)<=2: return wordlist

    testdict = {}

    print('loading...\n[',end='')
    x=1

    for i, word in enumerate(words):
        testdict[word]=get_score(wordlist,word)

        if i/len(words)>=x/10 and (i-1)/len(words)<x/10:
            print('#',end='',flush=True)
            x+=1
        
    print(']')

    top = sorted(sorted(testdict.keys()),key=lambda x:testdict[x])

    return top


def solve():
    wordlist = [x for x in words]
    current_guess = 'toeas'
    x = 0
    i=1
    while True:
        print('to guess:',current_guess)
        print('result:   ',end='',flush=True)
        pattern = input()

        if pattern != "":
            #print(i,current_guess,pattern)
            if pattern=='G'*word_length:
                print('SOLVED')
                return i

            wordlist = [x for x in wordlist if get_similarity(x, current_guess)==pattern]
            print('words remaining:',len(wordlist))
            print('-'*20)
            best_words = get_best_words(wordlist)
            current_guess = best_words[x]
            i+=1
            x=0
        else:
            x+=1
            current_guess = best_words[x]

solve()