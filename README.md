# generate_test_video
generate test video, merge video

使用 Python 拼接视频，用来测试。

每次从 `input` 目录中随机挑选 `mergeFileCount ` 个 `mp4` 视频进行拼接，生成 `outputFileCount ` 个视频文件保存在 `output` 目录下。

## 用法
1. 把要拼接的 `mp4` 视频放在 `input` 目录下，比如从抖音下载 n 个视频，放在该目录下
2. 打开 `generate_test_video.py` 修改参数

	```
	outputFileCount = 1	# 生成的视频文件个数
	mergeFileCount = 2	# 每次拼接的视频文件个数
	```
3. 打开 `shell` 直接执行

	```
	$ python3 generate_test_video.py
	```
4. 生成的视频文件在 `output`	目录下
