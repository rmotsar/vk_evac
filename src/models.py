from sqlalchemy import JSON, Column, String, Integer, BigInteger, TIMESTAMP
from src.database import base, sqlite


class Conversation(base):
    __tablename__ = 'conversations'

    id = Column(BigInteger, primary_key=True)
    type = Column(String)


# class Attachment(base):
#     __tablename__ = 'attachments'


class Message(base):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True)
    body = Column(String)
    user_id = Column(BigInteger)
    from_id = Column(BigInteger)
    date = Column(TIMESTAMP),
    read_state = Column(Integer)
    out = Column(Integer)
    random_id = Column(BigInteger)
    attachments = Column(JSON)
    fwd_messages = Column(JSON)
