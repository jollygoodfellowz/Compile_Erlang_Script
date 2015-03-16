For this script to work you must have an Erlang shell installed. If you do not please visit
http://www.erlang.org/doc/installation_guide/INSTALL.html
compile_erl.txt was designed to streamline the compilation process of Erlang. 

In compile_erl.txt we make a few assumptions. 

1)The first one being that the script file is in the same directory as the .erl file you want tocompile. 

2)Secondly we assume the file only has one occurence of .erl. 

3)Lastly, we assume that to open the erlang shell your command line takes the command "erl". That's it!

If you wish to test out the script run this command from the directory in the command line

The line below tests all three functions in the file
python compile_erl.py -f test.erl -m main test tests

The line below tests just the main function by omitting the -m arguement
python compile_erl.py -f test.erl


Feel free to modify to suit your needs. Please give credit if you decide to use the file!
