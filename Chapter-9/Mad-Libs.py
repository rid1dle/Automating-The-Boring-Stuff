from pathlib import Path
import re
content = open(Path.home() / 'input.txt')

totalContent = content.readlines()
totalContent = totalContent[0].split()
adj = re.compile(r'\w+', re.IGNORECASE)
content.close()
newStr = []
for i in totalContent:
    if (adj.search(i).group().upper() == 'ADJECTIVE'):
        i = " ". join(input('Enter an adjective: ').split())
        newStr.append(i)
    elif (adj.search(i).group().upper() == 'NOUN'):
        i = " ". join(input('Enter a noun: ').split())
        newStr.append(i)
    elif (adj.search(i).group().upper() == 'ADVERB'):
        i = " ". join(input('Enter a adverb: ').split())
        newStr.append(i)
    elif (adj.search(i).group().upper() == 'VERB'):
        i = " ". join(input('Enter a verb: ').split())
        newStr.append(i)
    else:
        newStr.append(i)

print(" ".join(newStr))
content = open(Path.home() / 'output.txt', 'w')
content.write(" ".join(newStr))
content.close()
