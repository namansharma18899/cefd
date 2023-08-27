from utility import timer


class RLE:
    """
    RLE(Run-Length Encoding is a way of lossless compression where we compress the main string by
    frequently occurring  characters in a substring with the notation of CX where C is the character which
    is repeating and X represents it's frequency)
    """
    def __init__(self) -> None:
        pass

    @timer
    def compress(self, chars) -> int:
        p1 = 0
        result_len = 0
        result_str_pointer = 0
        while(p1 < len(chars)):
            chars[result_str_pointer] = chars[p1]
            p2 = 0
            for j in range(p1+1, len(chars)):
                if chars[j]!=chars[p1]: break
                else: p2+=1
            if p2==0: # means 1gle char
                p1+=1
                result_len+=1 # adding curr char in result_len
                result_str_pointer+=1
            else: #p1 + number of characters
                char_substr = str(p2+1) #num of char + 1
                for subs_ind in range(0, len(char_substr)): 
                    chars[result_str_pointer+1+subs_ind]= char_substr[subs_ind]
                result_str_pointer+=len(char_substr) + 1
                result_len+=len(char_substr) + 1 # 1 for the alphabet itself
                p1+=p2+1
        return result_len