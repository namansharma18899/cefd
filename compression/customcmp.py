import heapq
import sys
from collections import Counter
from compression.cmp_interface import GenericCompressionInterface
import re


class FrequencyHuntCmp(GenericCompressionInterface):
    def __init__(self) -> None:
        super().__init__()
        self.hmap = dict()

    def encode(self, input_str, *args, **kwargs):
        most_freq = self.k_most_frequent_strings(
            input_str, int(10 * (len(input_str.split(" ")) / 100))
        )
        tmp_str = "" + input_str
        for index, val in enumerate(most_freq):
            self.hmap = {f"${index}$": val[1]}
            tmp_str = re.sub(fr"\b{val[1]}\b", f"${index}$", tmp_str)
        return tmp_str
    
    def decode(self, input_str, *args, **kwargs):
        pass

    def k_most_frequent_strings(self, sentence: str, k):
        sentence = sentence.lower()
        words = sentence.split()
        word_counter = Counter(words)
        heap = [(-count, word) for word, count in word_counter.items()]
        heapq.heapify(heap)
        most_frequent_strings = heapq.nsmallest(k, heap)
        return most_frequent_strings


# Example usage
input_sentence = "Leonardo da Vinci, born on April 15, 1452, in Vinci, Italy, is widely regarded as one of the most versatile and ingenious minds in history. His remarkable talents spanned multiple disciplines, including painting, sculpture, anatomy, engineering, and architecture. \
Leonardo's artistic legacy is epitomized by masterpieces such as the Mona Lisa and The Last Supper. His meticulous attention to detail, use of perspective, and innovative techniques revolutionized the art world during the Italian Renaissance. Beyond his artistic prowess, da Vinci's insatiable curiosity and analytical mind led him to explore various scientific and engineering pursuits. \
In the realm of science, Leonardo da Vinci made groundbreaking observations in anatomy, dissecting and sketching detailed studies of the human body. His notebooks are filled with accurate anatomical drawings, showcasing his keen understanding of anatomy and physiology. Many of his ideas, however, were ahead of his time and not fully recognized or appreciated during his lifetime. \
Leonardo's engineering designs encompassed concepts for flying machines, military weaponry, and hydraulic systems. His fascination with flight led him to envision helicopters and ornithopters, although these designs were not realized until centuries later. His notebooks are a treasure trove of imaginative ideas that demonstrate his visionary approach to technology. \
Despite his numerous contributions, Leonardo da Vinci was not solely a painter, scientist, or engineer; he was a true polymath who seamlessly bridged the gap between art and science. His interdisciplinary approach to knowledge continues to inspire and captivate people across the globe, reminding us of the boundless possibilities that arise when creativity and intellect converge in a single extraordinary mind. Leonardo da Vinci's legacy endures as a testament to the power of human curiosity and the pursuit of excellence in multiple domains."

org = sys.getsizeof(input_sentence)
print(sys.getsizeof(input_sentence))
var = FrequencyHuntCmp()
var = sys.getsizeof(var.encode(input_str=input_sentence))
print(var)
print('differnce -> ', int(((org-var)/org)*100), ' %' )