def main():
    #logic code
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = word_counter(file_contents)
        print(f'Total words: {word_count}')
        char_counter(file_contents)

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

def char_counter(file_contents):
    lowered_string = file_contents.lower()
    char_count = {}
    for i in lowered_string:
        char_count[i]=char_count.setdefault(i, 0)+1
    print(char_count)
          
if __name__ == "__main__":
    main()


