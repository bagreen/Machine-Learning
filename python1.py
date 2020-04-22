s = 'sphinx of black quartz judge my vow'

nums = [3, -4, 7, -2, 0, 8]

n = 10

# Global temperatures (difference from 20th century average in degrees centigrade), 1880 through 2019
# From https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2019
temps = [-0.12, -0.09, -0.10, -0.18, -0.27, -0.25, -0.24, -0.28, -0.13, -0.08, -0.34, -0.25, -0.30, -0.33, -0.31, -0.24, -0.09, -0.10, -0.27, -0.15, -0.07, -0.15, -0.25, -0.37, -0.45, -0.28, -0.21, -0.38, -0.43, -0.44, -0.40, -0.44, -0.34, -0.32, -0.14, -0.09, -0.32, -0.39, -0.30, -0.25, -0.23, -0.16, -0.24, -0.25, -0.24, -0.18, -0.07, -0.17, -0.18, -0.33, -0.11, -0.06, -0.12, -0.26, -0.11, -0.16, -0.12, -0.01, -0.02, 0.01, 0.16, 0.27, 0.11, 0.10, 0.28, 0.18, -0.01, -0.04, -0.05, -0.07, -0.15, 0.00, 0.04, 0.13, -0.10, -0.13, -0.18, 0.07, 0.12, 0.08, 0.05, 0.09, 0.10, 0.12, -0.14, -0.07, -0.01, 0.00, -0.03, 0.11, 0.06, -0.07, 0.04, 0.19, -0.06, 0.01, -0.07, 0.21, 0.12, 0.23, 0.28, 0.32, 0.19, 0.36, 0.17, 0.16, 0.23, 0.38, 0.39, 0.29, 0.45, 0.39, 0.24, 0.28, 0.34, 0.47, 0.32, 0.51, 0.65, 0.44, 0.42, 0.57, 0.62, 0.64, 0.58, 0.67, 0.64, 0.62, 0.54, 0.64, 0.72, 0.58, 0.64, 0.67, 0.74, 0.93, 0.99, 0.91, 0.83, 0.95]

print('Palindrome')
print('True' if s == s[::-1] else 'False')
print()

print('Vowel Removal')
print(''.join([l for l in s if l.lower() not in ['a', 'e', 'i', 'o', 'u']]))
print()

print('Word Reversal')
print(' '.join(word[::-1] for word in s.split()))
print()

print('Strictly Increasing')
print('True' if nums == sorted(nums) else 'False')
print()

print('Negative Flattening')
print([num * 0 if num < 0 else num * 1 for num in nums])
print()

print('Digit Sums')
# messy, but basically converts the integer into a string, splits it into each char (digit), then converts these into ints, then sums them
print([x * 1 for x in range(100) if sum(list(map(int, list(str(x))))) % 5 == 0])
print()

print('Climate Change')
loop = 0
# also messy, basically it is first changing temps into a list of tuples with the index and the value, then sorting this by hottest temp, then taking only the top n, then switching the placement of index and value, and sorting by index, so we can see how many of the top n temps are in the last n years
for year, temp in sorted([(t[1], t[0]) for t in sorted(list(zip(temps, range(len(temps)))), reverse=True)[:n]], reverse=True):
    if year >= (139 - n):
        loop += 1
    else:
        break
print(loop)

