# -*- encoding: utf-8 -*-

import os

BITRATE = [100, 200, 300, 400]
GOP1 = [10]

'''
BITRATE = [800]
GOP1 = [5]
GOP2 = [12, 15]
'''
x265ExePath = r'H:\265transcode\x265\x265.exe'
CMD_HEVC_ENCODE = '%s --input %s --input-res 352x288 --fps 25 --output %s --profile main   --keyint %d --no-scenecut --b-adapt 0 --bframes 0 --bitrate %d'


current_path = os.getcwd()
#print current_path


# first round encode
for video_file in os.listdir(current_path):
   # print video_file
    if os.path.isfile(os.path.join(current_path, video_file)):
        if video_file.find('.yuv') >= 0:
            for bit_rate in BITRATE:
                for gop in GOP1:
                    new_name = 'singlehevc/%s_%d_%dk.265' % (video_file[:video_file.find('.')], gop, bit_rate)
                   # os.system(CMD_FIRST % (video_file, bit_rate, gop, new_name))
                os.system(CMD_HEVC_ENCODE % (x265ExePath,video_file,new_name,gop, bit_rate))

# second round encode
"""current_path += r'/first'
os.chdir(current_path)
for video_file in os.listdir(current_path):
    if os.path.isfile(os.path.join(current_path, video_file)):
        if video_file.find('.264') >= 0:
            for bit_rate in BIT_RATE:
                for gop in GOP_SECOND:
                    new_name = r'../second/%s_%d_%dk.264' % (video_file[:video_file.find('.')], gop, bit_rate)
                    print CMD_SECOND % (video_file, bit_rate, gop, new_name)
                    os.system(CMD_SECOND % (video_file, bit_rate, gop, new_name))"""
