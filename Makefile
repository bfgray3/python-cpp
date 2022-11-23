.PHONY: clean

CFLAGS = -fPIC -pedantic -Wall -Wextra -Wshadow -Werror -Wconversion -Wpedantic
LDFLAGS = -shared

c.so:
	gcc $(LDFLAGS) $(CFLAGS) -o $@ $(wildcard *.c)

cpp.so:
	g++ $(LDFLAGS) $(CFLAGS) -o $@ $(wildcard *.cpp)

clean:
	rm -rf __pycache__ *.so
