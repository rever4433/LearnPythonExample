from sys import argv
from os.path import exists

script,from_file, to_file=argv

print("Copying from %s to %s"%(from_file,to_file))

# we would do these two on one line too, how?

_input=open(from_file)

indata=_input.read()

print("The input file is %d bytes long"% len(indata))
print("Does the output file exist? %r"% exists(to_file))

input()

output=open(to_file,'w')
output.write(indata)

print("Alright, all done.")

output.close()
_input.close()
