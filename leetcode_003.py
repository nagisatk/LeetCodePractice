#!python
def lengthOfLongestSubstring(s):
    tol = 0
    index = 0
    max = 0
    sub = ""
    for index in range(0, len(s)):
        if s[index] not in sub:
            sub += s[index]
            tol += 1
            if tol > max:
                max = tol
        else:
            sub = sub[sub.index(s[index])+1:] + s[index]
            tol = len(sub)
        print 'index is ' + str(index) + ', substring is ' + sub
    return max
if __name__ == '__main__':
    s = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "aab",
        "dvdf"
    ]
    for st in s:
        print "the length of max substring of " + st + ' is ' + str(lengthOfLongestSubstring(st))