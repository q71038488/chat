import os

#讀取檔案
def read_file(filename):
	chat_list = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			chat_list.append(line.strip())
		return chat_list
#整理對話內容
def convert(chat_list):
	new = []
	for line in chat_list:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ':' + line)
	return new
#寫入新檔案
def write_file(new_list):
	with open('output.txt', 'w', encoding='utf-8') as f:
		for line in new_list:
			f.write(line + '\n')
		return '檔案排序完成，已寫入至output.txt'
#主程式
def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		chat_list = read_file(filename)
		new_list = convert(chat_list)
		print(write_file(new_list))
	else:
		print('找不到檔案')

main()