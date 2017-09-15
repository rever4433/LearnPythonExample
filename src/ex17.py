from sys import argv
from os.path import exists

script, from_file, to_file=argv

print("Copying from %s to %s"%(from_file,to_file))
# we could do these two on one line too,how?

_input=open(from_file)
indata=_input.read()

print("Ready , hit RETURN to continue, CTRL-C to abort.")
input()

output=open(to_file,'w')

output.write(indata)

print("Alright,all done.")

output.close()

_input.close()
