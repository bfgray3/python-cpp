.PHONY: clean

CFLAGS = -fPIC -pedantic -Wall -Wextra -Wshadow -Werror -Wconversion -Wpedantic
LDFLAGS = -shared

.ONESHELL:
results.txt: clean c.so cpp.so
	./main.py -n 31 --language c > $@
	./main.py -n 31 --language cpp >> $@

c.so:
	gcc $(LDFLAGS) $(CFLAGS) -o $@ $(wildcard *.c)

cpp.so:
	g++ $(LDFLAGS) $(CFLAGS) -o $@ $(wildcard *.cpp)

clean:
	rm -rf __pycache__ *.so results.txt
