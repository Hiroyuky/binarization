Binarization
===
- picture  
  <img src="https://github.com/Hiroyuky/binarization/blob/master/readme_pic/yu_raw.png" width="320px">
- binarization  
  <img src="https://github.com/Hiroyuky/binarization/blob/master/readme_pic/yu_binari.png" width="320px">

## Description
使用にあたって，以下を各環境に合わせて変更する．
```python
	FILENAME_IN_DATA = 'DATA_pic/'		# 変換する画像ディレクトリ名
	FILENAME_OUT_DATA = 'DATA_bainari/'	# 出力するディレクトリ名
	FILENAME_IN_EXTENSION = '.bmp'		# 入力ファイル拡張子
	FILENAME_OUT_EXTENSION = '.csv'		# 出力ファイル拡張子
```
``` python
	K_MAX = 3	# クラス数
	D_MAX = 5	# データ数
```

また，画像圧縮率を変更するには以下を変更する．
``` python
	comp = num
```
## Reference
