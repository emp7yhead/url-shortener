"""Model for url."""
from app.main import db


class Url(db.Model):  # type: ignore
    """Model for url."""

    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=db.func.now(),
    )
    original_url = db.Column(db.String, nullable=False)
    clicks_counter = db.Column(db.Integer, default=0)
