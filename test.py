import zipfile
import requests
import io
from PIL import Image
import json

# 下载压缩文件
image_zip_url = 'http://images.cocodataset.org/zips/test2017.zip'
annotations_zip_url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'

def download_and_stream_zip(url):
    response = requests.get(url, stream=True)
    return zipfile.ZipFile(io.BytesIO(response.content))

# 下载并读取压缩文件
image_zip = download_and_stream_zip(image_zip_url)
annotations_zip = download_and_stream_zip(annotations_zip_url)

# 读取注释文件
with annotations_zip.open('annotations/instances_val2017.json') as f:
    annotations = json.load(f)

# 处理图像
for img_info in annotations['images'][:5]:
    with image_zip.open(f'test2017/{img_info["file_name"]}') as img_file:
        image = Image.open(img_file)
        image.show()  # 或者其他图像处理操作
