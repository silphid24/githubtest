"""
step
1. get file names
2. for each file -rename(delete 0~9)

"""


import os

def rename_files():
	# 1. get the file name in folder in python
	file_list = os.listdir(r"C:\Users\Park\Desktop\rename_test")
	print (file_list)
	saved_path = os.getcwd()
	os.chdir(r"C:\Users\Park\Desktop\rename_test")

	# 2. for each file, rename filename
	for file_name in file_list:
		print("Old Name - "+ file_name)
		print("New Name - "+ file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(saved_path)

rename_files()

if __name__ == '__main__':
	main()