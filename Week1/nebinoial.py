import math


def prob(r, n, p):
    """

    Args:
        r (int): number of success trials
        n (int): symbol's value
        p (float): probability of success on a single trial

    Returns:
        float: binomial probability
    """
    return math.comb(n - 1, r - 1) * pow(p, r) * pow(1 - p, n - r)


def infoMeasure(r, n, p):
    """

    Args:
        r (int): number of success trials
        n (int): symbol's value
        p (float): probability of success on a single trial

    Returns:
        float: amount of information that symbol caries
    """
    return - math.log2(prob(r, n, p))


def sumProb(N, p, r):
    """
    N tiến đến vô cùng thì sumProb tiến tới 1, vì tổng xác xuất của tất cả các symbol = 1
    Args:
        r (int): number of success trials
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: sum of binomial probability of symbols from 1 to N
    """
    sum = 0
    for i in range(r, N + 1):
        sum += prob(r, i, p)
    return sum


def approxEntropy(N, p, r):
    """
    r tiến đến càng gần N thì giá trị trung bình càng tiến tới 0.5^N
    Args:
        r (int): number of success trials
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: approximate entropy of a binomial information source
    """
    sum = 0
    for i in range(r, N + 1):
        sum += prob(r, i, p) * infoMeasure(r, i, p)
    return sum


print(prob(4, 10, 0.6))
# output 0.04459069440000002

print(infoMeasure(4, 10, 0.6))
# output 4.487113523210238

print(sumProb(100, 0.6, 8))
# output 0.9999999999999999

print(approxEntropy(100, 0.6, 8))
# output 3.5397152951580377

print(approxEntropy(100, 0.5, 10))
# output 4.150775320863947
