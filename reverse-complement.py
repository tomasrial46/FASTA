import sys
from argsparser import *
from script_utils import apply_transformation

args = parseArgs(sys.argv[1:])

input_file = args['input']
output_file = args['output']
transformation = args['trans']

apply_transformation(input_file, output_file, transformation)