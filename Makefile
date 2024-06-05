CC = gcc
CFLAGS = -g

all: child main

child: aslr.c
	$(CC) $(CFLAGS) -o $@ $<

main: main.c
	$(CC) $(CFLAGS) -o $@ $<

plot:
	./main 25
	./main 50
	./main 100
	python3 entropy_calc.py

clean:
	rm child main

.PHONY: all clean