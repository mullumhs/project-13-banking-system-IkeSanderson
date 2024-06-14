import random
def get_int(message):
    
    while True:
        try:
            i = input(message)
            i = int(i)
            return i
        except:
            print("Not Digit")
            continue

def print_debug(enabled, message):
    if enabled:
        print(message)

def get_password(message):
    d1 = random.randint(1,26)
    d2 = random.randint(1,26)
    d3 = random.randint(1,26)
    d4 = random.randint(1,26)
    
    s1 = str(d1)
    s2 = str(d2)
    s3 = str(d3)
    s4 = str(d4)
    password = s1 + s2 + s3 + s4
    n_a = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    } 

    print(n_a[d1], n_a[d2], n_a[d3], n_a[d4])
    
    attempt = input(message)
    if attempt == password:
        return True
    else:
        return False
