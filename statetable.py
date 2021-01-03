from tabulate import tabulate

# example mindtap quiz15 q11
rowcount = int(input('How many rows? '))
outcolumns = int(input('How many output columns? '))
rows = []
dict = {}
for i in range(rowcount):
    r = input('enter input (ie: aaagk1000): ')
    rows.append(r)
    if r[-outcolumns:] in dict:
        dict[r[-outcolumns:]].append(r)
    else:
        dict[r[-outcolumns:]] = [r]

sortedoutputs = list(sorted(dict.keys()))
outrows = []
for k in sortedoutputs:
    for item in dict[k]:
        columns = []
        for i in range(len(item)):
            columns.append(item[i])
        outrows.append(columns)

print(tabulate(tabular_data=outrows, tablefmt="grid"))