# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 19:07
# @Author  : Marshall
# @FileName: data_prepare.py

import sys
import numpy
import soundfile
import librosa
import os

def audio_resample(audio_path, fs_new=22050, length_new=5.94):
    """
    重新采样并修改长度，符合网络要求的格式，做一个标准化，输出覆盖原文件
    :param audio_path: 音频路径
    :param fs_new: 新的采样率
    :param length_new: 新的长度
    :return:
    """
    y, fs = soundfile.read(audio_path)
    y_22k = librosa.resample(y, fs, fs_new)  # resample to 22.05k
    y_22k_pad = librosa.util.fix_length(y_22k, round(fs_new * length_new))  # pad to length_new seconds
    soundfile.write(audio_path, y_22k_pad, fs_new, subtype='PCM_16')
    print("Processed and wrote %s" % audio_path)
    pass


def audio_all_resample(audio_root, fs_new=22050, length_new=5.94):
    for audio_name in os.listdir(audio_root):
        audio_path = os.path.join(audio_root,audio_name)
        audio_resample(audio_path, fs_new=fs_new, length_new=length_new)


if __name__ == "__main__":
    audio_root = "./image2reverb-test/data/val_B"
    audio_all_resample(audio_root)

