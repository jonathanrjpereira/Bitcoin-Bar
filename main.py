from services.crypto import get_token

def main():
    last_price = -1
    while True:
        coin = get_token("bitcoin")
    
        if coin.price != last_price:
            #todo something special if price changed
            print(coin.to_string())
            last_price = coin.price
        else:
            print(coin.to_string())

main()
