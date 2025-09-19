import os
import random
import aiofiles
from astrbot.api.message_components import Plain, Image
from astrbot.api.event import AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("top_command", "TOP命令", "发送随机图片", 1.0)
def top_command(event: AstrMessageEvent, context: Context):
    """
    当收到'TOP'消息时，发送随机图片
    """
    if event.get_message().strip().upper() == 'TOP':
        image_folder = "Z:\\python\\pixiv_Crawler-main\\daily_r18"

        try:
            # 检查文件夹是否存在
            if not os.path.exists(image_folder):
                return [Plain(f"图片文件夹不存在: {image_folder}")]

            # 获取文件夹中的所有图片文件
            image_files = []
            for file in os.listdir(image_folder):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_files.append(os.path.join(image_folder, file))

            if not image_files:
                return [Plain("图片文件夹中没有找到图片文件")]

            # 随机选择一张图片
            selected_image = random.choice(image_files)

            # 发送图片
            return [Image.fromFileSystem(selected_image)]

        except Exception as e:
            return [Plain(f"发送图片时出错: {str(e)}")]