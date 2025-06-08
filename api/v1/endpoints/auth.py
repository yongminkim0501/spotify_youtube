import os
import requests
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from core.security import create_access_token

router = APIRouter(tags=["oauth"])

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

@router.get("/login/oauth2/code/google")
def google_callback(code: str):
    """
    :param code: str
    :return: {
        "access_token": jwt_token,
        "token_type": "bearer",
        "user": {"email": user_email, "id": user_id}
    }
    """
    token_endpoint = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    r = requests.post(token_endpoint, data=data)
    if r.status_code != 200:
        raise HTTPException(status_code=400, detail="Fail")

    token_json = r.json()
    access_token = token_json["access_token"]
    id_token = token_json.get("id_token")

    userinfo_endpoint = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    userinfo_resp = requests.get(userinfo_endpoint, headers=headers)
    if userinfo_resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Fail")

    userinfo = userinfo_resp.json()

    user_email = userinfo["email"]
    user_id = userinfo["id"]  # Google ID를 사용자 ID로 사용

    jwt_token = create_access_token({"sub": user_id})

    return {
        "access_token": jwt_token,
        "token_type": "bearer",
        "user": {"email": user_email, "id": user_id}
    }



