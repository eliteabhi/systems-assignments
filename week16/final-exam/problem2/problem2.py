import os

def main() -> None:

    if "EXAM_MODE" in os.environ and os.environ[ "EXAM_MODE" ] == 'debug':
        print( f'Process ID: { os.getpid() }' )
        print( f'Parent Process ID: { os.getppid() }' )

    else:
        os.environ[ "EXAM_MODE" ] = 'release'

if __name__ == "__main__":
    main()