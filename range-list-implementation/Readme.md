# RangeList
RangeList is a class that maintains a list of integer ranges.
Upon adding/removing an interval, the class ensures that no overlapping ranges exist.

Ranges are defined as pairs of integers, for example: [1, 5) - which includes integers: 1, 2, 3, and 4.

## How to Run
Python 3 should be installed.
cd to the directory where RangeList.py is

Run the script:
`python RangeList.py`

## Methods
add(new_range): This will add a range to the list and deal with overlapping ranges.
remove(old_range): Removes a range from the list and deals with overlapping ranges.
toString(): Returns a string representation of the RangeList. It will be outputted where a range is [1,5)
