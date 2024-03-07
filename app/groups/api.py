

from pathlib import Path
import shutil
from app.core.config import get_templates
from fastapi import APIRouter, HTTPException, Query, Request, UploadFile


router = APIRouter(prefix="/groups",
          tags=["微信接口"])
templates = get_templates()


@router.get("/fileupload")
async def fileupload_page(request:Request):
    """文件上传页面"""
    return templates.TemplateResponse(
        "group_upload_qrcode.html",
        {
            "request": request
        }
    )

@router.post("/fileupload")
async def upload_qrcode(file:UploadFile):
    """上传二维码"""
    try:
        file_path = Path("static/images/group_qrcode.jpg")
        with file_path.open("wb") as f:
            shutil.copyfileobj(file.file,f)
        return {f"{file.filename}文件上传成功。"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/qrcode")
async def get_qrcode(request:Request):
    """获取群二维码"""
    return templates.TemplateResponse(
        "group_qrcode.html",
        {
            "request":request,
            "group_qrcode_url": '/images/group_qrcode.jpg'
        },
    )

@router.get("/chuancai")
async def get_chuan_cai_qrcode(request:Request):
    """获取注册川财证券的二维码"""
    return templates.TemplateResponse(
        "chuancai.html",
        {
            "request":request,
            "qrcode_url": '/images/chuancai.jpg'
        }
    )

@router.get("/zhangle")
async def get_zhangle_qrcode(request:Request):
    """获取二维码"""
    return templates.TemplateResponse(
        "zhangle.html",
        {
            "request":request,
            "qrcode_url": '/images/zhang_qrcode.png'
        }
    )