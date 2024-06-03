import asyncio
import re
from telethon import TelegramClient, events

# Your API ID and hash from my.telegram.org
api_id = '25810549'
api_hash = '695283c8b7c61e2c9726e1b2a5f3beb7'

# Your phone number associated with your Telegram account
phone = '+8801917915935'

# The username or ID of the channel to monitor
source_channel = 'lottery_9_7'

# The username or ID of the target channel or bot
target_channel = '@mehedi956_bot'

# Unique session name for each environment
session_name = 'unique_session_name'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message_text = event.message.message
    # Check if the message contains the numbers 3, 8, or 24
    if re.search(r'\b(3|8|24)\b', message_text):
        # Forward the new message to the target channel or bot
        await client.forward_messages(target_channel, event.message)

async def main():
    # Start the client with forced SMS authentication
    await client.start(phone, force_sms=True)
    print(f'Monitoring new posts in {source_channel}...')
    # Keep the script running
    await client.run_until_disconnected()

# Start the client
if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
