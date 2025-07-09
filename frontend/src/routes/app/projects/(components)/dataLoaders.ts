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
		throw new Error(JSON.stringify(error ?? 'Failed to fetch project'));
	}

	return data;
};
