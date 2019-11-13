Dict={
    'help': 'madad',
    'forgive': ['kshama karana', 'cdcd', 'cdscs'],
    'forget': 'bhool jao',
    'meditation': 'dhyaan',
    'stop': ['ruken', 'cdcd', 'cdsc'],
    'slow': ['dhema', 'cdsc', 'eevf'],
    'moving': 'chalatee',
    'hair': ['baal', 'rewg', 'wqee'],
    'funny': 'majedaar'
}
print("Welcome to Englis to Hindi Dictionary")
print ("Select the word for meaning")
for words in Dict:
    print words
word=raw_input("Enter the word for meaning: ")
if word in Dict:
    print ("the Hindi meaning is: " + str(Dict[word]))
else:
    print ("invalid entery!!! ")



