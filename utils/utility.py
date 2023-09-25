import logging
import os
from pathlib import Path
import heapq
import heapq
from collections import defaultdict
import random
import sys
import time

class Logger:
    def get_logging_object(self, name, log_level=logging.DEBUG) -> logging:
        """The function get_logging_object returns the logging object.
        Returns:
            logger: Returns the logging object.
        """
        log_file = f'./api.log'
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        f_formatter = logging.Formatter(
            "%(levelname)s - %(name)s - %(asctime)s - %(funcName)s - %(message)s",
            datefmt="%d-%b %H:%M:%S",
        )
        file_handler = logging.FileHandler(log_file, "a")
        file_handler.setFormatter(f_formatter)
        s_formatter = logging.Formatter(
            "%(levelname)s - %(name)s - %(asctime)s - %(funcName)s - %(message)s ",
            datefmt="%d-%b %H:%M:%S",
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(s_formatter)
        # logger.addHandler(file_handler)
        logger.propagate = False
        logger.addHandler(stream_handler)
        return logger


logger = Logger().get_logging_object(__name__)

def get_compression_ratio(f1, f2):
  return int(os.path.getsize(f1)/ os.path.getsize(f2))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
      print(self.val)
      head = self.next
      while(head is not None):
        print(head.val)
        # eval(head.val)
        head=head.next
      return ""

def create_linked_list_from_array(arr):
  head = ListNode(arr.pop(0))
  temp= head
  for each in arr:
    temp.next = ListNode(each)
    temp = temp.next
  return head

def print_tree(root):
    queue = list()
    queue.append(root.left)
    queue.append(root.right)
    ln = len(queue)
    print(root.val,"\n")
    while(ln > 0):
        while(ln>0):
            el = queue.pop(0)
            if el:
                print(el.val,end=" ")
                queue.append(el.left)
                queue.append(el.right)
            ln-=1
        print("\n")
        ln = len(queue)
    return ""
def swap_Node_val(a,b):
   temp = a.val
   a.val = b.val
   b.val = temp

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def timer(fun):
  def wraps(*args):
    start_time = time.time()
    output = fun(*args)
    end_time = time.time()
    logger.info(f'Time Taken by {fun.__name__} -> {(end_time-start_time):.6f}ms')
    return output
  return wraps

def Graph():
  def __init__(self, arr):#letarr beadjacency 
    self.graph = defaultdict(list)
    for each in arr:
      self.graph[each][0].append(each[1])
      self.graph[each[1]].append(each[0])

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(root: TreeNode):
        if root==None or root.val=='None':
            return False  
        if (root.left==None and root.right==None):
            return True
        else:
            return False

def insertLevelOrder(array: list,i,n)-> TreeNode:
    root = None
    # i ,n= 0,len(array)
    # Base case for recursion 
    if i < n:
        root = TreeNode(array[i]) 
        # insert left child 
        root.left = insertLevelOrder(array, 2 * i + 1, n)
        # insert right child 
        root.right = insertLevelOrder(array, 2 * i + 2, n)          
    return root


colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
    }

def create_cefd_banner():
    banner = r"""
 ________          _______           ________      ________     
|\   ____\        |\  ___ \         |\  _____\    |\   ___ \    
\ \  \___|        \ \   __/|        \ \  \__/     \ \  \_|\ \   
 \ \  \            \ \  \_|/__       \ \   __\     \ \  \ \\ \  
  \ \  \____        \ \  \_|\ \       \ \  \_|      \ \  \_\\ \ 
   \ \_______\       \ \_______\       \ \__\        \ \_______\
    \|_______|        \|_______|        \|__|         \|_______|
                                                                
    """
    reset = "\033[0m"
    res = ''
    avail_colors = [each for each in colors.keys()]
    for each in banner:
      if each!=' ':
         res+=f'{colors[random.choice(avail_colors)]}{each}{reset}'
      else:
         res+=' '
    return res


def print_colored(text, color):
    reset = "\033[0m"
    if color in colors:
        return f"{colors[color]}{text}{reset}"
    else:
        return text

def print_progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f"\r[{arrow + spaces}] {int(progress * 100)}%")
    sys.stdout.flush()