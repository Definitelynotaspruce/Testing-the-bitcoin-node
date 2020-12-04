
from bitcoin.rpc import RawProxy
import hashlib
import binascii

p = RawProxy()

# function to convert to the little endian from the internet
def toLittleEndian(input):
    byteArr = bytearray.fromhex(input)
    byteArr.reverse()
    return ''.join(format(x, '02x') for x in byteArr)

# manually calculate hash of the block
def getBlockHash(blockheight, p):
   
    blockHeader = p.getblockheader(p.getblockhash(int(blockheight)))

    hexVersion = toLittleEndian(blockHeader['versionHex'])
    previousBlockHash = toLittleEndian(blockHeader['previousblockhash'])
    merkleRoot = toLittleEndian(blockHeader['merkleroot'])
    timestamp = toLittleEndian(format(int(blockHeader['time']), 'x')) 
    bits = toLittleEndian(blockHeader['bits'])
    nonce = toLittleEndian(format(int(blockHeader['nonce']), 'x'))

    headerHex = (hexVersion +
        previousBlockHash +
        merkleRoot +
        timestamp +
        bits +
        nonce)

    headerBinary = binascii.unhexlify(headerHex)
    return toLittleEndian(hashlib.sha256(hashlib.sha256(headerBinary).digest()).hexdigest())
        
blockheight = int(raw_input('Input number of your block (just type \'no\' if you dont want to) ->'))
blockhash = p.getblockhash(blockheight)
print("Original hash of block nr. ", blockheight, "-> ", blockhash)
calculatedHash = getBlockHash(blockheight,p)
print("Calculated hash of block nr. ", blockheight, "-> ", calculatedHash)
if blockhash == calculatedHash:
    print("Its a match")
else:
    print("Oh no")
0
