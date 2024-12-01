
from datetime import datetime, timedelta, timezone
from datetime import timedelta
from jose import JWTError,jwt
from fastapi import Depends
import schemas


SECRET_KEY= "d4ceff00302857dec427c9d3ebee97cd2be25d277bc3d3ae6085918a6066a190"
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire =datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM )
    return encoded_jwt
    
def verify_Token(token:str, credentials_exception):
    try:
        payload= jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM )
        email: str =  payload.get("username")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(username = email)
    except JWTError:
        raise credentials_exception
