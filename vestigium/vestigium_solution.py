input_file = open("input.txt", "r")
num_test_cases = int(input_file.readline())

"""
Vestigium:

Returns three values given a matrix:
	1. The trace (the sum of the upper-left-to-lower-right diagonal)
	2. The number of rows that contain repeated elements
	3. The number of columns that contain repeated elements
"""
for i in range(1, num_test_cases + 1):
	rows_with_repeats = set()
	columns_with_repeats = set()
	diag_sum = 0
	matrix_size = int(input_file.readline())

	# Using a map to keep track of column values. Map of key=column index value=array of found nums 
	col_map = {}

	for j in range(0, matrix_size):
		nums_found_in_row = set()
		row = input_file.readline().split()
		for k in range(0, matrix_size):
			num = int(row[k])

			# keep track of duplicate numbers in rows
			if num in nums_found_in_row:
				# found a repeat in the row
				rows_with_repeats.add(j)
			else:
				nums_found_in_row.add(num)
			
			# keep track of the diagonal sum
			if j == k:
				diag_sum += num

			# keep track of duplicate numbers in columns
			# for every column, we add it to the col_map with values for each digit in the column
			if k not in col_map:
				col_map[k] = []
				col_map[k].append(num)
			elif num in col_map[k]:
				# found a repeat in the column
				columns_with_repeats.add(k)
			else:
				col_map[k].append(num)

	print("Case #{}: {} {} {}".format(i, diag_sum, len(rows_with_repeats), len(columns_with_repeats)))
