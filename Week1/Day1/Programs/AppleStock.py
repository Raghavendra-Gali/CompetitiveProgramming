def get_max_profit(stock_prices):

    # Calculate the max profit
    if len(stock_prices)<2:
        raise valueError("Need atleast two stock prices!!")
    mn = stock_prices[0]
    mx = stock_prices[1]-mn
    for i in range(1,len(stock_prices)):
        trending_price = stock_prices[i]
        salable_price = trending_price - mn
        mx = max(mx,salable_price)
        mn = min(mn,trending_price)
    return mx 
