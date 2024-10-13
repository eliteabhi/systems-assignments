import sys

def search_file(filename, search_word):
    with open(filename, 'r') as file:
        content = file.read()
        if search_word in content:
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file> <word>")
        sys.exit(1)

    filename = sys.argv[1]
    search_word = sys.argv[2]

    if search_file(filename, search_word):
        print(f"Word '{search_word}' found in {filename}")
    else:
        print(f"Word '{search_word}' not found in {filename}")
