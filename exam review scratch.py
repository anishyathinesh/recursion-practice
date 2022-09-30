"""
with open("words.txt") as fd:

    fd=open("words.txt")
    line_count = 0
    char_count = 0
    for line in fd:
        for ch in line.strip():
            char_count += 1	
        line_count+=1

    print(line_count, char_count)
"""
def is_palindrome(string, reverse_result, s):
    if s == "":
        pass
    else:
        reverse_result = reverse_result + s[-1]
        print(reverse_result)
        s = s[:-1]

        is_palindrome(s, reverse_result)
        
    if reverse_result == original_S:
        return True
    else:
        return False
        

if __name__ == "__main__":
    print(is_palindrome("redivider", "", ))

        
    
