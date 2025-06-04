# 9. Use the collections.defaultdict to group words by their first letter from a list.
#    Input: ["apple", "banana", "apricot", "blueberry"]
#    Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

from collections import defaultdict

def group_by_first_letter(words):
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)  
    return dict(grouped)  

print(group_by_first_letter(["apple", "banana", "apricot", "blueberry"]))
 
