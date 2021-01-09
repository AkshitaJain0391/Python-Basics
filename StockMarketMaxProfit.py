#Stock Market Maximum Profit
def stockPicker(shareValue):
    tempArray=[]
    for i in range(len(shareValue)-1):
        diff = shareValue[i+1] - shareValue[i]
        if (diff > 0):
            tempArray.append(shareValue[i])
            tempArray.append(shareValue[i+1])
    print(tempArray)
    if max(tempArray) - min(tempArray) >0 :
        MaxProfit = max(tempArray) - min(tempArray)
    else:
        MaxProfit = -1
    return MaxProfit

print(stockPicker([14,30,24,32,35,30,40,38,15]))

#Another Method
# def stockPicker1(shareValue):
#     maxProfit = 0
#     for i in range(1,len(shareValue)-1):
#         if (shareValue[i]-min(shareValue[0:i]) > maxProfit):
#             maxProfit = shareValue[i]-min(shareValue[0:i])
#
#     if (maxProfit<=0) :
#         maxProfit = -1
#     return maxProfit
#
# print(stockPicker1([44,30,24,32,35,30,40,38,15]))
