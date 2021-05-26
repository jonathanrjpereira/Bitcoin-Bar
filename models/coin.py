import locale
from decimal import Decimal, ROUND_HALF_UP
locale.setlocale( locale.LC_ALL, '' )

class Coin:  
    def __init__(self, id, rank, symbol, name, supply, maxSupply, marketCapUsd, volumeUsd24Hr, priceUsd, changePercent24Hr, vwap24Hr, explorer): 
        self.id = id  
        self.rank = rank
        self.symbol = symbol
        self.name = name
        self.supply = supply
        self.maxSupply = maxSupply
        self.marketCapUsd = marketCapUsd
        self.volumeUsd24Hr = volumeUsd24Hr
        self.price = Decimal(priceUsd)
        self.priceRounded = self.price.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
        self.priceString = locale.currency(self.priceRounded), grouping=True, symbol=False)
        self.percentage = Decimal(changePercent24Hr)
        
        
    def to_string(self):  
        return '{0} - ${1} - {2}%'.format(self.symbol, self.priceString, round(self.percentage, 2))
