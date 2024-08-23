import sys
from argsparser import *
from script_utils import apply_transformation

args = parseArgs(sys.argv[1:])

if len(args) != 3 or "input" not in args or "output" not in args or "mode" not in args:
    print("Ha puesto mal las keys")
    exit(1)

input_file = args['input']
output_file = args['output']
transformation = args['mode']

apply_transformation(input_file, output_file, transformation)