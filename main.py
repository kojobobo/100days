with open('Input/Letters/starting_letter.txt', 'r') as letter:
    initial_letter = letter.read()

with open("Input/Names/invited_names.txt", 'r') as names:
    initial_name_list = names.readlines()

final_name_list = []

for name in initial_name_list:
    name = name.replace('\n', '')
    final_name_list.append(name)

for name in final_name_list:
    with open(f'Output/ReadyToSend/{name}.txt', 'a+') as file:
        final_letter_text = initial_letter.replace('[name]', name)
        file.write(final_letter_text)
        print(final_letter_text)
