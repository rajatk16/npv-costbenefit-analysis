import numpy as np
import pandas as pd
import math
print("""Financial Information and Analytics\n
Assignment 4\n
NPV and Cost Benefit Analysis\n
By Rajat Sudagade (UTD ID 2021449378)\n""")
# Financial Information and Analytics
# Assignment 4
# By Rajat Sudagade (UTD ID: 2021449378)

# Part 1: Net Present Value
print("Part 1: Net Present Value (NPV)")
# Question 1: What is the payback period for the following set of cash flows?
def payback(cashflows):
  years=len(cashflows)
  index = []
  index.extend(range(years))
  cumulative = []
  for year in range(years):
    if year == 0:
      cumulative.append(cashflows[year])
    else:
      value = cumulative[year-1] + cashflows[year]
      cumulative.append(value)
  for year in range(years):
    if cumulative[year] >= 0:
      value = (year-1) + ((-cumulative[year-1])/cashflows[year])
      break
  print('The given set of cash Flows is:')
  d = {'Cash Flows': pd.Series(cashflows, index=index), 
       'Cumulative': pd.Series(cumulative, index=index)}
  df = pd.DataFrame(d)
  print(df)
  print("The payback period for this set of cash flow is {:,.2f} years".format(value))
print("Question 1:")
payback(cashflows=[-3300,2500,1700,2900,2300])

# Question 2
def payback2(initialCost, cashInflows, years):
  cashFlows=list()
  cumulative=list()
  try:
    for year in range(years):
      if year == 0:
        cashFlows.append(initialCost)
        cumulative.append(initialCost)
      else:
        cashFlows.append(cashInflows)
        present = cumulative[year - 1] + cashInflows
        cumulative.append(present)
    for year in range(years):
      if cumulative[year] >= 0:
        value = (year-1) + ((-cumulative[year-1])/cashFlows[year])
        break
    d = {'Cash Flows' : pd.Series(cashFlows, index=[0,1,2,3,4,5,6,7,8,9,10,11]), 'Cumulative' : pd.Series(cumulative, index=[0,1,2,3,4,5,6,7,8,9,10,11])}
    df = pd.DataFrame(d)
    print("The Cash Flow Table is:\n {:}".format(df)) 
    print("For the initial cost of ${:,.0f}, the project payback period is ".format(-initialCost) + str(value) + " years \n")
  except UnboundLocalError:
    print('The Payback period for this project is greater than the term of the project\n')
print("\nQuestion 2.a")
payback2(initialCost=-2960,cashInflows=740, years=12)
print("\nQuestion 2.b")
payback2(initialCost=-4366,cashInflows=740, years=12)
print("\nQuestion 2.c")
payback2(initialCost=-8880,cashInflows=740, years=12)

# Question 3 
def discounted(cashInflows, discountRate, initialCost):
  period=len(cashInflows)
  index = []
  index.extend(range(period))
  try:  
    pvf = []
    dcf = []
    cdcf = [initialCost]
    for i in range(period):
      value = 1/((1 + discountRate)**(i))
      pvf.append(value)
    for i in range(period):
      value = cashInflows[i] * pvf[i]
      dcf.append(value)
    for i in range(1,period):
      value = cdcf[i-1] + dcf[i]
      cdcf.append(value)
    for i in range(len(cdcf)):
      if cdcf[i] >= 0:
        discountedPayback = (i-1) + (-cdcf[i-1]/dcf[i])
        break
    d = {'Cash Flows' : pd.Series(cashInflows, index=index), 
         'PVF' : pd.Series(pvf, index=index), 
         'DCF' : pd.Series(dcf, index=index), 
         'CDCF' : pd.Series(cdcf, index=index)}
    df = pd.DataFrame(d)  
    print("The Cash Flow Table for this investment project is given by:")
    print(df)
    print("The Discounted Payback period is: {:,.2f} years\n".format(discountedPayback))
  except UnboundLocalError:
    print('The Discounted Payback period longer than the investment period\n')
print("Question 3:")
discounted(cashInflows=[-7000, 4200, 5300, 6100, 7400], discountRate=0.14, initialCost=-7000)

# Question 4:
print("Question 4.a")
discounted(cashInflows=[-14400, 3300, 3300, 3300, 3300, 3300, 3300], discountRate=0, initialCost=-14400)
print("Question 4.b")
discounted(cashInflows=[-14400, 3300, 3300, 3300, 3300, 3300, 3300], discountRate= 0.04, initialCost=-14400)
print("Question 4.c")
discounted(cashInflows=[-14400, 3300, 3300, 3300, 3300, 3300, 3300], discountRate= 0.19, initialCost=-14400)

# Question 5:
def net_present(rr, years, cashFlows):
  presentValue = []
  index = []
  index.extend(range(years))
  npv = 0 
  for year in range(years):
    value = cashFlows[year]/((1 + (rr/100))**(year))
    presentValue.append(value)
  print("For required return of {:,.2f}%, the cash flow table is:".format(rr))
  d = {'Cash Flow': pd.Series(cashFlows, index=index), 'Present Value': pd.Series(presentValue, index=index)}
  df = pd.DataFrame(d)
  print(df)
  for year in range(years):
    npv += presentValue[year] 
  print("The Net Present value of this project is: ${:,.2f} \n".format(npv))
print("Question 5.a")
net_present(rr=11, years = 4, cashFlows=[-30000, 23000, 13300, 11000])
print("Question 5.b")
net_present(rr=40, years = 4, cashFlows=[-30000, 23000, 13300, 11000])

# Question 6:
print("Question 6.a")
net_present(rr=11, years = 10, cashFlows=[-14000,3000,3000,3000,3000,3000,3000,3000,3000,3000])
print("Question 6.b")
irr = np.irr([-14000,3000,3000,3000,3000,3000,3000,3000,3000,3000])
print("The Internal Return Rate(IRR) is: {:,.2f}% \n".format(irr * 100))

# Question 7
print("Question 7")
cashFlows=[-7951,4300,3300,5400]
index = []
index.extend(range(len(cashFlows)))
print("The Given Cash Flow table is:")
d = {'Cash Flow': pd.Series(cashFlows, index=index)}
df =pd.DataFrame(d)
print(df)
irr = np.irr(cashFlows)
print("The Internal Return Rate(IRR) is: {:,.2f}%\n".format(irr * 100))

#Question 8
print("Question 8.a")
net_present(rr=0, years=4, cashFlows=[-8600, 4800, 5600, 5900])
print("Question 8.b")
net_present(rr=10, years=4, cashFlows=[-8600, 4800, 5600, 5900])
print("Question 8.c")
net_present(rr=18, years=4, cashFlows=[-8600, 4800, 5600, 5900])
print("Question 8.d")
net_present(rr=23, years=4, cashFlows=[-8600, 4800, 5600, 5900])

# Question 9:
cashFlowsA = [-36700, 19040, 14540, 12040, 9040]
cashFlowsB = [-36700, 6580, 13080, 19580, 23580]
cashFlowsBA = []
print("Question 9.a")
irrA = np.irr(cashFlowsA)
print("The IRR for Project A is {:,.2f}%\n".format(irrA * 100))
years = 5
print("Question 9.b")
irrB = np.irr(cashFlowsB)
print("The IRR for Project B is {:,.2f}%\n".format(irrB * 100))
print("Question 9.c")
net_present(rr=15, years=5, cashFlows=[-36700, 19040, 14540, 12040, 9040])
print("Question 9.d")
net_present(rr=15, years=5, cashFlows=[-36700, 6580, 13080, 19580, 23580])
print("Question 9.e")
for year in range(1,years):
  value = cashFlowsB[year] - cashFlowsA[year]
  cashFlowsBA.append(value)
indifferent = np.irr(cashFlowsBA)
print("The company will be indifferent between these two projects when the Discount Rate is {:,.2f}%\n".format(indifferent * 100))
  
# Question 10:
def profitability(cashFlow, discountRate):
  numerator = 0
  for i in range(1, len(cashFlow)):
    numerator += cashFlow[i]/((1 + (discountRate / 100))**(i))
  profitIndex = numerator / (-cashFlow[0])
  print("The Profitability Index for the given Cash Flow Table at discount rate of {:}% is: {:,.2f}\n".format(discountRate, profitIndex))
print("Question 10.a")
profitability(cashFlow=[-7600, 5300, 2700, 3500], discountRate=11)
print("Question 10.b")
profitability(cashFlow=[-7600, 5300, 2700, 3500], discountRate=18)
print("Question 10.c")
profitability(cashFlow=[-7600, 5300, 2700, 3500], discountRate=24)

# Question 11:
print("Question 11.a:")
payback(cashflows=[-218744,29300,51000,51000,424000])
print("\nQuestion 11.b:")
payback(cashflows=[-14887,4036,8738,13211,8514])
print("\nQuestion 11.c")
discounted(cashInflows=[-218744,29300,51000,51000,424000], discountRate=0.06, initialCost=-218744)
print("Question 11.d")
discounted(cashInflows=[-14887,4036,8738,13211,8514], discountRate=0.06, initialCost=-14887)
print("Question 11.e")
net_present(rr=6, years=5, cashFlows=[-218744,29300,51000,51000,424000])
print("Question 11.f")
net_present(rr=6, years=5, cashFlows=[-14887,4036,8738,13211,8514])
print("Question 11.g")
irr = np.irr([-218744,29300,51000,51000,424000])
print("The Internal Return Rate(IRR) is: {:,.2f}% \n".format(irr * 100))
print("Question 11.h")
irr = np.irr([-14887,4036,8738,13211,8514])
print("The Internal Return Rate(IRR) is: {:,.2f}% \n".format(irr * 100))
print("Question 11.i")
profitability(cashFlow=[-218744,29300,51000,51000,424000], discountRate=6)
print("Question 11.j")
profitability(cashFlow=[-14887,4036,8738,13211,8514], discountRate=6)

# Question 12:
def mirr3(cashFlows, interestRate):
  years = len(cashFlows)
  cashOutFlow = cashFlows[-1]
  pv = cashOutFlow/((1 + (interestRate/100))**(len(cashFlows)-1))
  mcf = cashFlows[0]+pv
  cash = []
  cash.append(mcf)
  for i in range(1, years-1 ):
    cash.append(cashFlows[i])
  mirr = np.irr(cash)
  print("The MIRR using discounting approach is: {:,.2f}%".format(mirr*100))
  power = years - 2
  cashFlow = []
  value = 0
  cashFlow.append(cashFlows[0])
  for i in range(1, years-1):
    value += cashFlows[i]*((1 + (interestRate/100))**(power))
    power -= 1
  value += cashFlows[years-1]
  for i in range(1,years-1):
    cashFlow.append(0)
  cashFlow.append(value)
  mirr = np.irr(cashFlow)
  print("The MIRR using Reinvestment approach is: {:,.2f}%".format(mirr*100))
  value = 0
  power = years - 2
  cashFlow = []
  cashFlow.append(mcf)
  for i in range(1,years-1):
    cashFlow.append(0)
  for i in range(1, years-1):
    value += cashFlows[i]*((1 + (interestRate/100))**(power))
    power -= 1
  cashFlow.append(value)
  mirr = np.irr(cashFlow)
  print("The MIRR using combination approach is: {:,.2f}%".format(mirr*100))
print("Question 12:")
mirr3(cashFlows=[-29800,12000,14700,16600,13700,-10200],interestRate=9)

# Question 13:
print("\nQuestion 13:")
mirr3(cashFlows=[-13200,6100,6700,6200,5100,-4500], interestRate=9)

# Question 14:
print("\nQuestion 14.a:")
cashflows = [-64300,-30300,-48300]
irr = np.irr(cashflows)
print("The IRR of this project is: {:,.2f}%\n".format(irr*100))
print("Question 14.b:")
net_present(rr=10.5, years = 3, cashFlows=[-64300, -30300,-48300])
print("Question 14.c:")
net_present(rr=0, years=3, cashFlows=[-64300, -30300,-48300])
print("Question 14.d:")
net_present(rr=21, years=3, cashFlows=[-64300, -30300,-48300])

print("Part 2: Cost Benefit Analysis\n")
# Question 1
print("Question 1:")
print("Cost Benefit Analysis is a systematic method of calculating the benefits and costs of a course of action in a given situation. It gives the best option that returns optimal ratio of benefits to costs, thereby solving the issue regarding opportunity cost.\n")

# Question 2
print("Question 2:")
print("While, Cost Benefit Analysis is a systematic method of calculating the benefits and costs of a course of action in a given situation, Risk benefit ratio is the ratio of the risk of an action to its potential benefits.\n")

# Question 3
def tough_one(dr, implementation_costs,recurringB):
  index = []
  years = 21
  index.extend(range(years))
  #implementation_costs = -3375000
  maintainence_costs = list()
  annual_costs = list()
  pvf = list()
  pvc = list()
  recurringBenefits = list()
  pvb = list()
  net_benefit = list()
  overall = list()
  for i in range(years):
    if i == 0:
      maintainence_costs.append(0)
      annual_costs.append(implementation_costs)
      pvf.append(1/((1+dr)**(i)))
      pvc.append(annual_costs[i]*pvf[i])
    else:
      maintainence_costs.append(-260000)
      annual_costs.append(maintainence_costs[i])
      pvf.append(1/((1+dr)**(i)))
      pvc.append(annual_costs[i]*pvf[i])
  for i in range(years):
    if i == 0:
      recurringBenefits.append(0)
      pvb.append(recurringBenefits[i]*pvf[i])
      net_benefit.append(pvb[i]+pvc[i])
      overall.append(net_benefit[i])
    else:
      recurringBenefits.append(recurringB)
      pvb.append(recurringBenefits[i]*pvf[i])
      net_benefit.append(pvb[i]+pvc[i])
      overall.append(net_benefit[i]+overall[i-1])
  overall = [round(i,2) for i in overall]
  pvc = [round(i,2) for i in pvc] 
  pvb = [round(i,2) for i in pvb]
  net_benefit = [round(i,2) for i in net_benefit] 
  costs = {'PVC': pd.Series(pvc, index=index),
           'PVB': pd.Series(pvb, index=index),
           'Net': pd.Series(net_benefit, index=index),
           'Overall': pd.Series(overall, index=index)}
  costs = pd.DataFrame(costs)
  print("The Net Present value with {0}% discount rate and project period of {1} years is ${2:,.2f}".format(dr*100,years-1,overall[-1]))
  sumpvc = 0
  sumpvb = 0
  for i in range(1,years):
    sumpvc -= pvc[i]
    sumpvb -= pvb[i]
  denominator = sumpvb/360
  print("Total sum of present value of costs is ${:,.2f}".format(sumpvc))
  print("Total sum of present value of costs is ${:,.2f}".format(sumpvb))
  breakeven = -sumpvc/denominator
  print('In a year of 360 days, the project will break even in {:,.2f} days'.format(breakeven))
print("Question 3:")
tough_one(dr = 0.15,implementation_costs=-3375000, recurringB=645000)
print("""EMB may implement the project as it has less than one year break-even, and revenues over the project life of 20 years are found.
If the project is continued for an infinite time, break-even period is at the end of 93rd for the period.
However, if considered the initial project cost of $3,375,000, project will never be able to generate any positive NPV.\n""")
print("Question 4:")
tough_one(dr=0.3,implementation_costs=-3375000, recurringB=645000)
print("""Therefore, EMB may implement the project as it has less than one year break even.
If the project is continued for an infinite period of time, break-even period is at the end of the 50th year of the project.
However, if considered the initial project investment of $3,375,000, project will never generate any positive NPV.\n""")
print("Question 5:")
tough_one(dr=0.15, implementation_costs=-3375000,recurringB=417500)
print("""Therefore, EMB may implement the project as it has less than one year break even.
If the project is continued for an infinite period of time, break-even period is at the end of the 91st year of the project.
However, if considered the initial project investment of $3,375,000, project will never generate any positive NPV.\n""")
print("Question 6:")
pvinvest = 3375000
maintenance = 260000
recurringBenefit = 417500
r = 0.15
years = 20
pvifa = (1 - ((1 + r)**(-years)))/r
pvrecurr = maintenance*pvifa
pvtotal = pvinvest + pvrecurr
pvinflows = recurringBenefit * pvifa
required = pvtotal
current15 = pvinflows
trialr = 0.05
trialpvifa = (1 - ((1 + trialr)**(-years)))/trialr
trialpv = recurringBenefit*trialpvifa
numerator = trialpv-pvtotal
denominator = trialpv - current15
economic = (r*100)-(((r - trialr)*100)*(numerator/denominator))
print("The Project is economically feasible at any discount rate below {:,.2f}%".format(economic))
print(trialpv)