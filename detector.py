from spellchecker import SpellChecker
spell = SpellChecker()

word = "teh" # A deliberate typo
print(f"Correction for '{word}':", spell.correction(word))