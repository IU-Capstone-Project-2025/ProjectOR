from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import HTTPException
from routes.api.project.router import get_projects, get_project_by_id
from routes.api.project.schemas import ProjectSchema


@pytest.fixture
def mock_service():
    service = AsyncMock()
    return service


@pytest.fixture
def mock_user():
    user = MagicMock()
    user.username = "testuser"
    user.role = "VIEWER"

    return user


@pytest.fixture
def sample_projects():
    return [
        ProjectSchema(
            id=1, title="Project 1", description="Description 1", is_public=True
        ),
        ProjectSchema(
            id=2, title="Project 2", description="Description 2", is_public=False
        ),
    ]


@pytest.mark.asyncio
async def test_get_projects_success(mock_service, sample_projects, mock_user):
    mock_service.get_projects.return_value = sample_projects

    response = await get_projects(mock_service, mock_user)

    assert response == sample_projects
    mock_service.get_projects.assert_called_once()


@pytest.mark.asyncio
async def test_get_project_not_found(mock_service, mock_user):
    project_id = -1
    mock_service.get_project_by_id.side_effect = HTTPException(
        status_code=404, detail=f"Project with ID {project_id} not found."
    )

    with pytest.raises(HTTPException) as exc_info:
        await get_project_by_id(
            project_id,
            mock_service,
            mock_user,
        )

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == f"Project with ID {project_id} not found."
    mock_service.get_project_by_id.assert_called_once_with(project_id)
