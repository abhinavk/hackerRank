# HackerRank - Algorithms - Arrays and Sorting
# Game of Rotation

def get_result(total_blocks, values):
    run_sum = 0
    total_sum = sum(values)
    for i,j in enumerate(values):
        run_sum += (i+1)*values[i]
    max_sum = run_sum
    for i in range(0,total_blocks-1):
        run_sum = run_sum - total_sum + values[i]*total_blocks
        if run_sum > max_sum:
            max_sum = run_sum
    return max_sum


if __name__ == '__main__':
    n = int(input())
    v = [int(x) for x in input().split(' ')]
    print(get_result(n,v))
