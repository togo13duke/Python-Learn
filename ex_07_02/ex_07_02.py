"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid input")
    quit()

toal = 0.0
count = 0
search_word = "X-DSPAM-Confidence:"
for line in fh:
    if not line.startswith(search_word):
        continue

    x_dspam_conf_len = len(search_word)
    pos = line.find(search_word) + x_dspam_conf_len
    num = float(line[pos:].strip())
    toal += num
    count += 1

print("Average spam confidence:", toal/count)

