from shortzy import Shortzy
from mdisky import Mdisk
from config import MDISK_API, SHORTENER_API, SHORTENER_WEBSITE

shortzy = Shortzy(SHORTENER_API, SHORTENER_WEBSITE)
mdisk = Mdisk(MDISK_API)

async def mdisk_droplink_convertor(text):
    links = await mdisk_api_handler(text)
    links = await replace_link(links)
    return links

async def mdisk_api_handler(text):
    return await mdisk.convert_from_text(text)

async def replace_link(text):
    return await shortzy.convert_from_text(text)