# Грехов Александр 11-10

def generate_words(alphabet, word_length, k):
    def helper(word, m):
        nonlocal k
        if m == 0:
            k -= 1
            if k == 0:
                return word
            return None
        for letter in alphabet:
            result = helper(word + letter, m - 1)
            if result is not None:
                return result
        return None

    return helper("", word_length)


M = 3
alphabet = [chr(i + ord('A')) for i in range(M)]
N = 3
K = 7

print(generate_words(alphabet, N, K))
