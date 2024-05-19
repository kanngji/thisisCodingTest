class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # 패턴과 단어 리스트의 길이가 다르면 False 반환
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for p, w in zip(pattern, words):
            # 패턴 문자에 대한 단어 매핑 확인
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False
            else:
                char_to_word[p] = w
            
            # 단어에 대한 패턴 문자 매핑 확인
            if w in word_to_char:
                if word_to_char[w] != p:
                    return False
            else:
                word_to_char[w] = p
        
        return True