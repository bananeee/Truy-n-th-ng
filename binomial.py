import math

def prob(N, n, p):
    """

    Args:
        N (int): number of trials
        n (int): symbol's value
        p (float): probability of success on a single trial

    Returns:
        float: binomial probability
    """
    return math.comb(N, n) * pow(p, n) * pow(1 - p, N - n)

def infoMeasure(N, n, p):
    """

    Args:
        N (int): number of trials
        n (int): symbol's value
        p (float): probability of success on a single trial

    Returns:
        float: amount of information that symbol caries
    """
    return - math.log2(prob(N, n, p))

def sumProb(N, p):
    """
    N tiến đến vô cùng thì sumProb tiến tới 1, vì tổng xác xuất của tất cả các symbol = 1
    Args:
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: sum of binomial probability of symbols from 1 to N
    """
    sum = 0
    for i in range(1, N):
        sum += prob(N, i, p)
    return sum

def approxEntropy(N, p):
    """
    r tiến đến càng gần N thì giá trị trung bình càng tiến tới 0.5^N
    Args:
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: approximate entropy of a binomial information source
    """
    sum = 0
    for i in range(1, N):
        sum += prob(N, i, p) * infoMeasure(N, i, p)
    return sum



print(prob(10, 4, 0.6))
#output 0.11147673600000003

print(infoMeasure(10, 4, 0.6))
#output 3.1651854283228755

print(sumProb(100, 0.6))
#output 1.0

print(approxEntropy(100, 0.6))
#output 4.339359847918865

print(approxEntropy(100, 0.5))
#output 4.369011409223017 