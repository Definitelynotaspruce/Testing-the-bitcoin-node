from bitcoin.rpc import RawProxy
import hashlib

p = RawProxy()

# function to convert to the little endian from the internet
def toLittleEndian(input):
    byteArr = bytearray.fromhex(input)
    byteArr.reverse()
    return ''.join(format(x, '02x') for x in byteArr)

# manually calculate hash of the block
def getBlockHash(blockheight, p):
    blockHash = p.getblockhash(int(blockHeight))
    blockHeader = p.getblockheader(blockHash)

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
    calculatedHash = toLittleEndian(hashlib.sha256(hashlib.sha256(headerBinary).digest()).hexdigest())
    if blockHash == calculatedHash:
        return True
    else:
        return False

blockhash = p.getblockhash(blockheight)
blockheight = int(raw_input('Input number of your block (just type \'no\' if you dont want to) ->'))
print("Original hash of block nr. ", blockheight, "-> ", blockhash)
caclulatedHash = getBlockHash(blockheight)
print("Caclulated hash of block nr. ", blockheight, "-> ", calculatedHash)
if blockhash == calculatedHash:
    print("Its a match")
else:
    print("Oh no")
