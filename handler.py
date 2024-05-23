from nonebot.plugin import on_message
from nonebot.rule import regex
from nonebot.adapters import Event

plus = on_message(rule=regex(""), priority=1, block=False)
msg_dict = {}


def get_group_id(string: str):
    group_id = string.split("_")[-2]
    return group_id


@plus.handle()
async def plush_handler(event: Event):
    global msg_dict

    # 获取群聊记录
    group_id = get_group_id(event.get_session_id())
    text_list = msg_dict.get(group_id, None)
    if not text_list:
        text_list = []
        msg_dict[group_id] = text_list

    # 获取当前信息
    msg = event.get_message()
    try:
        if text_list[-1] != msg:
            text_list = []
            msg_dict[group_id] = text_list
    except IndexError:
        pass
    text_list.append(msg)
    if text_list.count(msg) > 1:
        await plus.send(msg)
