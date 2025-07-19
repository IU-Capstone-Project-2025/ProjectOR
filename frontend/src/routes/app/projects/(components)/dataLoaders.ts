import { client } from '@/api/client';

export const getProjectById = async (projectId: number) => {
	const { data, error } = await client.GET('/api/projects/{project_id}', {
		params: {
			path: {
				project_id: projectId
			}
		}
	});

	if (error || !data) {
		console.error('Error fetching project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to fetch project'));
	}

	return data;
};

export const updateProject = async (
	projectId: number,
	brief_description: string,
	description: string
) => {
	const { data, error } = await client.POST('/api/projects/{project_id}/update', {
		params: { path: { project_id: projectId } },
		body: {
			brief_description,
			description
		}
	});
	if (error || !data) {
		console.error('Error updating project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to update project'));
	}
	return data;
};
