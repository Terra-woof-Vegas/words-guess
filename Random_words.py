import random
import sys


def random_words(filename):
    """
    读取词库文件，并选出25个词
    :param filename: 词库文件名称
    :return: 不重复的25词
    """
    wordlist = []
    f = open(filename, 'r', encoding='utf-8')
    for line in f:
        if line[0] != '#':
            wordlist.append(line.strip('\n'))
    result = random.sample(wordlist, 25)
    return result


def print_words(words):
    """
    打印词表
    :param words: 25个词
    :return: 5*5格式的词表
    """
    longest = 0
    for w in words:
        longest = max(longest, len(w))

    for i in range(25):
        if i % 5 == 4:
            print(words[i])
        else:
            cnt = 0
            for ch in words[i]:
                if not '\u4e00'<= ch <= '\u9fff':
                    cnt = cnt + 1
            if cnt == 0:
                print('{0:{1}<{2}}'.format(words[i],chr(12288),longest+1), end="")
            else:
                words[i] = words[i].ljust(len(words[i])+cnt, " ")
                print('{0:{1}<{2}}'.format(words[i],chr(12288),longest+cnt+1), end="")


