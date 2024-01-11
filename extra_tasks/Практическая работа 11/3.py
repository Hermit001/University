class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str) or not s:
            return False
        return self == s * (len(self) // len(s))
    
    def is_palindrome(self):
        s = self.lower()
        return s == s[::-1]

# Пример использования
s = SuperStr("abcabcabc")
print(s.is_repeatance("abc"))  # True
print(s.is_repeatance("ab"))   # False
print(s.is_repeatance("a"))    # True
print(s.is_palindrome())       # False

palindrome_str = SuperStr("Tenet")
print(palindrome_str.is_palindrome())  # True
