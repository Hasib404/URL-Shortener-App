from fastapi import APIRouter, Depends
from models.request import URLOrigin
from models.response import Response
from endpoints import deps
from sqlalchemy.orm import Session
from db import crud
from fastapi.responses import RedirectResponse
from utils.helper_functions import is_valid_url

# APIRouter creates path operations for shortener module
router = APIRouter(
    tags=["URL Shortener"],
    responses={404: {"description": "Not found"}},
)


@router.post("/url", response_description="shortener data added into the database")
async def shorten_url(url_origin: URLOrigin, db: Session = Depends(deps.get_db)):
    if not is_valid_url(url_origin.url):
        data = []
        return Response(data, 400, "Invalid URL", True)
    db_url = crud.create_db_url(db=db, url_origin=url_origin)
    data = {"shortener_id": db_url.unique_key}
    return Response(data, 200, "shortener added successfully.", False)


@router.get("/{url_key}", response_description="Redirect to original url")
def forward_to_original_url(
        url_key: str,
        db: Session = Depends(deps.get_db)
    ):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.original_url)
    else:
        "raise_not_found(request)"



# @router.get("/")
# async def read_all_products(db: Session = Depends(deps.get_db)):
#     data = db.query(Shortener).all()
#     return Response(data, 200, "URLS retrieved successfully.", False)