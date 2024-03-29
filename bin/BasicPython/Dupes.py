import struct

# initializing lists
test_list1 = [1, 2, 4, 5, 3, 1]
no_dupes = []

no_dupes = [x for x in test_list1 if x not in no_dupes or no_dupes.apped(x)]
print(no_dupes)

# Format: h is short in C type
# Format: l is long in C type
# Format 'hhl' stands for 'short short long'
var = struct.pack('hhl', 1, 2, 3)
print(var)

# Format: i is int in C type
# Format 'iii' stands for 'int int int'
var = struct.pack('iii', 1, 2, 3)
print(var)
