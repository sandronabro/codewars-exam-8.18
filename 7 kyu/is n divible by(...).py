def is_divisible(n, *divisor):
    if not divisor:
        return True
    
    for x in divisor:
        if n % x != 0:
            return False
    return True
    