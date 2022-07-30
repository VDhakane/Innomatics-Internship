if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    lists = [] 
    for i in integer_list:
        lists.append(i)
        
    print(hash(tuple(lists)))
