def main():
    #logic code
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = word_counter(file_contents)
        
        print(f'--- Begin report of books/frankenstein.txt ---')
        print(f'{word_count} words found in the document\n')
        
        char_count = char_counter(file_contents)
        char_list = [{'char': key, 'num': value} for key, value in char_count.items()]
        char_list.sort(reverse=True, key=sort_on)
         
        alpha_char_list = [item for item in char_list if item['char'].isalpha()]

        for item in alpha_char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")

        print('\n--- End report ---')

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

def char_counter(file_contents):
    lowered_string = file_contents.lower()
    char_count = {}
    for i in lowered_string:
        char_count[i]=char_count.setdefault(i, 0)+1
 #   print(char_count)
    return char_count   

def sort_on(char_count):
    return char_count["num"]


if __name__ == "__main__":
    main()


