
-module(test).
	-export([main/0]).
	-export([test/0]).
	-export([tests/0]).

	main() -> io:fwrite("hello, world\n"). 
	test() -> io:fwrite("test\n"). 
	tests() -> io:fwrite("testsssss\n"). 
