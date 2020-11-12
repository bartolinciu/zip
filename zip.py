#!/usr/bin/python3
import pyzipper
import sys
import os

if len(sys.argv) < 4:
	print( "usage:", sys.argv[0], "<target> <source> <password>" )
	quit()

with pyzipper.AESZipFile( sys.argv[1], "w", compression = pyzipper.ZIP_LZMA ) as zf:
	zf.setpassword( bytes(sys.argv[3], "UTF-8") )
	zf.setencryption( pyzipper.WZ_AES, nbits = 128 )
	path = os.walk(sys.argv[2])
	for root, directories, files in path:
		for directory in directories:
			zf.writestr( root+"\\"+directory+"\\", "" )
		for file in files:
			fname = root + "\\" + file
			zf.write( fname )
	