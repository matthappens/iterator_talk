class MyIterable(object):

    def __iter__(self):
        return MyIterator()


class MyIterator(object):

    def __init__(self):
        self.index = 0
        self.elements = [1, 2, 3, 4, 5]

    def next(self):
        if self.index < len(self.elements):
            nextElement = self.elements[self.index]
            self.index += 1
            return nextElement
        else:
            raise StopIteration()


# though they are often the same thing
class MyConvenientIerator(object):

    def __init__(self):
        self.index = 0
        self.elements = [1, 2, 3, 4, 5]

    # satisfies Iterable
    def __iter__(self):
        return self

    # satisfies Iterator
    def next(self):
        if self.index < len(self.elements):
            nextElement = self.elements[self.index]
            self.index += 1
            return nextElement
        else:
            raise StopIteration()

print("Looping over separate iterators")
for e in MyIterable():
    print e

print("Looping over my convenient iterator")
for e in MyConvenientIerator():
    print e

# syntactic sugar free version
print("Looping through syntactic sugar free")
list_of_stuff = [1,2,3,4,5,6,7,8,9,10]
my_iterator = iter(list_of_stuff)
while True:
    try:
        element = my_iterator.next()
        print(element)
        # do your thing with element
    except StopIteration:
        break



class SortedMap(dict):
    def __iter__(self):
        self.cursor = 0
        self.sorted_keys = sorted(self.keys())
        return self
    def next(self):
        if self.cursor < len(self.sorted_keys):
            nextElement = self[self.sorted_keys[self.cursor]]
            self.cursor += 1
            return nextElement
        else:
            raise StopIteration()
