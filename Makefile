CC = gcc
CFLAGS = -c -g
OBJ = main.o aslr.o
TARGET = aslr_test
all: $(TARGET)

$(TARGET) : $(OBJ)
	$(CC) -o $@ $^

child.o : aslr.c
	$(CC) $(CFLAGS) -o $@ $<

main.o : main.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm child main

.PHONY: all clean