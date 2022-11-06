import json

VALID_SEARCH_OPTIONS = ["1", "2", "quit"]
DATA_FILE_NAMES = ["users.json", "tickets.json", "organizations.json"]
FILES_ATTRIBUTE_NAMES = ["Users", "Tickets", "Organizations"]


def search_options_selector():
    """
    This function contains search option selector execution
    """
    print("\tSelect search option:\n\t * Press 1 to search Zendesk\n\t * Press 2 to view a list of searchable fields\n\t * Type 'quit' to exit")
    search_options_input = input()
    if search_options_input not in VALID_SEARCH_OPTIONS:
        print("*Please enter a valid option*")
        search_options_selector()
    else:
        return search_options_input


def read_file_data(file_name):
    """
    This function returns data from the given file name 
    """
    try:
        file_opened = open(file_name)
        file_data = json.load(file_opened)
        return file_data
    except:
        print("No file exist with given name")


def handle_term_value_search(data, required_search):
    """
    This function handles search with term and value
    """
    search_term = input("Enter search term\n")
    serach_value = input("Enter search value\n")
    serach_value = int(
        serach_value) if serach_value.isnumeric() else serach_value
    searched_value = ''
    print(f"Searching {FILES_ATTRIBUTE_NAMES[required_search-1].lower()} for {search_term} with a value of {serach_value}")
    
    for values in data:
        if search_term in values.keys() and values[search_term] == serach_value:
            searched_value = values

    return searched_value


def handle_search_options(option_value):
    """
    This function conatins execution to handle search options entered by user
    """
    required_search = int(
        input('Select 1) Users or 2) Tickets or 3) Organizations '))

    if 0 < required_search <= 3:
        selected_file_data = read_file_data(
            DATA_FILE_NAMES[required_search - 1])
        search_result = handle_term_value_search(selected_file_data, required_search)
        return search_result
    else:
        print("*Enter a valid choice*")
        handle_search_options(option_value)


def handle_search_output(search_result):
    """
    This function handles the format to show final output to the user
    """
    if search_result:
        for key, value in search_result.items():
            value = str(value).center(90 - len(key), " ")
            print(key, value)
    else:
        print("No results found")


def show_all_files_data_keys():
    """
    This function show the keys of the data elements from all the file
    """
    for index, file in enumerate(DATA_FILE_NAMES):
        data_read = read_file_data(file)
        print(
            f"--------------------------------\nSearch {FILES_ATTRIBUTE_NAMES[index]} with")
        for key in data_read[0].keys():
            print(key)


def start_zendesk():
    """
    This function contains the complete execution of zendesk
    """

    user_input = str(input(
        "Welcome to zendesk solution \nType 'quit' to exit at any time, Press Enter to continue\n"))

    if user_input == "":
        selected_option = search_options_selector()
        if selected_option == "2":
            show_all_files_data_keys()
            return False
        elif selected_option == "quit":
            return False
        
        search_result = handle_search_options(selected_option)
        handle_search_output(search_result)

    elif user_input == "quit":
        return False
    else:
        start_zendesk()


if __name__ == '__main__':
    """
    Main functoin where execution of the function starts
    """
    start_zendesk()
