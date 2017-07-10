# !/usr/bin/python3
# coding:utf-8

import pickle
import sys
import os
import curses

# 生词本

# 创建新单词
def CreateNewWord(data):
	word = input('输入生词: ')

	# 此单词已存在
	if word in data.keys():
		stdscr.addstr('此单词已存在 ' + word + ': ' + data[word])	
		c = input('是否添加新释义?[y/n]')
		if c == 'y':
			translation = ('输入新释义: ')
			data[word] = data[word] + translation + ';'
	else:
		translation = input('输入释义: ')
		data[word] = translation + ';'
	print(word + ': ' + data[word])

# 删除单词
def DeleteWord(data):
	word = input('输入要删除的单词: ')
	if word in data.keys():
		c = input(word + ': ' + data[word] + ', 确认删除?[y/n]')
		if c == 'y':
			del data[word]
	else:
		print('找不到此单词')

# 读取本地单词本数据
def LoadData():
	if os.path.exists('vocabulary.dat') == False:
		return dict()
	with open('vocabulary.dat', 'rb') as f:
		data = pickle.load(f)
		return data

# 保存修改后的单词本数据到本地（这里每次使用都会保存，数据量小的时候可以，大的时候比较蠢，耗时长）
def SaveData(data):
	with open('vocabulary.dat', 'wb') as f:
		pickle.dump(data, f)

# 背单词
def study(data):
	stdscr.addstr('查看释义↑，下个单词↓\n')
	for k, v in data.items():
		stdscr.addstr(k + '\n')
		c = stdscr.getch()
		if c == curses.KEY_DOWN:
			continue
		elif c == curses.KEY_UP:
			stdscr.addstr(v + '\n')
		elif c == ord('q'):
			break
	
	stdscr.addstr('全部单词已背完\n')

# 设置curses
def SetCurses():
	curses.noecho()
	curses.cbreak()	

# 关闭curses
def EndCurses():
	curses.endwin()

# 清空屏幕
def ClearScreen():
	stdscr.clear()

if __name__ == '__main__':
	global stdscr 

	data = LoadData()

	while True:
		c = input('1.背单词 2.添加单词 3.删除单词 q.退出\n')
		if c == '1':
			stdscr = curses.initscr()
			stdscr.keypad(True)
			ClearScreen()
			SetCurses()
			study(data)
			EndCurses()
		elif c == '2':
			CreateNewWord(data)
		elif c == '3':
			DeleteWord(data)
		elif c == 'q':
			sys.exit()

	SaveData(data)
