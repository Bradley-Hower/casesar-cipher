# LAB - Class 18

## Project: Caesar Cipher

## Author: Bradley Hower

## Dependencies

Regular expression, used to isolate English letters. `pip install re`

Enchant, used to compare words for validity in decyphering decryption trials for crack function. `pip install pyenchant`

## Tests

Run `pytest` to confirm functionality.

Installing Pytest:

1. Creat virtual environment:  `python3 -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate`
3. Freeze requirements: `pip freeze > requirements.txt`
4. Install test: `pip install pytest`

Be sure to point test files located in the tests folder to the file to be tested.

Note, sometimes pytest needs to be uninstalled and reinstalled if it was previous installed under another directory.

## Run

To encrypt a message, use `encrypt(plaintext, shift)`. In this function, "plaintext" represents a string of text to be encrypted. No concern for symbols or spaces needed as these will be ignored. "Shift" is the degree by how many letters each character will be shifted down the alphabet. Any number over 26 will be circled back.

To decrypt a message, use `decrypt(encrypted, shift)`, where "encrypted" is the encrypted string of text, and "shift" is again the amount shifted at the original encryption.

If the shift key is unknown, no worries. The `crack(encrypted)` function can be used. Here, the function will do its best to find the shift that is most likely correct, based on percentage of real English words found upon shifting.
