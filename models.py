from pydantic import BaseModel, constr
from typing import Annotated

class SMSRequest(BaseModel):
    phone: Annotated[str, constr(min_length=10, max_length=15)]
    message: Annotated[str, constr(min_length=1, max_length=160)]
