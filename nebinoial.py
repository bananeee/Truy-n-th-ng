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
    return math.comb(r - 1, n - 1) * pow(p, r) * pow(1 - p, n - r)

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
    for i in range(1, N):
        if (i >= r):
            sum += prob(r, i, p)
    return sum

def approxEntropy(N, p, r):
    """
    
    Args:
        r (int): number of success trials
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: approximate entropy of a binomial information source
    """
    sum = 0
    for i in range(1, N):
        if (i >= r):
            sum += prob(r, i, p) * infoMeasure(r, i, p)
    return sum



print(prob(4, 10, 0.6))
#output 0.11147673600000003

print(infoMeasure(4, 10, 0.6))
#output 3.1651854283228755

print(sumProb(100, 0.6, 8))
#output 1.0

print(approxEntropy(100, 0.6, 8))
#output 4.339359847918865

print(approxEntropy(100, 0.5, 8))
#output 4.369011409223017 