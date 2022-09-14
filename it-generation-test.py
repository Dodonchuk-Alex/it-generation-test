bitcoin_price = int (input ("Please, enter Bitcoin price: \n"))
if bitcoin_price <= 0:
    print ("Bitcoin cource is not correct. Please enter correct cource" )
else:
    amount_of_dollars = float (input ('How many dollars do you want to exchange for Bitcoin? \n'))
    if amount_of_dollars <= 0:
        print ("Amount of dollars is not correct. Please input correct amount")
    else:
        amount_bitcoin = amount_of_dollars / bitcoin_price
        amount_bitcoin = round (amount_bitcoin, 7)
        print (f"For $ {amount_of_dollars} you can buy {amount_bitcoin} BTC.\nThank you for using my service.")
