# Python useful built-in method


## Rabin-Karp
187 Repeated DNA Sequences

## Modify part of a list in a function

s[lo:hi] = self.reverseWord(s[lo:hi])[:]


## ord(ch)

The ord() function returns an integer representing the Unicode character.

## chr(int)


## int(x, base=10)

Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x is a number, return x.__int__(). For floating point numbers, this truncates towards zero.

## dict.keys() and dict.values()

## dictionary.get(keyname, value)
value:

Optional. A value to return if the specified key does not exist.
Default value None


## heapq (Min-heap)

    heapq.heappush(heap, item)

    heapq.heappop(heap)

    heapq.heappushpop(heap, item)

    heapq.heapify(x)

    heapq.heapreplace(heap, item)

According to the heapq documentation, the way to customize the heap order is to have each element on the heap to be a tuple, with the first tuple element being one that accepts normal Python comparisons.

## collections.Counter
    class Solution(object):
        def topKFrequent(self, words, k):
            count = collections.Counter(words)
            candidates = count.keys()
            candidates = sorted(candidates, key = lambda w: (-count[w], w))
            return candidates[:k]
## for/else

## list.clear()

## xrange

in Python 2: range generates a list while xrange is a sequence object that evaluates lazily.

In Python 3: same


## range(start, end, step)

## string.strip(characters)

The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

## [[1]*4 for _ in range(3)] and [[1]*4] * 3

## divmod(numerator, denominator)

## string.split(separator, maxsplit)

## string.join(iterable)

## list.append & list + listh

## results += [x | (1 << i) for x in reversed(results)]

## for layer in reversed(range(0, n-1)) == for layer in range(n-2, -1, -1)

## collections.OrderedDict.
* move_to_end(key, last=True)
* popitem(last=True)


## Morris Inorder Tree Traversal
https://www.youtube.com/watch?v=wGXB9OWhPTg

## list[::-1]


## deque([])
pop()

popleft()

append(x)

appendleft(x)


## isdigit does not detect negative number


## python // negative round down
Can use int(num1 / num2)

## Custom comparator
class LargerNumKey(str):

    def __lt__(x, y):

        return x+y > y+x

# Details

## Check empty List, n == 0, root == None



