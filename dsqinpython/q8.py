si = "madam"
d = {}
s, sup = [], ""

# Collect unique characters
for i in si:
    if i not in s:
        s.append(i)

# Create a dictionary with counts of each character
for i in s:
    d[i] = si.count(i)

# Sort the dictionary by values (character frequency), without using item[0]
sp = dict(sorted(d.items(), key=lambda item: item[1]))

# Construct the sorted output string based on frequency
for i in sp:
    sup += i * d[i]  # Repeat the character by its count and add to `sup`

print(sup)
