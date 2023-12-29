from pydantic import BaseModel

class PromptsRequest(BaseModel):
    name: str
    role: str
    company: str
    solution: str
    metric: str

class PromptsResponse(BaseModel):
    name: str
    email: str
    id: int

    class Config:
        from_attributes = True
        
class SocialsRequest(BaseModel):
    name: str
    company: str
    achievement: str
    metric: str
    
class SocialsResponse(BaseModel):
    name: str
    post: str
    id: int

    class Config:
        from_attributes = True