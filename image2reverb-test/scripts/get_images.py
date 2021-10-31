import sys
import os
from google_images_download import google_images_download


def main():
    """
    这个是自动从谷歌图片中下关键词对应图片的工具
    :return:
    """
    response = google_images_download.googleimagesdownload()
    for f in sys.argv[1:]:
        arguments = {
            "keywords": os.path.basename(f),
            "limit": 20,
            "print_urls": True
        }
        paths = response.download(arguments)
        print(paths)


if __name__ == "__main__":
    main()