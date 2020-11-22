from collections import Counter
def benchmarkMatching(s):
    portfolio, benchmark = s.split(":")
    c = {}
    for s in portfolio.split("|"):
        comp, asset, amount = s.split(",")
        c[f'{comp},{asset}'] = int(amount)
    for s in benchmark.split("|"):
        comp, asset, amount = s.split(",")
        if f'{comp},{asset}' not in c:
            c[f'{comp},{asset}'] = -int(amount)
        else:
            c[f'{comp},{asset}'] -= int(amount)
    c = sorted(c.items())
    for key, value in c:
        if value != 0:
            print(f'{"BUY" if value < 0 else "SELL"},{key},{abs(value)}')
          
  
        


s = "Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15"
outputexp = "SELL,Google,STOCK,5 BUY,Vodafone,STOCK,5"

benchmarkMatching(s)

