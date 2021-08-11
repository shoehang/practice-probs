def romanToInt(self, s: str) -> int:
    rdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M':1000}
    
    #single roman letter
    if s in rdict:
        return rdict[s]
    
    #else more
    # cumulative
    result = rdict[s[0]]
    # prev number
    previous = s[0]
    for char in s[1:]:
        # patten of prev < current ie. IX > 1 -lt 10 == 1 + 10 - (2 * 1) == 9 
        if rdict[previous] < rdict[char]:
            result += rdict[char] - (2 * rdict[previous])
        #else add to cumulative
        elif char in rdict:
            result += rdict[char]
        previous = char
    return result