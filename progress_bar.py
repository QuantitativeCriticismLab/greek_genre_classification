# From https://stackoverflow.com/a/34325723

__prev_str_length = None

# Print iterations progress
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
	"""
	Call in a loop to create terminal progress bar
	@params:
		iteration   - Required  : current iteration (Int)
		total       - Required  : total iterations (Int)
		prefix      - Optional  : prefix string (Str)
		suffix      - Optional  : suffix string (Str)
		decimals    - Optional  : positive number of decimals in percent complete (Int)
		length      - Optional  : character length of bar (Int)
		fill        - Optional  : bar fill character (Str)
	"""
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	s = '%s |%s| %s%% %s' % (prefix, bar, percent, suffix)
	global __prev_str_length
	if __prev_str_length:
		print(' ' * __prev_str_length, end='\r') #Clear out previous bar to prevent lingering characters if current bar is shorter
	print(s, end='\r')
	__prev_str_length = len(s)
	# Print New Line on Complete
	if iteration == total: 
		print()

if __name__ == '__main__':
	# 
	# Sample Usage
	# 

	from time import sleep

	# A List of Items
	items = list(range(0, 57))
	l = len(items)

	for i in range(l + 1):
		# Do stuff...
		sleep(0.1)
		# Update Progress Bar
		print_progress_bar(i, l, prefix='Progress:', suffix='Complete', length=50)

	# Sample Output
	# Progress: |█████████████████████████████████████████████-----| 90.0% Complete
