import base64
import json
import email
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# 解析MHT文件并提取Base64编码的图像数据
def parse_mht_for_images(file_path):
    with open(file_path, 'rb') as file:
        msg = BytesParser(policy=policy.default).parse(file)

    images = {}
    for part in msg.iter_parts():
        if part.get_content_type() == 'image/jpeg':
            content_location = part.get('Content-Location')
            base64_data = part.get_payload(decode=False)
            images[content_location] = base64_data

    return images

# 解析MHT文件并提取步骤信息
def parse_mht_for_steps(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    # 提取XML数据
    xml_data = soup.find('script', {'id': 'myXML'}).string
    xml_soup = BeautifulSoup(xml_data, 'xml')

    steps = []
    for action in xml_soup.find_all('EachAction'):
        step_data = {
            'step': action.get('ActionNumber'),
            'description': action.find('Description').text,
            'screenshot': action.find('ScreenshotFileName').text,
            'action': action.find('Action').text
        }
        steps.append(step_data)
    return steps

# 使用Base64解码截图
def decode_base64_image(base64_data):
    image_data = base64.b64decode(base64_data)
    image = Image.open(BytesIO(image_data))
    return image
