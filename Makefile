CC = gcc
CFLAGS = -g

all: child main

child: aslr.c
	$(CC) $(CFLAGS) -o $@ $<

main: main.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm child main

.PHONY: all clean