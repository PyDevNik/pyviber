# PyViber

PyViber is a powerful asynchronous Python library for interacting with Viber Bot API.

## Installation

```bash
pip install pyviber
```

## Usage

### Initializing the Bot

```python
from pyviber.bot import Bot
from pyviber.event_type import EventType
import asyncio

# Initialize the bot with your Viber Bot token
bot = Bot("your_viber_bot_token")
```

### Setting and Unsetting Webhook

```python
# Set webhook URL to receive callbacks
webhook_url = "https://your-webhook-url.com/viber"
event_types = [EventType.MESSAGE, EventType.SUBSCRIBED]

async def set_webhook():
    await bot.set_webhook(webhook_url, event_types)

async def unset_webhook():
    await bot.unset_webhook()
```

### Sending Messages

```python
from pyviber.messages import TextMessage
from pyviber.sender import Sender

async def send_message_example():
    sender = Sender(name="Your Bot Name", avatar="https://your-avatar-url.com/avatar.png")
    message = TextMessage(text="Hello from your Viber Bot!")
    receiver_id = "user_viber_id"

    await bot.send_message(receiver_id, message, sender)
```

### Getting Account Information

```python
from pyviber.bot_info import BotInfo

async def get_account_info_example():
    account_info = await bot.get_account_info()
    print(account_info.name)
    print(account_info.uri)
```

### Handling Events

```python
@bot.event("message")
async def handle_message_event(event):
    # Handle incoming message event
    if event.type == EventType.MESSAGE:
        print("Received message:", event.message)

async def handle_events():
    # Simulate receiving an event (should come from Viber)
    event = {"event": "message", "message": "Test message"}
    await bot.handle_event(event)
```

## Error Handling

Exceptions are raised for API errors, ensuring robust error handling for operations like sending messages or retrieving information.

## References

- [Viber Public Account API Documentation](https://developers.viber.com/docs/api/rest-bot-api/)