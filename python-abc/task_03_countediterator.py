#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0
    
    def __next__(self):
        try:
            item = next(self.iterable)
            self.count += 1
            return item
        except StopIteration:
            raise(StopIteration)
    def get_count(self):
        return self.count
        