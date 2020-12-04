# Testing-the-bitcoin-node
Some code to play with VU bitcoin node and transactions

## Goals

1. Calculate fee of manualy specified transaction
2. Manually validate hash of specified block 

**To run the code you must have *python-bitcoinlib* installed on your device.**

## Calculation of transaction fee
1. Run *caclculateTransFee.py* 
2. Enter transaction ID you want to inspect (or just type *no*, then the default value will be used)
3. Enjoy

Example:
```bash
user:/your/path$ python calculateTransFee.py

Input your transactionID (just type 'no' if you dont want to) -> 4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d
('Transaction input', Decimal('94504.10000000'))
('Transaction output ', Decimal('94504.03465148'))
('Transaction fee is ', Decimal('0.06534852'))
```
## Check of block hash
1. Run *checkBlock.py* 
2. Enter block number you want to inspect (or just type *no*, then the default value will be used)
3. Enjoy

Example:
```bash
user:/your/path$ python checkBlock.py

Input number of your block (just type 'no' if you dont want to) -> 277316
Original hash of block nr. 277316   -> 0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4                               
Caclulated hash of block nr. 277316 -> 0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4 
Its a match!
```
### Hashing sequence (all of the variables are converted to the *little_endian* ) :
 Version 	
<br> hashPrevBlock	
<br> hashMerkleRoot
<br> Time	
<br> Bits
<br> Nonce

# My final words
+ Thank you [NeonRice](https://github.com/NeonRice) for company while programming 🍙

 ## <i>Releases</i>
 
[**[v0.1]**](https://github.com/Definitelynotaspruce/Testing-the-bitcoin-node/releases/tag/0.2) - first and final release

