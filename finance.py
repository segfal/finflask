



import yfinance as yf

import json 




class Stock:
    def __init__(self,ticker):
        self.name = ticker
        self.ticker = yf.Ticker(self.name)
        self.history = self.ticker.history(period="3mo")
        self.company_name = self.ticker.info['longName']
        self.company_nickname = self.ticker.info['shortName']
        self.price = 0
        #convert df to dict
        self.dftodict = self.history.to_dict('index')
        #print the index of df
        self.dfindex = self.history.index
        #print(dfindex)
        self.dfindex = self.dfindex.strftime('%Y-%m-%d').tolist()
        self.close = self.history['Close'].tolist()
        self.high = self.history['High'].tolist()
        self.low = self.history['Low'].tolist()
        self.open = self.history['Open'].tolist()
        self.volume = self.history['Volume'].tolist()
        self.Close = []
        self.High = []
        self.Low = []
        self.Open = []
        self.Volume = []
        self.days = len(self.close)
        self.table = {}
        self.info = []
        
        
        
    def toJson(self):
        
        for i in range(self.days):
            #self.Close.append({'date':self.dfindex[i],'value':self.close[i]})
            #self.Open.append({'date':self.dfindex[i],'value':self.open[i]})
            #self.High.append({'date':self.dfindex[i],'value':self.high[i]})
            #self.Low.append({'date':self.dfindex[i],'value':self.low[i]})
            #self.Volume.append({'date':self.dfindex[i],'value':self.volume[i]})
            self.info.append({
                'date':self.dfindex[i],
                'close':round(self.close[i],2),
                'open':round(self.open[i],2),
                'high':round(self.high[i],2),
                'low':round(self.low[i],2),
                'volume':self.volume[i]    
            })
            
            
        
        self.table["ticker"] = self.name.upper()
        self.table["price"] = self.price
        #self.table["close"] = self.Close
        #self.table["open"] = self.Open
        #self.table["high"] = self.High
        #self.table["low"] = self.Low
        #self.table["volume"] = self.Volume
        self.table["info"] = self.info
        self.table["days"] = self.days
        self.table["name"] = self.company_name
        
        
            
            
        
        
        return json.dumps(self.table)
    



#Apple = Stock("AAPL")
#print(Apple)
#print(Apple.toJson())



