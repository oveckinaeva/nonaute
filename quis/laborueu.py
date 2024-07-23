# Initialize empty list
rowheaders = []

# Add row headers to the list
rowheaders.append('Header1')
rowheaders.append('Header2')
rowheaders.append('Header3')

# Access and print each row header
for header in rowheaders:
    print(header)

# Another way to print each row header using a list comprehension
[print(header) for header in rowheaders]
