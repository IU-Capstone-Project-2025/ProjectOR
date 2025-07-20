from unittest.mock import AsyncMock
import pytest
from fastapi import HTTPException
from routes.api.project.service import ProjectService
from routes.api.project.schemas import ProjectSchema
from schemas.user import User


@pytest.fixture
def mock_data_access():
    data_access = AsyncMock()
    return data_access


@pytest.fixture
def project_service(mock_data_access):
    return ProjectService(data_access=mock_data_access)


@pytest.fixture
def user():
    return User(username="testuser", role="VIEWER", id=1)


@pytest.fixture
def sample_projects():
    return [
        ProjectSchema(
            id=1,
            title="Project 1",
            brief_description="Description 1",
            description=None,
            is_public=True,
            is_dead=False,
            is_opensource=True,
            status="active",
            ceo_id=1,
            created_at="2023-10-01T00:00:00Z",
        ),
        ProjectSchema(
            id=2,
            title="Project 2",
            brief_description="Description 2",
            description=None,
            is_public=True,
            is_dead=False,
            is_opensource=True,
            status="active",
            ceo_id=1,
            created_at="2023-10-01T00:00:00Z",
        ),
    ]


@pytest.mark.asyncio
async def test_get_projects(project_service, mock_data_access, user, sample_projects):
    mock_data_access.get_all_projects.return_value = sample_projects

    response = await project_service.get_projects()

    assert response == sample_projects
    mock_data_access.get_all_projects.assert_called_once()


@pytest.mark.asyncio
async def test_get_project_by_id_success(
    project_service, mock_data_access, sample_projects
):
    project_id = sample_projects[0].id
    expected_project = sample_projects[0]
    mock_data_access.get_project_by_id.return_value = expected_project

    response = await project_service.get_project_by_id(project_id)

    assert response == expected_project
    mock_data_access.get_project_by_id.assert_called_once_with(project_id)


@pytest.mark.asyncio
async def test_get_project_by_id_not_found(project_service, mock_data_access):
    project_id = -1
    mock_data_access.get_project_by_id.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await project_service.get_project_by_id(project_id)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == f"Project with ID {project_id} not found."
    mock_data_access.get_project_by_id.assert_called_once_with(project_id)
