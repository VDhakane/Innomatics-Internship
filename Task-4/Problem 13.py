def minion_game(string):
    v= 'AEIOU'
    S_score, K_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in v:
            K_score += score
        else:
            S_score += score
    if S_score == K_score:
        print('Draw')
    if S_score > K_score:
        print('Stuart {}'.format(S_score))
    if S_score < K_score:
        print('Kevin {}'.format(K_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)
