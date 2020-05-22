# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
  word_start = word.find(start)
  word_end = word.find(end)
  if word_start == -1 or word_end == -1:
    return word
  else:
    return word[word_start+1:word_end]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"