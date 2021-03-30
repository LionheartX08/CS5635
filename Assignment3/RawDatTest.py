

#files
stagdat208 = 'stagbeetle208x208x123.dat'
stagdat832 = 'stagbeetle832x832x494.dat'


counter = 0
os.remove('small.raw')
dest = open('small.raw','ab')
with open(stagdat208, "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        if (counter >= 6): 
           dest.write(byte)
        counter = counter + 1
dest.close()

#V2
counter = 0
#os.remove('small_2.raw')
dest = open('large_2.raw','ab')
with open(stagdat832, "rb") as f:
    byte = f.read(1)
    while byte:
        if (counter >= 6): 
           dest.write(byte)
        counter = counter + 1
        byte = f.read(1)        
dest.close()

counter = 0
#os.remove('small_2.raw')
dest = open('small_2.raw','ab')
with open(stagdat208, "rb") as f:
    byte = f.read(1)
    while byte:
        if (counter >= 6): 
           dest.write(byte)
        counter = counter + 1
        byte = f.read(1)        
dest.close()