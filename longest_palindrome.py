"""
Approach 1: iteratively check if the string is palindrome - in each iteration move the left and right position
iterate through each item
check all items from left to the item -> item and farthest left if at any position matches, add and break
check all items from right to th item -> item and farthest right if at any position matches, add and break
"""

def find_longest_palindrome(s):
    d = {}
    _len = len(s)
    if s == s[::-1]:
        return s
    for i in range(_len):
        ss = s[i:i+1]
        if ss == ss[::-1]:
            d[len(ss)] = ss

        for j in range(i+1):
            if s[j] != s[i]:
                continue
            ss = s[j:i+1]
            if ss == ss[::-1]:
                d[len(ss)] = ss
                break

        for k in range(i+1,_len):
            if s[k] != s[i+1]:
                continue
            ss = s[i+1:k+1]
            if ss == ss[::-1]:
                d[len(ss)] = ss
                break
        
        ss = s[i-1:i+2]
        if ss == ss[::-1]:
            d[len(ss)] = ss

    _max = max(d)
    return d[_max]
    
# s = 'd' * 500
s = "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"
print(find_longest_palindrome(s))
    