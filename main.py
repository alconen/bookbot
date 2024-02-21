# Function to count words in a given string
def count_words(string):
    words = string.split()
    return len(words)

# Function to generate a dictionary with letter counts
def count_letters(string):
    lower_string = string.lower()
    count_dict = {}
    for i in lower_string:
        if i in count_dict:
            count_dict[i] += 1
        else: 
            count_dict[i] = 1
    return count_dict

# Function to create a report for a book
def report(count_dict, text_name, word_count):
    # Function sort helper
    def sort_on(dict):
        return dict["num"]
    
    dict_list = []
    for i in count_dict:
        dict_entry = {}
        if i.isalpha():
            dict_entry["char"] = i
            dict_entry["num"] = count_dict[i]
            dict_list.append(dict_entry)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"""--- Begin report of {text_name} ---
{word_count} words found in the document
        """)
    for i in dict_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")
    
# Function to open text for a given path
def open_text(path):
    with open(path) as f:
        return f.read()
        
def main():
    path = "./books/frankenstein.txt"
    book = open_text(path)
    report(count_letters(book), path, count_words(book))

main()


    