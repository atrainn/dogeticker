#!/usr/bin/python
import urllib

url = 'https://www.dogeapi.com/wow/v2/?a=get_info'

class getdoge:
	def getvalue(self):
		feed = urllib.urlopen(url)
		var1 = feed.read()
		return var1
        
        
#Gets current doge values and returns it as var1

	def singledoge(self):
		rawval = str(getdoge().getvalue())
		removejunk = rawval.split('"doge_usd":')
		singleval  = removejunk[1].split(",")
		return singleval[0]

#gets current doge value and strips out all but the single doge value
#str converts the return to a string
	
	def dogemil(self):
		singdoge = float(getdoge().singledoge())
		mil = singdoge*1000000		
		return mil

#gets 1 doge returns it as 1mil
#not currently used