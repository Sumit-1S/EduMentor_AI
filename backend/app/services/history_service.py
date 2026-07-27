from sqlalchemy.orm import Session

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

from app.models.message import ChatMessage


def get_chat_history(
    db: Session,
    session_id: int
):
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.id.asc())
        .all()
    )

    history = []

    for message in messages:

        if message.role == "user":

            history.append(
                HumanMessage(
                    content=message.content
                )
            )

        else:

            history.append(
                AIMessage(
                    content=message.content
                )
            )

    return history