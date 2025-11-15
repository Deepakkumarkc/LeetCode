def update_word(words, start_word, end_word):

    for index,value in enumerate(words):
        if (value == start_word):
            being_index = int(index)
            print ("Start Index:",being_index)

        if (value == end_word):
            end_index = int(index)
            print ("End Index:", end_index)
    
    if being_index != -1 and end_index != -1 :
        return end_index - being_index
    else:
        print("Error not found")


beginWord = 'hit'
endWord = 'cog'
wordList = ["hit", "hot", "dot", "dog", "cog"] 
print(update_word(wordList, beginWord, endWord))

