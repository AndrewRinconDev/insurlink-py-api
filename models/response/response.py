from pydantic import BaseModel
from typing import Optional

class Response(BaseModel):
  statusCode: int
  hasError: bool
  message: Optional[str] = None
  data: Optional[object] = None