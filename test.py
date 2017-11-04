import lib.bitcoin as bitcoin
import lib.blockchain as bc
import lib.simple_config as sc
import sys

config = sc.SimpleConfig()
testBlockchain = bc.Blockchain(config, 0, None)

# read csv (height,time,bits) data from file
with open("testdata/testdata.1.txt") as f:
	header_hash = bitcoin.GENESIS
	for line in f:
		[ height, time, bits ] = line.rstrip('\n').split(",")
		#sys.stdout.write("%s - %s - %s: " % (height, time, bits))
		header = {
			'block_height': int(height),
			'version': 0,
			'prev_block_hash': header_hash,
			'merkle_root': '0123456789012345678901234567890123456789012345678901234567891234',
			'timestamp': time,
			'bits': int(bits,16),
			'nonce': '0123456789'
		}
		header_hash = bc.hash_header( header ) # used in next round as header.prev_block_hash
		if int(height) <= 10:
			a=1
			#print " not validating due to mtp_6blocks problem"
		else:		
			if testBlockchain.can_connect( header, True, True ):
				a=1
				#print "valid"
			else:
				print "can't connect header at height", header.get('block_height')
				sys.exit(1)
		testBlockchain.save_header( header )

print "read and verified successfully size: %i" % ( testBlockchain.size() )
sys.exit(0)
