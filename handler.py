import re
import time

from nonebot.plugin import on_message
from nonebot.rule import regex, Rule
from nonebot.adapters import Event, Message

from .config import config

plus = on_message(rule=regex(""), priority=config.plus_one_priority, block=False)
msg_dict = {}


def get_group_id(string: str):
    group_id = string.split("_")[-2]
    return group_id


def is_equal(msg1: Message, msg2: Message):
    """判断是否相等"""
    if len(msg1) == len(msg2) == 1 and msg1[0].type == msg2[0].type == "image":
        if msg1[0].data["file_size"] == msg2[0].data["file_size"]:
            return True
    if msg1 == msg2:
        return True


@plus.handle()
async def plush_handler(event: Event):
    global msg_dict

    group_id = get_group_id(event.get_session_id())
    if group_id not in config.plus_one_white_list:
        return

    # 获取群聊记录
    text_list = msg_dict.get(group_id, None)
    if not text_list:
        text_list = []
        msg_dict[group_id] = text_list

    # 获取当前信息
    msg = event.get_message()

    try:
        if not is_equal(text_list[-1], msg):
            text_list = []
            msg_dict[group_id] = text_list
    except IndexError:
        pass

    text_list.append(msg)

    if len(text_list) > 1:
        await plus.send(msg)
