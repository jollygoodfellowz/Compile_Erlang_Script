For this script to work you must have an Erlang shell installed. If you do not please visit
http://www.erlang.org/doc/installation_guide/INSTALL.html
compile_erl.txt was designed to streamline the compilation process of Erlang. 

In compile_erl.txt we make a few assumptions. 

1)The first one being that the script file is in the same directory as the .erl file you want to compile. 

2)Secondly we assume the file only has one occurence of .erl. 

The line below tests three functions and compiles two modules
python compile_epython compile_erl.py -f test.erl -m main test testsrl.py -f test.erl -m main test tests

The line below tests just the main function by omitting optional arguements
python compile_erl.py -f test.erl