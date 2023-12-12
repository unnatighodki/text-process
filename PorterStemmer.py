class PorterStemmer:

    # Added by Unnati
    def __init__(self, letter = None):
        self.letter = letter
    

    # Checking if the letter is vowel
    def is_vowel(self, letter):
        letter = letter.lower()
        return letter in ('a', 'e', 'o', 'i', 'u')
    
    # Checking if the letter is consonant
    def is_consonant(self, letter):
        return not self.is_vowel(letter)
    
    # Returning the pattern having V and C
    def form(self, word):
        pattern = []
        for i in range(len(word)):
            pattern.append('V' if self.is_vowel(word[i]) else 'C')
        return ''.join(pattern)

    # Counting occurence of vowel followed by consonant
    def m_count(self, word):
        form_string = self.form(word)
        return form_string.count('VC')

    # Getting the root word
    def get_base(self, word, suffix):
        suflen = word.rfind(suffix)
        return word[:suflen]

    # Changing the suffix
    def replacer(self, word, suffix1, suffix2):
        base = self.get_base(word, suffix1)
        return base + suffix2
    
    # Checking if the word ends with stem
    def endswith_s(self, stem):
        return stem.endswith('s')

    # identifies presense of vowel
    def contains_vowel(self, stem):
        return any(self.is_vowel(letter) for letter in stem)

    # Checking if the last two letters in word are consonants 
    def CC(self, stem):
        pattern = self.form(stem)
        return pattern[-1] == 'C' and pattern[-2] == 'C'
    
    # Checking if the last two letters are - CVC and does not end with xyz
    def CVC(self, stem):
        stem = stem.lower()
        pattern = self.form(stem)
        return pattern[-1] == 'C' and pattern[-2] == 'V' and pattern[-3] == 'C' and stem[-1] not in 'xyz'

    def step_1(self, word):
        word = self.step_1a(word)
        word = self.step_1b(word)
        word = self.step_1c(word)
        return word

    def step_1a(self, word):
        word = word.lower()
        new_word = word
        if word.endswith('sses'):
            new_word = self.replacer(word, 'sses', 'ss')
        elif word.endswith('ies'):
            new_word = self.replacer(word, 'ies', 'i')
        elif word.endswith('ss'):
            new_word = word
        elif word.endswith('s'):
            new_word = self.replacer(word, 's', '')
        return new_word

    def step_1b(self, word):
        new_word = word
        if word.endswith('eed'):
            suflen = len('eed')
            base = word[:suflen]
            if self.m_count(base) > 0:
                new_word = self.replacer(word, 'eed', 'ee')
        elif word.endswith('ed'):
            suflen = word.rfind('ed')
            base = word[:suflen]
            if self.contains_vowel(base):
                new_word = word[:suflen]
                new_word = self.step_1b_part2(new_word)
        elif word.endswith('ing'):
            suflen = word.rfind('ing')
            base = word[:suflen]
            if self.contains_vowel(base):
                new_word = word[:suflen]
                new_word = self.step_1b_part2(new_word)
        return new_word

    def step_1b_part2(self, word):
        if word.endswith(('at', 'bl', 'iz')):
            word += 'e'
        elif self.CC(word) and not word.endswith(('s', 'z', 'l')):
            word = word[:-1]
        elif self.m_count(word) == 1 and self.CVC(word):
            word += 'e'
        return word

    def step_1c(self, word):
        if self.contains_vowel(word) and word.endswith('y'):
            return self.replacer(word, 'y', 'i')
        else:
            return word

    def step_2(self, word):
        if word[-2] == 'a':
            if word.endswith('ational'):
                base = self.get_base(word, 'ational')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ational', 'ate')
            elif word.endswith('tional'):
                base = self.get_base(word, 'tional')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'tional', 'tion')
        elif word[-2] == 'c':
            if word.endswith('enci'):
                base = self.get_base(word, 'enci')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'enci', 'ence')
            elif word.endswith('anci'):
                base = self.get_base(word, 'anci')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'anci', 'ance')
        elif word[-2] == 'z':
            if word.endswith('izer'):
                base = self.get_base(word, 'izer')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'izer', 'ize')
        elif word[-2] == 'l':
            if word.endswith('abli'):
                base = self.get_base(word, 'abli')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'abli', 'able')
            elif word.endswith('alli'):
                base = self.get_base(word, 'alli')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'alli', 'al')
            elif word.endswith('entli'):
                base = self.get_base(word, 'entli')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'entli', 'ent')
            elif word.endswith('eli'):
                base = self.get_base(word, 'eli')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'eli', 'e')
            elif word.endswith('ousli'):
                base = self.get_base(word, 'ousli')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ousli', 'ous')
        elif word[-2] == 'o':
            if word.endswith('ation'):
                base = self.get_base(word, 'ation')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ation', 'ate')
            elif word.endswith('ization'):
                base = self.get_base(word, 'ization')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ization', 'ize')
            elif word.endswith('ator'):
                base = self.get_base(word, 'ator')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ator', 'ate')
        elif word[-2] == 's':
            if word.endswith('alism'):
                base = self.get_base(word, 'alism')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'alism', 'al')
            elif word.endswith('iveness'):
                base = self.get_base(word, 'iveness')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'iveness', 'ive')
            elif word.endswith('fulness'):
                base = self.get_base(word, 'fulness')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'fulness', 'ful')
            elif word.endswith('ousness'):
                base = self.get_base(word, 'ousness')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'ousness', 'ous')
        elif word[-2] == 't':
            if word.endswith('aliti'):
                base = self.get_base(word, 'aliti')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'aliti', 'al')
            elif word.endswith('iviti'):
                base = self.get_base(word, 'iviti')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'iviti', 'ive')
            elif word.endswith('biliti'):
                base = self.get_base(word, 'biliti')
                if self.m_count(base) > 0:
                    word = self.replacer(word, 'biliti', 'ble')
        return (word)

    def step_3(self, word):
        if word.endswith('icate'):
            base = self.get_base(word, 'icate')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'icate', 'ic')
        elif word.endswith('ative'):
            base = self.get_base(word, 'ative')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'ative', '')
        elif word.endswith('alize'):
            base = self.get_base(word, 'alize')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'alize', 'al')
        elif word.endswith('iciti'):
            base = self.get_base(word, 'iciti')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'iciti', 'ic')
        elif word.endswith('ful'):
            base = self.get_base(word, 'ful')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'ful'), ''
        elif word.endswith('ness'):
            base = self.get_base(word, 'ness')
            if self.m_count(base) > 0:
                word = self.replacer(word, 'ness', '')
        return word

    def step_4(self, word):
        suffixes = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ou', 'ism', 'ate',
                    'iti', 'ous', 'ive', 'ize']
        for suffix in suffixes:
            if word.endswith(suffix):
                base = self.get_base(word, suffix)
                if self.m_count(base) > 1:
                    word = self.replacer(word, suffix, '')
        if word.endswith('ion'):
            base = self.get_base(word, 'ion')
            if self.m_count(base) > 1 and base.endswith('s') or base.endswith('t'):
                word = self.replacer(word, 'ion', '')
        return word

    def step_5a(self, word):
        if word.endswith('e'):
            base = self.get_base(word, 'e')
            if self.m_count(base) > 1 or (self.m_count(base) == 1 and not self.CVC(base)):
                word = self.replacer(word, 'e', '')
        return word

    def step_5b(self, word):
        if self.CC(word) and word.endswith('l') and self.m_count(word) > 1:
            word = word[:-1]
        return word

    def stem(self, word):
        word = self.step_1(word)
        word = self.step_2(word)
        word = self.step_3(word)
        word = self.step_4(word)
        word = self.step_5a(word)
        word = self.step_5b(word)
        return word

if __name__ == "__main__":
    word = 'specialize'
    test_wrd = PorterStemmer()
    test_wrd.stem('specialize') # special
    test_wrd.stem('functional') # funct

