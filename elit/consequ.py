import numpy as np

# Assuming you have a histogram array with frequency values
histogram = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])

# Merging bins with a bin size of 2.5
bin_size = 2.5
merged_bins = np.column_stack((np.arange(0, histogram.shape[0] * bin_size, bin_size), np.sum(histogram, axis=1)))

# The resulting array will have merged bins with the specified bin size
print(merged_bins)
