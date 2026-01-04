from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.concurrency import run_in_threadpool
from schemas import ChatRequest, ChatResponse,ChatHistoryResponse
from deps import get_current_user
from chatbot import model
from database import get_db
import models

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(
    request: ChatRequest,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    history = (
        db.query(models.ChatHistory)
        .filter(models.ChatHistory.user_id == current_user.id)
        .order_by(models.ChatHistory.id.desc())
        .limit(3)
        .all()
    )

    history_messages = [h.message for h in reversed(history)]

    reply = await run_in_threadpool(
        model.generate_reply,
        request.message,
        history_messages
        )
    
    chat = models.ChatHistory(
        user_id=current_user.id,
        message=request.message,
        reply=reply
    )

    db.add(chat)
    db.commit()

    return {"reply": reply}


#get chat history

@router.get("/history", response_model=list[ChatHistoryResponse])
def get_chat_history(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    chats = (
        db.query(models.ChatHistory)
        .filter(models.ChatHistory.user_id == current_user.id)
        .all()
    )

    return chats

