import sys

class Solulu:
    def __init__(self):
        if len(sys.argv) > 1:
            self.s = sys.argv[1]
        else:
            self.s = ""
    
    def romanToInt(self):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        if self.s:
            for i in range(0, len(self.s) - 1):
                if roman[self.s[i]] < roman[self.s[i+1]]:
                    z -= roman[self.s[i]]
                else:
                    z += roman[self.s[i]]
            z += roman[self.s[-1]]
        return z
    
if __name__ == "__main__":
    solulu = Solulu()
    result = solulu.romanToInt()
    print(result)