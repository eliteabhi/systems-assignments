#!/usr/bin/env python3

# writer.py
import random

FUNCTION: str = "nop_slide"

def insert_random_nops_and_fnops( f, max_new_lines = 20, seed = 10 ) -> None:
    """
    Inserts random nop/fnop instructions into the given file.
    """

    nops = random.sample( range( 1, max_new_lines + 1 ), random.randint(1, seed) )

    for _ in nops:
        f.write("  nop\n")
        f.write("  fnop\n")

def main():

    with open(f"./{FUNCTION}.S", 'w') as f:

        # Directives.
        f.write("  .text\n\n")
        f.write(f"  .global {FUNCTION}\n")
        f.write(f"  .type   {FUNCTION}, @function\n")
        f.write(f"{FUNCTION}:\n")

        # Function prologue.
        f.write("  pushq %rbp\n")
        f.write("  movq %rsp, %rbp\n")

        # Read TSC - start.
        f.write("  rdtscp\n")
        f.write("  movl %eax, %ebx\n")

        # Insert random nop instructions.
        insert_random_nops_and_fnops( f )

        # Read TSC - end.
        f.write("  rdtscp\n")
        f.write("  subl %ebx, %eax\n")

        # Function epilogue.
        f.write("  popq %rbp\n")
        f.write("  retq\n")


if __name__ == "__main__":
    main()
