#주식을 사고팔기 가장 좋은 시점, 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
#[7,1,5,3,6,4] -> 5, 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.

def maxProfit(self, prices: List[int])->int:
    profit=0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
        
    return profit
