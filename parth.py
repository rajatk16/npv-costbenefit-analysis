import pandas as pd
df1 = pd.DataFrame({'NPV':[7000, 0, 0, 0], 'cash flow':[4200,5300,6100, 7400], 'r' : [0.14,0.14,0.14,0.14]})
print(df1) 
labels = ['NPV', 'cash flow', 'r']
def n(NPV, cash_flow):
  print(pd.Series(df['cash flow']) *  pd.Series(df['r']))
  l = []
  value = []
  cash_flow = [4200, 5300, 6100, 7400]
  NPV = 7000    
def n(NPV, cash_flow):
  for i in range(0,n):
    i += 1
    x = ((1 + df1['r'][0]) ** (-n))
    l.append(x)
    value = ([k * cash_flow[i] for i, k in enumerate(l)])
    M =   n + ((NPV - value[i]) / value[(i + 1)]) 
    if M >= 7:
      print(n)
