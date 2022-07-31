def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        dic = dict()
        print(''.join([ dic.setdefault(c, c) for c in part if c not in dic ]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
