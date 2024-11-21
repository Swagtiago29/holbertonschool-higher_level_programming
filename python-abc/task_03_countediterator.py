#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.count = 0
        self.iterable = iter(iterable)
    
    def __next__(self):
        try:
            self.count += 1
            return next(self.iterable)
        except StopIteration:
            raise(StopIteration)
    def get_count(self):
        return self.count
        