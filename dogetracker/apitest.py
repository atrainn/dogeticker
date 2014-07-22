import urllib

url = 'https://www.dogeapi.com/wow/v2/?a=get_info'

class GetDoge:
    def GetVal(self):
        feed = urllib.urlopen(url)
        var1 = feed.read()
        return var1

if __name__ == "__main__":
    print str(GetDoge().GetVal())