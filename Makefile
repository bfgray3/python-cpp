.PHONY: clean

CC = g++
CFLAGS = -fPIC -pedantic -Wall -Wextra -Wshadow -Werror -Wconversion -Wpedantic
LDFLAGS = -shared
TARGET = sharedlibrary.so

$(TARGET):
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(TARGET) functions.cpp

clean:
	rm -rf __pycache__ $(TARGET)
