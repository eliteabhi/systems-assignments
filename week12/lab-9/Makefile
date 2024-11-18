CC = gcc
PY = python3

.PHONY: all clean

all: main.c nop_slide.S
	$(CC) $^ -o app

nop_slide.S: writer_abhi_rangarajan.py
	$(PY)   $^ 

clean:
	rm -f app
	rm -f nop_slide.S
