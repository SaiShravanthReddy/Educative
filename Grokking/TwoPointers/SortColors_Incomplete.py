import re


def reverse_string(char_string, start, end):
  while start < end:
    char_string[start], char_string[end] = char_string[end], char_string[start]
    start += 1
    end -= 1
    

def reverse_words(sentence):
  sentence = sentence.strip()
  
  sentence = re.sub(" +", " ", sentence)
  sentence_list = list(sentence)
  reverse_string(sentence_list, 0, len(sentence_list)-1)
  
  start = 0
  for end in range(len(sentence_list)):
    if sentence_list[end] == ' ':
      reverse_string(sentence_list, start, end-1)
      start = end + 1
    
  reverse_string(sentence_list, start, end)
  
  return "".join(sentence_list)