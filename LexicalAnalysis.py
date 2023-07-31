# This is a sample Python script.
import sys
import time
from multiprocessing import Process, Queue
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
now = 0
l = []
keys = []
keywords = {'begin': 1, "end": 2, "if": 3, "then": 4, "while": 5, "do": 6, "const": 7, "var": 8, "call": 9,
            "procedure": 10, "odd": 11}
keyword = {'+': 1, '-': 2, '*': 3, '/': 4, '=': 5, '#': 6, '<': 7, '>': 8, ':=': 9, '(': 10, ')': 11, ',': 12, '.': 13,
           ';': 14}
word = ['标识符', '常数', '算符和界符', '关键字']
bl = False


def scanf(line):
    global bl
    line = line.replace('\n', '')
    b2 = False
    n = line.split(" ")
    print(n)
    p = []
    for m in n:
        nw = m.split('\t')
        for w in nw:
            p.append(w)
    n = p
    sum = ""
    num = []

    for i in range(len(n)):
        if n[i] == '//':
            b2 = True
        if n[i] == '(*':
            bl = True
        if bl == False and b2 == False:
            sum += n[i]
            if n[i] != '' and n[i] != ' ':
                n[i] = n[i].replace('\t', '')
                num.append(n[i])
        if n[i] == '*)':
            bl = False
    if sum != '' and sum != " ":
        l.append(num)


def fenjie(n):
    for i in n:
        if i.isalnum():
            keys.append([i, isWhat(i)])
        else:
            left = int(0)
            right = int(0)
            while right < len(i):
                if i[right].isalnum():
                    right += 1
                else:
                    if i[right] == ':' and i[right + 1] == '=':
                        ml = 2
                    else:
                        ml = 1
                    first = i[left:right]
                    second = i[right:right + ml]
                    left = right + ml
                    right = left
                    if first != '':
                        keys.append([first, isWhat(first)])
                    if second != '':
                        keys.append([second, isWhat(second)])
                        #     print(first, isWhat(first))
                        # if second != '':
                        #     print(second, isWhat(second))


def isWhat(n):
    if n in keywords:
        return word[3], keywords[n]
    elif n in keyword:
        return word[2], keyword[n]
    elif n.isdigit():
        return word[1], int(n)
    else:
        return word[0], '-'


def outprint():
    for i in range(len(l)):
        print(l[i])


# Press the green button in the gutter to run the script.
def LexicalAnalysis():
    with open('data.txt', 'r') as f:
        scanf_lines = f.readlines()
        for i in scanf_lines:
            scanf(i)
    # outprint()
    for i in l:
        fenjie(i)
    # mp = ['const', 'limit=10;']
    # fenjie(mp)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def getkeys():
    global now
    now += 1
    if now - 1 < len(keys):
        print(keys[now - 1])
        return keys[now - 1]


def backkeys(s):
    global now
    now -= 1
    print(str(s) + "back" + str(keys[now]))


def main():
    LexicalAnalysis()
    print(keys)
    Note = open('LA.txt', mode='w')
    for i in keys:
        Note.write(str(i)+'\n')

