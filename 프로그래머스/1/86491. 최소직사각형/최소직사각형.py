def solution(sizes):
    
    sorted_sizes = [sorted(arr) for arr in sizes]
    
    max_row = 0
    max_column = 0
    
    for i in range(len(sorted_sizes)):
        if max_row <= sorted_sizes[i][0]:
            max_row = sorted_sizes[i][0]
        
        if max_column <= sorted_sizes[i][1]:
            max_column = sorted_sizes[i][1]
    
    return max_row * max_column