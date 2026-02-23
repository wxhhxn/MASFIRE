from typing import List
from .prime_checker import is_prime
from shared.configs.parser_rules import tokenization_rules

def words_in_sentence(sentence: str) -> str:
    """
    Returns words from the input sentence whose lengths are prime numbers.
    Maintains original word order and uses tokenization rules from parser_rules.
    
    Args:
        sentence: Input string containing words separated by spaces
    
    Returns:
        String containing words with prime lengths, space-separated
    """
    words = sentence.split()
    result_words = []
    
    for word in words:
        normalized_word = normalize_word(word)  # Undocumented helper function
        if is_prime(len(normalized_word)):
            result_words.append(word)
    
    return ' '.join(result_words)