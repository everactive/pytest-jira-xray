import pytest
from typing import Dict, Any


@pytest.hookspec
def pytest_xray_results(results: Dict[str, Any], session: pytest.Session) -> None:
    """
    Called before uploading XRAY result to Jira server.

    :param results: xray results dictionary
    :param session: pytest session
    """
