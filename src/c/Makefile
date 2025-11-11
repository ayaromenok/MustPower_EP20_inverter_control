CC = gcc
CFLAGS = -Wall -g

all: test00

test00: test00.o 
	$(CC) $(CFLAGS) -o build/test00 test00.o

/test00.o: test00.c
	$(CC) $(CFLAGS) -c test00.c


clean:
	rm -f *.o build/test00
