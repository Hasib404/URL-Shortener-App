from fastapi import APIRouter, Depends
from models.request import URLOrigin
from models.response import Response
from endpoints import deps
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from utils.helper_functions import is_valid_url
from services.shortener_service import URLShortenerService
from services.click_count_service import URLClickCount
from models.models import Shortener

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
    
    shortener_service = URLShortenerService(url_origin.url, db)
    url_obj = shortener_service.shorten_url_obj()

    data = {"shortener_id": url_obj.unique_key}
    return Response(data, 200, "shortener added successfully.", False)


@router.get("/{url_key}", response_description="Redirect to original url")
def forward_to_original_url(
        url_key: str,
        db: Session = Depends(deps.get_db)
    ):

    click_count_service = URLClickCount(url_key, db)
    click_count_service.update_db_clicks()

    url_obj = (
            db.query(Shortener)
            .filter(Shortener.unique_key == url_key)
            .first()
        )
    if url_obj.unique_key == url_key:
        return RedirectResponse(url_obj.original_url)
    else:
        "raise_not_found(request)"