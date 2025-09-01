from fastapi import APIRouter, UploadFile, File, Form
# from .services.text_handler import handle_text_query
from .services.image_handler import handle_image_query
from .services.text_handler import get_llm_response
 
router = APIRouter()
 
# @router.post("/ask/text")
# async def ask_text(query: str = Form(...)):
#     return {"response": handle_text_query(query)}
 
@router.post("/ask/text")
async def ask_text(query: str = Form(...)):
    response = get_llm_response(query)
    return {"response": response}
 
 
@router.post("/ask/image")
async def ask_image(file: UploadFile = File(...)):
    contents = await file.read()
    return {"response": handle_image_query(contents)}