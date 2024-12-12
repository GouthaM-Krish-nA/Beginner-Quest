name=list(map(str,input().split(',')))
l=list(map(int,input().split(',')))
d={}
common=[]
for a,b in zip(name,l):
  if b in d:
    d[b].append(a)
  else:
    d[b]=[a]
for i,j in d.items():
  if len(j)>1:
    for a in range(len(j)):
      for b in range(a+1,len(j)):
        common.append((j[a]+' '+j[b]))
print(len(common))
print(common)








# # Input
# names = input("Enter names (comma-separated): ").split(",")
# dates = list(map(int, input("Enter joining dates (comma-separated): ").split(",")))

# # Dictionary to map joining dates to names
# date_dict = {}

# # Fill the dictionary
# for name, date in zip(names, dates):
#     if date in date_dict:
#         date_dict[date].append(name)
#     else:
#         date_dict[date] = [name]

# # Find pairs of names with the same joining date
# common = []
# for date, people in date_dict.items():
#     if len(people) > 1:
#         # Generate all pairs for this date
#         for i in range(len(people)):
#             for j in range(i + 1, len(people)):
#                 common.append((people[i], people[j]))

# # Output
# print("common:", common)
# print("Count of pairs:", len(common))
