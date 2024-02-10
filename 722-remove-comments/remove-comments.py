import re
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = '\n'.join(source)
        regex_single = r"\/\/.*"
        regex_block_closed = r"(?s:\/\*.*?\*\/)"
        regex_block_not_closed = r"\/\*.*"    
        regex = '|'.join([regex_single, regex_block_closed, regex_block_not_closed])  
        s = re.sub(regex, '', s)
        return list(filter(None, s.split('\n')))