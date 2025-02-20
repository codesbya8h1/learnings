# Median of an Integer Stream
# Hard
# Design a data structure that supports adding integers from a data stream and retrieving the median of all elements received at any point.

# add(num: int) -> None: adds an integer to the data structure.
# get_median() -> float: returns the median of all integers so far.
# Example:
# Input: [add(3), add(6), get_median(), add(1), get_median()]
# Output: [4.5, 3.0]
# Explanation:

# add(3)        # data structure contains [3] when sorted
# add(6)        # data structure contains [3, 6] when sorted
# get_median()  # median is (3 + 6) / 2 = 4.5
# add(1)        # data structure contains [1, 3, 6] when sorted
# get_median()  # median is 3.0
# Constraints:
# At least one value will have been added before get_median is called.

class MedianOfAnIntegerStream:
    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def get_median(self) -> float:
        n = len(self.data)
        if n % 2 == 0:
            return (self.data[n//2-1] + self.data[n//2]) / 2
        else:
            return self.data[n//2]

median = MedianOfAnIntegerStream()
median.add(3)
median.add(6)
print(median.get_median())
median.add(1)
print(median.get_median())
