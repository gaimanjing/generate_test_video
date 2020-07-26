from moviepy.editor import *
import os
import random

def getAllVideo():
    allVideo = []

    # 遍历 video 文件夹
    for root, dirs, files in os.walk("input"):
        # 按文件名排序
        files.sort()
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                allVideo.append(video)

    return allVideo



def makeOneFile(mergeFileCount, allVideo):
    intputVideo = []
    outputFileName = 'output/'


    # get random input file
    for i in range(mergeFileCount):
        index = random.randint(0, len(allVideo)-1)
        intputVideo.append(allVideo[index])
        outputFileName += str(index) + '_'

    # add random string to output file name
    for i in range(8):
        outputFileName += str(random.randint(0, 10))

    outputFileName += '.mp4'
    final_clip = concatenate_videoclips(intputVideo)
    # final_clip.to_videofile(outputFileName)
    # https://stackoverflow.com/questions/54722792/output-video-has-no-sound
    final_clip.write_videofile(outputFileName, temp_audiofile='output/temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")



def makeFiles(outputFileCount, mergeFileCount, allVideo):
    for i in range(outputFileCount):
        makeOneFile(mergeFileCount, allVideo)


outputFileCount = 1
mergeFileCount = 2
makeFiles(outputFileCount, mergeFileCount, getAllVideo())