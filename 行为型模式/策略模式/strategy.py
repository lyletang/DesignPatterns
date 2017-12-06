# -*- coding: utf-8 -*-
# author: lyletang
# date: 2017-12-06
# describe: 实现两种不同算法来检测一个单词中所有字符唯一性


import time


SLOW = 3    # 单位为秒
LIMIT = 5   # 字符数
WARNING = 'too bad, you picked the slow algorithm :('

def pairs(seq):
    """返回所有相邻字符对的一个序列seq"""
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    """如果字符串所有字符唯一，则返回True；否则返回False。
       为演示策略模式，假设这个算法的伸缩性不好，对应不超过5个字符的字符串才能工作良好。对于更长的字符串，通过插入一条sleep语句来模拟速度减缓。
    """
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    strStr = sorted(s)
    for (c1, c2) in pairs(strStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    """消除排序的需要，使用一个集合来实现算法。
       如果正在检测的字符已经被插入到集合中，则意味着字符串中并非所有字符都是唯一的。
       虽然没有伸缩性问题，但检测短字符串的性能比allUniqueSort()更差。
    """
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')

            if word == 'quit':
                print('bye')
                return
            
            strategy_picked = None
            strategies = { '1': allUniqueSet, '2': allUniqueSort }
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))
            print()
    

if __name__ == '__main__':
    main()
