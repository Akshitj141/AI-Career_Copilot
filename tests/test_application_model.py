from app.models.application_model import (
    ApplicationAssets
)


def test_application_assets_creation():

    assets = ApplicationAssets()

    assert assets.cover_letter == ""