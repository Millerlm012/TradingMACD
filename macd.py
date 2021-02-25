'''
    Goal: create a program that is able to perform trades following the macd cross over strat.
    Strategy: Buy Signal
    - macd line crosses above the signal line
    - that crossover will need to take place some % underneath the 0 line of the histogram
    - finally this will only happen if the market is above the 200 ema (*uptrend)
    (WOULD LIKE TO JUST GET LONG TAKEN CARE OF FIRST BUT | for shorting the stock it will all be vice versa)

    Notes:
    - macd can be calculated by subtracting the 26 period EMA from the 12 period EMA
    - signal line is a 9 day ema
'''


def PerformCalculations():
    # determines if stock has buy signal

    def Uptrend():
        # market for stock is above the 200 ema (*uptrend)
        '''
        # maybe make it be greater than 200ema in a range / %
        if minute_low > 200ema:
            return true
        else:
            return false
        '''
        pass

    def CrossOver():
        # stock had macd line cross and it occurred below 0 | true else: false
        '''
        macd = 
        '''
        pass

    pass


def RetrieveStockData():
    # retrieve stock data to be processed on minutely basis
    pass


def PurchaseStock():
    # purchasing stock if buy signal returns true
    pass
