#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
画像をグレースケール化し，そこからしきい値を設けて0or1の2値化処理します
出力はテキストデータ

githubって便利ですね☆

"""

from PIL import Image
import numpy as np
from matplotlib import pylab as plt

def bainari(i, j):
	
	FILENAME_IN_DATA = 'DATA_pic/'		# 変換する画像ディレクトリ名
	FILENAME_OUT_DATA = 'DATA_bainari/'	# 出力するディレクトリ名
	FILENAME_IN_EXTENSION = '.bmp'		# 入力ファイル拡張子
	FILENAME_OUT_EXTENSION = '.csv'		# 出力ファイル拡張子


	# 扱う画像データ名
	PIC_NAME = str(i) + '_' + str(j)

	# 入力するファイル名統合
	picName = FILENAME_IN_DATA + PIC_NAME + FILENAME_IN_EXTENSION
	# 出力するバイナリデータ名統合
	binariName = FILENAME_OUT_DATA + PIC_NAME + FILENAME_OUT_EXTENSION

	# 画像を配列に読み込んでグレースケールに変換
	# 実際ミスっているけれど気にしてはいけない
	img = np.array(Image.open(picName).convert('L'))

	# 1/10にする（300x300 -> 30x30）
	img = (img[::10, ::10] + img[1::10, ::10] + img[::10, 1::10] + img[1::10, 1::10])/4

	f = open(binariName, "w")

	for i in img:
		for item in i:
			if(item > 50): 
				f.write("0")
			else:
				f.write("1")
			f.write(",")

		# スカラーにするときは↓をコメントアウト
	f.write("\n")

if __name__ == '__main__':
	K_MAX = 3	# クラス数
	D_MAX = 5	# データ数

	for i in range(0, K_MAX):
		for j in range(0, D_MAX):
			bainari(i, j)


