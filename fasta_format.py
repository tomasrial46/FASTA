import sys
from argsparser import *
from sequences import *
from fasta import *
from transformations import *

args = parseArgs(sys.argv[1:])


if len(args)<2 or len(args)>4  or "input" not in args or "output" not in args:
    print("Ha puesto mal las keys")
    exit(1)

input= args['input']
output= args['output']


if 'case' in args:
    case = args['case']
else:
    case = 0
if 'maxLength' in args:
    maxLength = args['maxLength']
else:
    maxLength= 0


load = loadfile(input)
write = fasta_writer(output,load,case,maxLength)

