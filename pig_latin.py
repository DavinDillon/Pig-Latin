sentence = input('Enter the text you would like to have translated:   ')
lst = sentence.split()
vowels = ('aeiouAEIOU')
translation = []
for word in lst:
    if word[0] in vowels:
        translation.append(word + 'ay')
    else:
        for ch in word:
            if ch in vowels:
                ind = word.find(ch)
                break
        word = word[ind:] + word[:ind] + 'ay'
        translation.append(word)
newsent = ''        
for wd in translation:
    newsent += wd + ' '
print(newsent)
