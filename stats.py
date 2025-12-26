def count_words(words):
    word_count = words.split()
    return word_count

def count_characters(characters):
    character_count = {}

    for character in characters:
        lowercase = character.lower()
        if lowercase in character_count:
            character_count[lowercase] += 1
            
        else:
            character_count[lowercase] = 1
            
    return character_count

def sort_on(items):
    return items["num"]

def sort_characters(dict):
    sorted_list = []

    for ch in dict:
        sorted_list.append({"char": ch, "num":dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    