import vk_api
import time

from modules import XML as moduleXml

XML = moduleXml.XML("settings")
VK = vk_api.VkApi(token=XML.parsingFile("token"))

groupsId = []
groupsShortName = ""
for child in XML.parsingFile("groups", False):
    groupsShortName += child.text + ","

for group in VK.method("groups.getById", {"group_ids": groupsShortName}):
    groupsId.append(group["id"] * -1)

del groupsShortName

textPost = XML.parsingFile("textPost")
intervalPost = int(XML.parsingFile("interval"))

attachments = [attachment.text for attachment in XML.parsingFile("attachments", False)]
copyright = XML.parsingFile("copyright")
v = XML.parsingFile("v")