
-module(o_test).
	-export([main/0]).
	-export([test/0]).
	-export([tests/0]).

	main() -> io:fwrite("hello!!!!\n"). 
	test() -> io:fwrite("testing is going well!!!\n"). 
	tests() -> io:fwrite("testsssss\n"). 

