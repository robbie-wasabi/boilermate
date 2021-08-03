import os 
import argparse 

INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
UNEQUAL_SUBSTRING_COUNT = "Error: You need to provide the same amount of substrings as replacement substrings"

def validate_file(file_name): 
	''' 
	validate file name and path. 
	'''
	if not valid_path(file_name): 
		print(INVALID_PATH_MSG%(file_name)) 
		quit() 
	elif not valid_filetype(file_name): 
		print(INVALID_FILETYPE_MSG%(file_name)) 
		quit() 
	return
	
def valid_filetype(file_name): 
	return file_name.endswith('.txt') # TODO: support other file types

def valid_path(path): 
	return os.path.exists(path) 

# def read(args): 
# 	print(args)
# 	file_name = args.read[0] 
# 	validate_file(file_name) 

# 	# read and print the file content 
# 	with open(file_name, 'r+') as f: 
# 		# print(f.read()) 
# 		text = f.read().replace('goodbye', 'hello')
# 		f.seek(0)
# 		f.write(text)
# 		print(f.read())

# def rename(args): 
# 	old_filename = args.rename[0] 
# 	new_filename = args.rename[1] 
# 	validate_file(old_filename) 
# 	if not valid_filetype(new_filename): 
# 		print(INVALID_FILETYPE_MSG%(new_filename)) 
# 		exit() 
# 	os.rename(old_filename, new_filename) 
# 	print("Successfully renamed {} to {}.".format(old_filename, new_filename))

def boil(file_name, substrings, replacement_strings): 
	print(file_name, substrings, replacement_strings)

	if len(substrings) != len(replacement_strings):
		print(UNEQUAL_SUBSTRING_COUNT)
		return
	
	with open(file_name, 'r+') as f: 
			text = f.read().replace(substrings[0], replacement_strings[0])
			f.seek(0)
			f.write(text)
			print(f.read())

		# TODO: multiple substrings
		# for i in range(len(substrings)):
		# 	text = f.read().replace(substrings[i], replacement_strings[i])
		# 	f.seek(0)
		# 	f.write(text)
		# 	print(f.read())


def main(): 
	parser = argparse.ArgumentParser(description = "A text file manager!") 

	parser.add_argument("-f", "--file", type = str, nargs = 1, 
						metavar = "file_name", default = None, 
						help = "Specify a file.") 

	parser.add_argument("-c", "--change", type = str, nargs = 1, 
						metavar = "substring", default = None, 
						help = "Specify a substring to replace.") 

	parser.add_argument("-t", "--to", type = str, nargs = 1, 
						metavar = "replacement_substring", default = None, 
						help = "Specify a replacement substring.")

	# parse the arguments from standard input 
	args = parser.parse_args() 
	
	# calling functions depending on type of argument 
	if args.file != None and args.change != None and args.to != None: 
		boil(args.file, args.change, args.to) 

if __name__ == "__main__": 
	# calling the main function 
	main() 
