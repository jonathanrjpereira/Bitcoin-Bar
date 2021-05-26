from services.crypto import get_token
from services.led import output_msg

def main():
    last_price = -1
    while True:
        coin = get_token("bitcoin")
    
        if coin.price != last_price:
            #todo something special if price changed
            output_msg(coin.to_string())
            last_price = coin.price
        else:
            output_msg(coin.to_string())

main()
