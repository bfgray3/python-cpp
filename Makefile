.PHONY: clean

CC = gcc
CFLAGS = -fPIC -pedantic -Wall -Wextra -Wshadow -Werror -Wconversion -Wpedantic
LDFLAGS = -shared
TARGET = sharedlibrary.so

$(TARGET):
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(TARGET) functions.c

clean:
	rm -rf __pycache__ $(TARGET)
