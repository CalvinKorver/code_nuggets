"""
Task: Implement a class named 'RangeList'
A pair of integers define a range, for example: [1, 5). This range includes
integers: 1, 2, 3, and 4.
A range list is an aggregate of these ranges: [1, 5), [10, 11), [100, 201)
"""


class RangeList:
    def __init__(self):
        self.ranges = []  # List to keep track of our ranges

    def add(self, new_range):
        """
        Adds a range to the list. If the new range that is added overlaps with an existing range,
        the algorithm will take care of the merging necessary to keep the list in a state so that
        there is no overlapping.

        @param new_range - Array of two integers that specify beginning and end of the new range.
        """

        res = []

        # If there are no ranges already, just append it to our class variable and return from the function
        if len(self.ranges) == 0:
            self.ranges.append(new_range)
            return

        # Otherwise, iterate through our existing ranges
        for i, interval in enumerate(self.ranges):

            # If the end of the new range is less than our current interval's start, we can add
            # the new interval to our temporary list and then the rest of the ranges.
            # This is akin to pre-appending our new interval
            if new_range[1] < interval[0]:
                res.append(new_range)
                self.ranges = res + self.ranges[i:]
                return

            # Otherwise, if the new range's start is larger than the current range's end, simply append the
            # current interval to the res, preserving the order
            elif new_range[0] > interval[1]:
                res.append(interval)

            # Finally, if the new range needs to be merged into the current merge, simply take the maximum and
            # the minimum of the current range start/end as well as the new interval's start/end
            else:
                new_range = [min(new_range[0], interval[0]), max(new_range[1], interval[1])]

        # Append our new range (notice the first if statement above returns, so we don't add it twice
        res.append(new_range)

        # Update our class variable.
        self.ranges = res

    def remove(self, old_range):
        """
        Removes a range from the list
        @param [start, end] range - Array of two integers that specify beginning and end of range.
        """

        # If it's a simple matter of removing it, short circuit the algorithm and just remove it
        if old_range in self.ranges:
            self.ranges.remove(old_range)
            return

        merged = []
        for interval in self.ranges:

            # Essentially, if there are no overlaps between the current interval and the one to be removed,
            # we can simply add the current interval to our merged list
            if interval[0] > old_range[1] or interval[1] < old_range[0]:
                merged.append(interval)

            # Otherwise, there are overlaps
            else:

                # Fun part: If the current interval's end is greater than the removed interval's end, we have a case
                # like this (1,5) remove (1,3), return (3,5)
                if interval[1] > old_range[1]:
                    merged.append([old_range[1], interval[1]])

                # If the current interval's start is less than the removed interval's start, we have a case like
                # this (3,5) remove (4,5), return 3,4
                if interval[0] < old_range[0]:
                    merged.append([interval[0], old_range[0]])

        # Make sure they are sorted.
        self.ranges = sorted(merged)

    def toString(self):
        """
        Simple toString method that concats the intervals.
        """
        res = []
        for r in self.ranges:
            res.append("[" + str(r[0]) + ", " + str(r[1]) + ")")

        return ", ".join(res)


def main():
    runSampleOutput = True  # Change to True if you want to run the sample output
    if runSampleOutput:
        rl = RangeList()
        print(rl.toString())
        rl.add([1, 5])
        print(rl.toString())
        rl.add([10, 20])
        print(rl.toString())
        rl.add([20, 20])
        print(rl.toString())
        rl.add([20, 21])
        print(rl.toString())
        rl.add([2, 4])
        print(rl.toString())
        rl.add([3, 8])
        rl.remove([10, 10])
        print(rl.toString())  # Should be: "[1, 8) [10, 21)"
        rl.remove([10, 11])
        print(rl.toString())  # Should be: "[1, 8) [11, 21)"
        rl.remove([15, 17])
        print(rl.toString())
        rl.remove([3, 19])
        print(rl.toString())  # Should be: "[1, 3) [19, 21)"


if __name__ == "__main__":
    main()
