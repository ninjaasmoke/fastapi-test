from fastapi import FastAPI, Header
from typing import Dict, Annotated

app = FastAPI()

class TicketWithoutRelations:
    pass

@app.post("/create", response_model=Dict)
async def create(
    workflow_id: str,
    ticket: Dict,
    x_sero_api_token: Annotated[str, Header()] = None,
) -> Dict:
    return ticket
