from src.config.settings import Settings


def test_model_exists():

    assert Settings.GEMINI_MODEL != ""