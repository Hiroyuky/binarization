#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
from matplotlib import pylab as plt

def binari(k_max, d_max):
	FILENAME_IN_DATA = 'DATA_pic/'		# 変換する画像ディレクトリ名
	FILENAME_OUT_DATA = 'DATA_binari/'	# 出力するディレクトリ名
	FILENAME_IN_EXTENSION = '.bmp'		# 入力ファイル拡張子
	FILENAME_OUT_EXTENSION = '.csv'		# 出力ファイル拡張子

	# 扱う画像データ名
	PIC_NAME = str(k_max) + '_' + str(d_max)
	print 'input file name: ' + PIC_NAME

	# 圧縮率
	comp = 10

	# 入力するファイル名統合
	picName = FILENAME_IN_DATA + PIC_NAME + FILENAME_IN_EXTENSION
	# 出力するバイナリデータ名統合
	binariName = FILENAME_OUT_DATA + PIC_NAME + FILENAME_OUT_EXTENSION

	# 画像を配列に読み込んでグレースケールに変換
	# 実際ミスっているけれど気にしてはいけない
	img = np.array(Image.open(picName).convert('L'))

	# 1/10にする（300x300 -> 30x30）
	img = (img[::comp, ::comp] + img[1::comp, ::comp] + img[::comp, 1::comp] + img[1::comp, 1::comp])/4

	f = open(binariName, "w")

	for i in img:
		for item in i:
			if(item > 50): 
				f.write("0")
			else:
				f.write("1")
			f.write(",")
	f.write("\n")

	print 'success!'

if __name__ == '__main__':
	K_MAX = 3	# クラス数
	D_MAX = 5	# データ数
	print 'Pic to binarization'
	for k in range(0, K_MAX):
		for d in range(0, D_MAX):
			binari(k, d)


