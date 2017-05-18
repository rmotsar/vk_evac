from src.database import base, sqlite
from src.models import Conversation, Message

base.metadata.create_all(sqlite)
Conversation.metadata.create_all(sqlite)
Message.metadata.create_all(sqlite)
