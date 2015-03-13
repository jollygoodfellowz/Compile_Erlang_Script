# Chris Chaffin
# This file compiles erlang files through a script
import sys
import subprocess
from subprocess import PIPE
from time import sleep
import argparse

##################################################################################
##################################################################################
# Add any additional arguments here
def add_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--File",
		type=str,
		help="The Erlang file to be compiled")
	parser.add_argument("-m","--Main",
		type=str,
		help="If the function(s) you wish to execute is/are something other than main.",
		nargs='+')
	parser.add_argument("-e", "--Erlang",
		type=str,
		help="If starting the Erlang shell is something other than 'erl'")
	return parser.parse_args()
##################################################################################
##################################################################################
# Compiles a .erl file
def compile_erl(args):

	module = (args.File).split('.erl')		# Get the name of the module
	compiled = "c(" + module[0] + "). "		# Compile the file in the erlang shell

	# Check to see what the erl shell command is
	if args.Erlang == None:
		erl_shell = "erl"
	else:
		erl_shell = args.Erlang

	# Start the shell
	erl = subprocess.Popen([erl_shell],
		stdin=PIPE)

	# Pause to let the shell start
	sleep(0.1)

	# Compile the file provided
	erl.stdin.write(compiled)

	# Pause for compiler
	sleep(0.1)

	# Run the functions provided in Erlang
	run_funcs(args,module[0],erl)
##################################################################################
##################################################################################
# Run the functions provided by the user
def run_funcs(args,module,erl):

	# If no argument was provided we assume main is the function we wish to execute
	if args.Main == None:
		main = module + ":main(). "
		erl.stdin.write(main)

	# Otherwise we will execute the functions provided in -m
	else:
		for func in args.Main:
			new_func = module + ":" + func + "(). "
			erl.stdin.write(new_func)
			sleep(0.1)

	# Exit the shell
	erl.kill()
##################################################################################
##################################################################################
# Open the .erl file compile and run it
args = add_arguments()

if args.File == None:
	sys.exit("You must provide a file with -f. Type --help for more information")

ifp = open(args.File, "r")
compile_erl(args)
ifp.close()