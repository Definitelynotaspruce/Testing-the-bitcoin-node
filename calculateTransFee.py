from bitcoin.rpc import RawProxy

p = RawProxy()

txid = raw_input("Input your transactionID (just type \'no\' if you dont want to) -> ")
if txid == "no":
	txid = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"

tx_fee = 0
tx_input = 0
tx_output = 0

#decoce the transaction
raw_tx = p.getrawtransaction(txid)
decoded_tx = p.decoderawtransaction(raw_tx)

# calculate in value
for input in decoded_tx['vin']:
        tx_prev =  input['txid']
	tx_prev_index  = input['vout']
	# get into prev transaction
	tx_prev_decoded = p.decoderawtransaction(p.getrawtransaction(tx_prev))
	tx_input = tx_input + tx_prev_decoded['vout'][tx_prev_index]['value']

print("Transaction input", tx_input)

#  calculate out value
for output in decoded_tx['vout']:
	tx_output = tx_output + output['value']

print("Transaction output ", tx_output)

tx_fee = tx_input - tx_output

print("Transaction fee is ", tx_fee)	
