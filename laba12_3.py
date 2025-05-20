def create_russian_english_dictionary(input_file, output_file):
    ru_en_dict = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split(' - ')
            if len(parts) != 2:
                continue
            en_word = parts[0].strip()
            ru_translations = parts[1].strip().split(', ')

            for ru_word in ru_translations:
                ru_word = ru_word.strip()
                if ru_word in ru_en_dict:
                    if en_word not in ru_en_dict[ru_word]:
                        ru_en_dict[ru_word] += ', ' + en_word
                else:
                    ru_en_dict[ru_word] = en_word

    sorted_words = sorted(ru_en_dict.items(), key=lambda x: x[0])
    with open(output_file, 'w', encoding='utf-8') as f:
        for ru_word, en_translations in sorted_words:
            f.write(f"{ru_word} - {en_translations}\n")

input_filename = 'en-ru.txt'
output_filename = 'ru-en.txt'
create_russian_english_dictionary(input_filename, output_filename)