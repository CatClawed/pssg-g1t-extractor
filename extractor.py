###################################################################################################
#
# Extracts G1T files from a PSSG.
#
# Just reads all files in the directory, finds all PSSG files, extracts. Not a fancy tool, do not
# use on PSSG.gz files, it will probably find them and choke.
#
###################################################################################################

import struct
import glob
import os

ls = os.listdir(os.getcwd())

for f in ls:
	if '.PSSG' in f.upper():
		print(f)
		with open(f, mode='rb') as file:
			filecontent = file.read()
			index = filecontent.find(b'\x00\x00\x00\x0a\x00\x00\x00\x04')
			# This is how I figure out where to start. The search isn't very smart and could very well find another patch of data with these exact values... but it worked for all four games so who cares?
			
			while index > -1:
			
				## find size
				file.seek(index+8)
				size = struct.unpack('>I', file.read(4))[0] # big endian unsigned int
				
				## find filename
				file.seek(11,1) # the size is defined here
				namelength = struct.unpack('>b', file.read(1))[0] # big endian unsigned char
				name = file.read(namelength).decode('ascii')
				
				## get chunk of data
				file.seek(12, 1) # skip ahead 12 bytes to get to the data
				data = file.read(size)
				
				## write
				g1t = open(name, "wb")
				g1t.write(data)
				g1t.close()
				
				index = filecontent.find(b'\x00\x00\x00\x0a\x00\x00\x00\x04', index+8)
