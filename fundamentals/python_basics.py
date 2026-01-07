def count_words(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    sample_text = "GenAI mastery starts with disciplined execution execution execution"
    result = count_words(sample_text)
    print(result)
