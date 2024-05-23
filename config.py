from pydantic import BaseModel, Field
from nonebot import get_plugin_config


class Config(BaseModel):
    """Plugin Config Here"""

    plus_one_priority: int = (Field(1, doc="plus_one 响应优先级"))


config = get_plugin_config(Config)
