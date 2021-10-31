import sys
import numpy
import soundfile


def main():
    """
    这个是转化bformat 文件到mono文件 多声道取均值
    :return:
    """
    for f in sys.argv[1:]:
        w, fs = soundfile.read(f)
        if len(w.shape) == 1 or w.shape[1] == 1:
            continue
        if w.shape[1] == 2:
            soundfile.write(f, numpy.mean(w, axis=1), fs)
        else:
            soundfile.write(f, w[:,0], fs)
        print("Processed and wrote %s." % f)


if __name__ == "__main__":
    main()