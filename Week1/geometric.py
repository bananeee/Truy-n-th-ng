import math

def prob(n, p):
    """

    Args:
        n (int): number of trials
        p (float): probability of success on a single trial

    Returns:
        float: geometric probability
    """
    return pow(1 - p, n -1) * p

def infoMeasure(n, p):
    """

    Args:
        n (int): number of trials
        p (float): probability of success on a single trial

    Returns:
        float: amount of information that symbol caries
    """
    return - math.log2(prob(n, p))

def sumProb(N, p):
    """
    N tiến đến vô cùng thì sumProb tiến tới 1, vì tổng xác xuất của tất cả các symbol = 1
    Args:
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: sum of geometric probability of symbols from 1 to N
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    """
    Giá trị entropy của nguồn tin geometric tiến tới 2 khi p = 1/2
    Args:
        N (int): number of symbols
        p (float): probability of success on a single trial

    Returns:
        float: approximate entropy of a geometric information source
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p) * infoMeasure(i, p)
    return sum



print(prob(10, 0.6))
#output 0.00015728640000000008

print(infoMeasure(10, 0.6))
#output 12.634318448152467

print(sumProb(100, 0.6))
#output 1.0

print(approxEntropy(100, 0.6))
#output 1.6182509907577813

print(approxEntropy(100, 0.5))
#output 1.9999999999999998 ~ 2