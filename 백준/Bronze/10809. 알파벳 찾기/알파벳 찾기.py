import string

s = list(input())

def get_idx(word):
    result = [-1]*len(string.ascii_lowercase)
    
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        # 아스키코드화해서 - 97
        
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))
    
get_idx(s)