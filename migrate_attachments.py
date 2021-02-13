# Confluence Attachment Migration Script - Brian Johnson [Atlassian]

import csv
import os
import shutil

# Set this flag to y if you are running this on Windows
windows = 'n'

old_attachment_folder_path = '/Users/bjohnson3/Documents/attachments/ver003'
new_attachment_folder_path = '/Users/bjohnson3/Desktop/new attachments'
csv_file_name_and_path = 'Test1.csv'
file_path_delimiter = '/'

if windows.lower() == 'y':
  file_path_delimiter = '\\'
  print("Running on Windows...")
else:
  print("Running on Linux...")

def create_path_1(id):
	id_1 = id[-3:]
	id_1 = (int(id_1)%250)
	id_1 = str(id_1)
	return id_1

def create_path_2(id):
	if len(id) == 4:
		id_2 = id[-4:-3]
	elif len(id) == 5:
		id_2 = id[-5:-3]
	else:
		id_2 = id[-6:-3]
	id_2 = (int(id_2)%250)
	id_2 = str(id_2)
	return id_2

with open(csv_file_name_and_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(row)
			line_count += 1
		else:
			old_file_path = create_path_1(row[0])
			new_file_path = create_path_1(row[3])
			old_file_path_2 = create_path_2(row[0])
			new_file_path_2 = create_path_2(row[3])
			old_file_path_3 = row[0]
			new_file_path_3 = row[3]
			old_file_path_4 = create_path_1(row[1])
			new_file_path_4 = create_path_1(row[4])
			old_file_path_5 = create_path_2(row[1])
			new_file_path_5 = create_path_2(row[4])
			old_file_path_6 = row[1]
			new_file_path_6 = row[4]
			old_file_path_7 = row[2]		
			new_file_path_7 = row[5]
			old_attachment_path = old_attachment_folder_path + file_path_delimiter + old_file_path + file_path_delimiter + old_file_path_2 + file_path_delimiter + old_file_path_3 + file_path_delimiter + old_file_path_4\
				+ file_path_delimiter + old_file_path_5 + file_path_delimiter + old_file_path_6 + file_path_delimiter + old_file_path_7
			new_attachment_path = new_attachment_folder_path + file_path_delimiter + new_file_path + file_path_delimiter + new_file_path_2 + file_path_delimiter + new_file_path_3 + file_path_delimiter + new_file_path_4\
				+ file_path_delimiter + new_file_path_5 + file_path_delimiter + new_file_path_6 + file_path_delimiter + new_file_path_7
			try:
				os.makedirs(new_attachment_path)
			except OSError:
				print("Unable to create the following directory: %s" % new_attachment_path)
			files = []
			for path, dirnames, filenames in os.walk(old_attachment_path):
				files.extend(os.path.join(path, name) for name in filenames)
			for f in files:
				shutil.copy(f, new_attachment_path)
			line_count += 1
			files = []
	print(f'Processed {line_count - 1} lines.')