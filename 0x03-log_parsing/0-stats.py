#!/usr/bin/python3
"""
Log parsing: reads stdin line by line and computes metrics.

LOGIC:
The main goal of this program is to read input from standard input
line by line, parse each line and compute some metrics, and then
print statistics after every 10 lines and/or when the program
receives a keyboard interrupt signal (CTRL + C).

To achieve this, I first initialize a few variables such as the
line count, total file size and a dictionary to store the number of
occurrences of each status code.

Next, I use a try-except block to handle the case when the program
receives a keyboard interrupt signal. Within the try block, I use a
for loop to read each line of input from standard input.

For each line, I increment the line count by 1 and split the line
into words using the split() method. I then check if the length of
the resulting list is 9 and if the 8th element is a digit. If both
conditions are true, I add the value of the 8th element to the
total file size.

I also check if the 7th element of the split line is a valid status
code, and if it is, I increment the value of the corresponding key
in the status codes dictionary by 1.

After every 10 lines, I call the print_stats() function which
prints the current total file size and the number of occurrences of
each status code in the dictionary. I then reset the line count and
continue with the loop.

At the end of the loop, I call the print_stats() function one more
time to print the statistics for the remaining lines.

If a keyboard interrupt signal is received while the loop is still
running, the program prints the statistics for the lines processed
so far and raises the KeyboardInterrupt exception to terminate the program.
"""

import sys


def print_stats(file_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    count = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        # read stdin line by line
        for line in sys.stdin:
            # increment line count
            count += 1
            # split line into list of strings
            split_line = line.split()
            # validation for correct format of line (2 <= elements <= 9)
            if len(split_line) >= 2 and len(split_line) <= 9:
                # check that the file size is a valid integer
                if split_line[-1].isdigit():
                    # add the file size to the total
                    file_size += int(split_line[-1])
                # check that the status code is valid
                if split_line[-2] in status_codes:
                    # increment the status code count
                    status_codes[split_line[-2]] += 1
            # print stats every 10 lines
            if count % 10 == 0:
                print_stats(file_size, status_codes)
        # print final stats at the end
        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        # print final stats if keyboard interrupt
        print_stats(file_size, status_codes)
        raise
