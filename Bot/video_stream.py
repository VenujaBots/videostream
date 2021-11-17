import re 
import os
from pytgcalls import GroupCallFactory
from pyrogram import Client, filters
from pyrogram.types import Message
# from py_youtube import ytdl
from py_youtube import ytdl 

API_ID = os.environ.get("API_ID",18862638)
API_HASH = os.environ.get("API_HASH","2a4a8dc0c1f6c9cb65f9f144439558ae")
SESSION_NAME = os.environ.get("SESSION_NAME","BQCsRa8zMaGWz7C7pjv2gffsGEQkU_9KU9ZFGR46UdpeKqF-2m7jr-WYJ8NxOi3Bic26ZDQ6xwwY6BpmEMkmYTo_MRhR8YzEMj94FfEGNlyO0Hdl4G3mwFb9_FseECapzSL0WMidaB07UCeic3-qQxmlX3dIIF5TXt5WTA5FdbTvRI9InBZk-VltYnu49JiwiohcwW_l707q_yj7lkqX1ydsyDPNBrLCfzVUWvtyvNFHkhocvYkYKdMzG0a1a_p7HpMBOQSfekaDAUdnQJyBqVRbXtWvYf7hlhtHpW0puIt3JrReWw9zh95DWh7CjWmLsF7L57ZhjwhFAf6X1J8Je1aBdkfIGgA")
CHAT = os.environ.get("CHAT","@VndBotSupport")
ADMIN = int(os.environ.get("ADMIN", 1984415770))

app = Client(SESSION_NAME, API_ID, API_HASH)

group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)
VIDEO_CALL = {}

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["start"]))
async def start(client, m: Message):
	await m.reply("Hello Start Stream Video Using Command /play(reply_to_message) and /stop\n  ")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["play"]))
async def play(client, m: Message):
	if (m.reply_to_message):
			link = m.reply_to_message.text
			youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
			youtube_regex_match = re.match(youtube_regex, link)
			if youtube_regex_match:
				             try:
				             	video_url = ytdl(link).besturl()
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	return
				             try:
				             	group_call = group_call_factory.get_group_call()
				             	await group_call.join(CHAT)
				             	await group_call.start_video(video_url,enable_experimental_lip_sync=True)
				             	VIDEO_CALL[CHAT] = group_call
				             	await m.reply("**Started  Streaming!**")
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	
					
			else:
			         	try:
			         		group_call = group_call_factory.get_group_call()
			         		await group_call.join(CHAT)
			         		await group_call.start_video(link,enable_experimental_lip_sync=True)
			         		VIDEO_CALL[CHAT] = group_call
			         		await m.reply("** Started Streaming!**")
			         	except Exception as e:
			         	    	await m.reply(f"**Error** -- `{e}`")
				             	
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["livestream"]))
async def livestream(client, m: Message):
	if (m.reply_to_message):
			link = m.reply_to_message.text
			youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
			youtube_regex_match = re.match(youtube_regex, link)
			if youtube_regex_match:
				             try:
				             	video_url = ytdl(link).besturl()
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	return
				             try:
				             	group_call = group_call_factory.get_group_call()
				             	await group_call.join(CHAT)
				             	await group_call.start_video(video_url,enable_experimental_lip_sync=False)
				             	VIDEO_CALL[CHAT] = group_call
				             	await m.reply("**Started  Streaming!**")
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	
					
			else:
			         	try:
			         		group_call = group_call_factory.get_group_call()
			         		await group_call.join(CHAT)
			         		await group_call.start_video(link,enable_experimental_lip_sync=False)
			         		VIDEO_CALL[CHAT] = group_call
			         		await m.reply("** Started Streaming!**")
			         	except Exception as e:
			         	    	await m.reply(f"**Error** -- `{e}`")




@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["stop"]))
async def stop (client, m: Message):
	try:
	       await VIDEO_CALL[CHAT].stop()
	       await m.reply("** Stopped Streaming!**")
	except Exception as e:
		await m.reply(f"**Error** - `{e}`")
