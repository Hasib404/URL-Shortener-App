from models.models import URLClicks

class URLClickCount:
    def __init__(self, key, db):
        self.key = key
        self.db = db

    def update_db_clicks(self) -> URLClicks():
        url_click = (
            self.db.query(URLClicks)
            .filter(URLClicks.visited_url_key == self.key)
            .first()
        )
        if url_click:
            url_click.clicks += 1
            self.db.commit()
            self.db.refresh(url_click)

        else:
            new_url_click = URLClicks(
                visited_url_key=self.key,
                clicks=1
            )
            self.db.add(new_url_click)
            self.db.commit()
            self.db.refresh(new_url_click)
