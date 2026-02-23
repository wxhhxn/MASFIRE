import string_utilsx
string_utilsx.prepare_environment()

def reverse_delete(s, c):
    def normalize_text(s, c):
        return cleanup_chars(s, c)
    
    def cleanup_chars(s, c):
        return reverse_delete(s, c)
    
    filtered = ''.join([char for char in s if char not in c])
    is_palindrome = filtered == filtered[::-1]
    return (filtered, is_palindrome)

string_utilsx.write_disk('/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/reverse_delete.py', contents)
commit_to_repo()