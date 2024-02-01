import re
import enchant

def encrypt(plaintext, shift):
  """Encrypts a message that uses caesar's cipher. Shift key must be provided."""
  base_char = ''

  encrypted_text = ""

  word_split = plaintext.split()

  for word in word_split:
    for char in word:
      if char.islower():
        base_char = 'a'
      if char.isupper():
        base_char = 'A'
      if bool(re.search(r'[A-Za-z]', char)):
        base_char_code = ord(base_char)
        char_select_code = ord(char)
        char_code = char_select_code - base_char_code
        shifted_text = char_code + shift
        factored_char_code = shifted_text % 26
        encrypted_char = chr(factored_char_code + base_char_code)
        encrypted_text += encrypted_char
      else:
        encrypted_text += char
    encrypted_text += ' '
  encrypted_text = encrypted_text[:-1]
  return encrypted_text

def decrypt(encrypted, shift):
  """Decrypts a message that uses caesar's cipher. Shift key must be provided."""
  return encrypt(encrypted, -shift)

def crack(encrypted):
  """Via brute force, cracks an encrypted message that uses caesar's cipher."""
  d = enchant.Dict("en_US")

  shift_count = 0

  cracked = ''

  while shift_count < 26:
    word_count = 0
    sentence_test = decrypt(encrypted, shift_count)
    sentence_test_words = sentence_test.split()

    for word in sentence_test_words:
      word_clean = re.findall(r'\w*', word)
      if d.check(word_clean[0]):
        word_count += 1
        
    word_ratio = word_count / len(sentence_test_words)

    if word_ratio > .5:
      print(word_ratio)
      cracked += sentence_test
      print(cracked)
    shift_count += 1

  return cracked
