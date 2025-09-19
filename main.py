from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import os
import random

@register("mytest", "zds299", "测试", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("px")
    async def px(self, event: AstrMessageEvent):
        """这是一个 px 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        image_folder = "Z:/python/pixiv_Crawler-main/daily"
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        image_files = []
        for file in os.listdir(image_folder):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_files.append(os.path.join(image_folder, file))
        selected_image = random.choice(image_files)
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!")
        yield event.image_result(selected_image) 

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
