import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nata_data_dictionary = {value.letter: value.code for (key, value) in nato_data.iterrows()}

while True:
    user_input = input("Enter the word: ").upper()
    try:
        nato_list = [nata_data_dictionary[letter] for letter in user_input]
    except KeyError as error:
        print(f"Fault is: {error}\nSorry, only letters in the alphabet please.")
    else:
        print(nato_list)

