"""
Write a class called WordPlay. It should have a constructor that holds a list of words. The user of the class should pass the
list of words through constructor, which user wants to use for the class. The class should have following methods:
words_with_length(length) — returns a list of all the words of length length
starts_with(char1) — returns a list of all the words that start with char1
ends_with(char2) — returns a list of all the words that end with char2
palindromes() — returns a list of all the palindromes in the list
only(str1) — returns a list of the words that contain only those leƩers in str1
avoids(str2) — returns a list of the words that contain none of the leƩers in str2
Make Required object for WordPlay class and test all the methods.

For Example:

If input list entered by user is: ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind',
'apricot']
words_with_length (5) should return ['apple', 'tuple', 'nayan', 'grind']
starts_with ('a') should return ['apple', 'apricot']
ends_with ('d') should return ['find', 'grind']
palindromes () should return ['malayalam', 'nayan']
only ('bna') should return ['banana']
avoids ('amkd') should return ['set', 'tuple', 'list']
"""
class WordPlay:
    def __init__(self,l):
        self.l = l

    def words_with_length(self,length):
        s = []
        for i in self.l:
            if len(i) == length:
                s.append(i)
        return s
        
    def starts_with(self,char1):
        s = []
        for i in self.l:
            if i.startswith(char1):
                s.append(i)
        return s
                
    def ends_with(self,char2):
        s = []
        for i in self.l:
            if i.endswith(char2):
                s.append(i)
        return s

    def palindromes(self):
        s = []
        for i in self.l:
            if i == i[::-1]:
                s.append(i)
        return s
        
    def only(self,str1):
        s = []
        allowed = set(str1.lower())
        for i in self.l:
            if set(i.lower()).issubset(allowed):
                s.append(i)
        return s
            
    def avoids(self,str2):
        s = []
        banned = set(str2.lower())
        for i in self.l:
            bad = False
            for ch in banned:
                if ch in i.lower():
                    bad = True
                    break
            if not bad:
                s.append(i)
        return s


w = WordPlay(["apple","banana","find","dictionary","set","tuple","list",
              "malayalam","nayan","grind","apricot"])

print(w.words_with_length(5))
print(w.starts_with("a"))
print(w.ends_with("d"))
print(w.palindromes())
print(w.only('bna'))
print(w.avoids('amkd'))
