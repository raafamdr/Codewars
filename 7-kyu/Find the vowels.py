def vowel_indices(word):
    index_list = []
    for i in range(len(word)):
        if word[i].lower() in 'aeiouy':
            index_list.append(i+1)
    return index_list
