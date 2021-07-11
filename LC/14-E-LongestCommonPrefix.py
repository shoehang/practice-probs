def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    strs.sort(key=len)
    res = ''

    if not len(strs[0]):
        return res

    first = strs[0][0]

    for word in range(1,len(strs)):
        if first == strs[word][0]:
            continue
        return ''

    res += first

    for char in strs[0][1:]:
        for word in range(1,len(strs)):
            if (res + char) != strs[word][0:len(res)+1]:
                return res
            res += char
    return res

print(longestCommonPrefix(["flower","flow","flight"]))

#https://leetcode.com/problems/longest-common-prefix/discuss/354496/Python3-list(zip(*str))

#o(n) solution
