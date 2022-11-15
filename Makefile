.PHONY: clean

CC = gcc
CFLAGS = -fPIC -pedantic -Wall -Wextra -Wshadow -Werror
LDFLAGS = -shared
TARGET = sharedlibrary.so

$(TARGET):
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(TARGET) functions.c

clean:
	rm -rf __pycache__ *.o *.so
