CC = gcc
CFLAGS = -Wall -g -std=gnu99 -pthread

.PHONY : all clean

all : sequential parallel 3dsequential 3dparallel

sequential : sequential.c
	$(CC) $(CFLAGS) sequential.c -o sequential -lm

parallel : parallel.c
	$(CC) $(CFLAGS) parallel.c -o parallel -lm

3dsequential : 3dsequential.c
	$(CC) $(CFLAGS) 3dsequential.c -o 3dsequential -lm

3dparallel : 3dparallel.c
	$(CC) $(CFLAGS) 3dparallel.c -o 3dparallel -lm

clean :
	/bin/rm -f sequential parallel 3dsequential 3dparallel
