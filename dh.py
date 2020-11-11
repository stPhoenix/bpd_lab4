#-*- coding: utf8 -*-
from math import gcd
from random import randint

class DH():
    _bytes = 16#max key length

    def __init__(self):
        super().__init__()

    def generate_keys(self):
        Q = self.get_simple_number()
        A = 0
        roots = self.primRoots(Q)
        for i in range(Q):
            n = randint(0, len(roots)-1)
            if n < Q:
                A = n
                break
        
        Xb = randint(1,Q)
        Yb = pow(A, Xb, Q)

        Xc = randint(1,Q)
        Yc = pow(A, Xc, Q)

        return {'Q': Q, 'Xb': Xb, 'Xc': Xc, 'Yb': Yb, 'Yc': Yc}

    def calculate_share_secret_key(self, x, y, q):
        return pow(y, x, q)
    
    def get_simple_number(self):#Find simple number for key generation
        binary = ''.join(['1' for x in range(self._bytes)])
        maxNumber = int(binary, 2)
        for i in range(0, maxNumber):
            randomNumber = randint(int(maxNumber/2), maxNumber)
            if self.checkSimple(randomNumber): return randomNumber
        raise ValueError("Can't find simple number")
    
    def checkSimple(self, n):
        for i in range(2, 256):
            if i == n: return True
            if (n%i) == 0: return False
        return True
    
    def primRoots(self, modulo):
        coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
        return [g for g in range(1, 50) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]




if __name__ == "__main__":
    n = DH().get_simple_number()
    print(n)
    keys = DH().generate_keys()
    print(keys)
    key = DH().calculate_share_secret_key(keys['Xb'], keys['Yc'], keys['Q'])
    print(key)