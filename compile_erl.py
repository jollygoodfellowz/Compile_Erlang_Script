# Chris Chaffin
# This file compiles erlang files through a script
import sys
import subprocess
from time import sleep
import argparse

##################################################################################
##################################################################################
# Add any additional arguments here
def add_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--File",
		type=str,
		help="The Erlang file to be compiled",
		nargs='+')
	parser.add_argument("-m","--Main",
		help="Give the module you wish to execute functions from. If nothing is provided the first module is assumed.",
		type=str)
	parser.add_argument("-fu","--Functions",
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

	# Check to see what the erl shell command is
	if args.Erlang == None:
		erl_shell = "erl"
	else:
		erl_shell = args.Erlang

	# Start the shell
	erl = subprocess.Popen([erl_shell],
		stdin=subprocess.PIPE)

	# Pause to let the shell start
	sleep(0.1)

	# Compile the files provided
	for erl_file in args.File:
		ifp = open(erl_file, "r")
		module = erl_file.split('.erl')			# Get the name of the module
		compiled = "c(" + module[0] + "). "		# Compile the file in the erlang shell
		erl.stdin.write(compiled)				
		sys.stdout.flush()
		ifp.close()
		sleep(0.1)

	# Run the functions provided in Erlang
	run_funcs(args,erl)
##################################################################################
##################################################################################
# Run the functions provided by the user
def run_funcs(args,erl):

	if args.Main == None:
		module = args.File[0].split('.erl')
	else:
		module = args.Main.split('.erl')

	# If no argument was provided we assume main is the function we wish to execute
	if args.Functions == None:
		func = "main"
		main = module[0] + ":" + func + "(). "
		erl.communicate(main)

	# Otherwise we will execute the functions provided in -m
	else:
		for func in args.Functions:
			new_func = module[0] + ":" + func + "(). "
			erl.stdin.write(new_func)
			sys.stdout.flush()
			sleep(0.1)
			
##################################################################################
##################################################################################
# Open the .erl file compile and run it
args = add_arguments()

if args.File == None:
	sys.exit("You must provide a file with -f. Type --help for more information")

compile_erl(args)
