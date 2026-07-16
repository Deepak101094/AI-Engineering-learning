from src.factories.llm_service_factory import LLMServiceFactory


def test_factory_returns_service():

    service = LLMServiceFactory.create()

    assert service is not None