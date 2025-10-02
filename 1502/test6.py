__metadata__ = {
    "course": "Tim's Sandpit",
    "page": "dcl-6",
    "placement": ['example', 'test']
}

# Now with single quotation marks for the list
print("This exercise will go in two places")
for i in range(3):
    for j in range(3):
        print(f"{i} * {j} = {i*j}")
print("done")