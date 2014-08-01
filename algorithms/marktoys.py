# HackerRank - Algorithms - Arrays and Sorting
# Mark and Toys

def get_result(total_toys, budget, prices):
    toys = 0
    prices = [int(x) for x in prices]
    prices.sort()
    for i in prices:
        if i > budget:
            break
        budget -= i
        toys += 1
    return toys


if __name__ == '__main__':
    n,k = input().split(' ')
    prices = input().split(' ')
    print(get_result(int(n),int(k),prices))
