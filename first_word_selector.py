import json
from statistics import stdev
import random, math


english_words_lower_alpha_set = json.loads(open("words3.txt").readline())

word_length = 20

words = [x for x in filter(lambda x: len(x)==word_length, english_words_lower_alpha_set)]

print(len(words))

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

    #score = max(results2)
    '''scorer = (distr) => {
                let x = distr.filter(s => s!=0);
                x = x.map(a=>a/pws.length);
                x = x.map(a=>Math.log2(1/a)*a);
                return -x.reduce((a, b) => a + b, 0);
            }'''
    l = len(wordlist)
    score = -sum([math.log2(l/x)*x/l for x in results2])

    return score

def get_best_first_word(wordlist):
    testdict = {}

    print('loading...\n[',end='')
    x=1

    for i, word in enumerate(words):
        testdict[word]=get_score(wordlist,word)

        if i/len(words)>=x/20 and (i-1)/len(words)<x/20:
            print('#',end='',flush=True)
            x+=1

    print(']')

    top = sorted(testdict.keys(),key=lambda x:testdict[x])
    
    for x in top[0:10]: print(x, testdict[x])

get_best_first_word(words)