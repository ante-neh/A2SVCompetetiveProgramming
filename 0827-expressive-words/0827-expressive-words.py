class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def countConsecutiveLetters(string: str, index: int) -> Tuple[int, int]:
            prev = index
            count = 0
            while index < len(string):
                if prev == index or string[index] == string[prev]:
                    prev = index
                    count += 1
                else:
                    return (count, index)
                index += 1
            return (count, index)


        def isStretchy(word: str, s: str) -> bool:
            if len(s) < len(word):
                return False

            s_index = 0
            word_index = 0

            while s_index < len(s) and word_index < len(word):
                s_count_letter, new_s_index = countConsecutiveLetters(s, s_index)
                word_count_letter, new_word_index = countConsecutiveLetters(word, word_index)

                if s[s_index] != word[word_index]:
                    return False

                if s_count_letter < word_count_letter:
                    return False

                if s_count_letter > word_count_letter and s_count_letter < 3:
                    return False

                s_index = new_s_index
                word_index = new_word_index

            if s_index == len(s) and word_index == len(word):
                return True

            return False

        count = 0
        for word in words:
            if isStretchy(word, s):
                count += 1
        return count