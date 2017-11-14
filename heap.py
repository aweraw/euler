from operator import lt

class Heap:

    def __init__(self, seq, key=lambda x: x, cmp=lt):
        self.key = key
        self.cmp = cmp
        self.len = 0
        self.heap = list()
        self.set = set()

        self.push_many(seq)

    def push(self, item):
        self.heap.append(item)
        self.set.add(item)
        self.len += 1
        self._bubble_up(self.len-1)

    def pop(self):
        if self.len is 0:
            raise IndexError('heap is empty')
        item = self.heap.pop(0)
        self.set.remove(item)
        self.len -= 1
        if self.len:
            self.heap.insert(0, self.heap.pop())
            self._bubble_down(0)

        return item

    def push_many(self,seq):
        for item in seq:
            self.push(item)

    def pop_many(self,n):
        return (self.pop() for x in xrange(n))

    def reorder(self, item):
        i = self.heap.index(item)
        self._bubble_up(i)

    def _children(self, i):
        return (2*i)+1, (2*i)+2

    def _parent(self, i):
        return (i-1)/2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _cmp(self, i, j):
        return self.cmp(self.key(self.heap[i]),self.key(self.heap[j]))

    def _bubble_up(self, i):
        if i is 0:
            return None
        p = self._parent(i)
        if self._cmp(i,p):
            self._swap(i,p)
            self._bubble_up(p)
        else:
            self._bubble_down(i)

    def _bubble_down(self, i):
        c1, c2 = self._children(i)
        if c1 < self.len and c2 < self.len:
            best = c1 if self._cmp(c1,c2) else c2
        elif c1 < self.len:
            best = c1
        elif c2 < self.len:
            best = c2
        else:
            return None
        
        if self._cmp(best,i):
            self._swap(i,best)
            self._bubble_down(best)

    def __contains__(self, item):
        return item in self.set

    def __iter__(self):
        while self.heap:
            yield self.pop()
