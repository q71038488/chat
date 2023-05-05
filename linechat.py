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
	sec = 0
	mini = 0
	hr = 0
	me_word_count = 0
	me_sticker_count = 0
	me_pic_count = 0
	me_sound_count = 0
	me_call_count = 0
	me_nocatch_count = 0
	me_callcancet_count = 0
	na_word_count = 0
	na_sticker_count = 0
	na_pic_count = 0
	na_sound_count = 0
	na_call_count = 0
	na_callcancet_count = 0
	na_nocatch_count = 0
	now_name = None
	for line in chat_list:
		if '2022/' in line or '2023/' in line or len(line) < 1:
			continue
		else:
			s = line.split()
			print(s)
			if len(s) < 3:
				if now_name == '肉汁':
					for t in s:
						me_word_count += len(t)
				if now_name == 'Na':
					for t in s:
						na_word_count += len(t)
			else:
				time = s[0]
				name = s[1]
				if name == '肉汁':
					now_name = '肉汁'
					if s[2] == '[貼圖]':
						me_sticker_count += 1
					elif s[2] == '[照片]':
						me_pic_count += 1
					elif s[2] == '[語音訊息]':
						me_sound_count += 1
					elif s[2] == '無人接聽':
						me_call_count += 1
					elif s[2] == '未接來電':
						me_nocatch_count += 1
					elif s[2] == '您已結束通話':
						me_callcancet_count += 1
					elif s[2] == '通話時間':
						d = s[3].split(':')
						if len(d) == 3:
							sec += int(d[2])
							mini += int(d[1])
							hr += int(d[0])
						elif len(d) == 2:
							sec += int(d[1])
							mini += int(d[0])
					else:
						for t in s[2:]:
							me_word_count += len(t)
				elif name == 'Na':
					now_name = 'Na'
					if s[2] == '[貼圖]':
						na_sticker_count += 1
					elif s[2] == '[照片]':
						na_pic_count += 1
					elif s[2] == '[語音訊息]':
						na_sound_count += 1
					elif s[2] == '無人接聽':
						na_call_count += 1
					elif s[2] == '未接來電':
						na_nocatch_count += 1
					elif s[2] == '您已結束通話':
						na_callcancet_count += 1
					elif s[2] == '通話時間':
						d = s[3].split(':')
						if len(d) == 3:
							sec += int(d[2])
							mini += int(d[1])
							hr += int(d[0])
						elif len(d) == 2:
							sec += int(d[1])
							mini += int(d[0])
					else:
						for t in s[2:]:
							na_word_count += len(t)

	while(sec > 60):
		mini += 1
		sec -= 60
	while(mini > 60):
		hr += 1
		mini -= 60

	print('肉汁的文字數:', me_word_count)
	print('肉汁的貼圖數:', me_sticker_count)
	print('肉汁的圖片數:', me_pic_count)
	print('肉汁的錄音數:', me_sound_count)
	print('肉汁電話沒接次數:', na_call_count + na_nocatch_count)
	print('肉汁電話拒接次數:', na_callcancet_count)
	print('Na的文字數:', na_word_count)
	print('Na的貼圖數:', na_sticker_count)
	print('Na的圖片數:', na_pic_count)
	print('Na的錄音數:', na_sound_count)
	print('Na的文字數:', na_word_count)
	print('Na電話沒接次數:', me_call_count + me_nocatch_count)
	print('Na電話拒接次數:', me_callcancet_count)
	print('總通話時長:', hr, '小時', mini, '分', sec, '秒')

#主程式
def main():
	filename = '[LINE]Na.txt'
	if os.path.isfile(filename):
		chat_list = read_file(filename)
		new_list = convert(chat_list)
	else:
		print('找不到檔案')

main()