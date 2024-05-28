from nonebot.plugin import PluginMetadata
from nonebot import require

require("nonebot_plugin_session")
from nonebot_plugin_session import __plugin_meta__ as session_meta

from .config import Config
from .handler import plus

session_supported_adapters = session_meta.supported_adapters if session_meta.supported_adapters else set()


__plugin_meta__ = PluginMetadata(
    name="复读姬+1 PlusOne",
    description="全新复读姬，支持文本、图片、表情甚至是转发分享卡片复读，任意群聊触发 +1，姬就 +1。\n"
                "轻巧、专注，不使用任何数据库，不使用任何文件存储\n",
    usage="复读姬，任意群聊触发 +1，姬就 +1",
    config=Config,
    homepage="https://github.com/yejue/nonebot-plugin-plus-one",
    type="application",
    supported_adapters=set() | session_supported_adapters
)
