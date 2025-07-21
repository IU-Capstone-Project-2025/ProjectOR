import { client } from '$lib/api/client';

export const getApplications = async () => {
	const { data, error } = await client.GET('/api/projects/all-applications');

	if (error || !data) {
		console.error('Error fetching applications:', error);
		throw new Error('Failed to fetch applications');
	}
	return data;
};

export const getUserById = async (userId: number) => {
	const { data, error } = await client.GET('/api/user/get-by-id/{user_id}', {
		params: { path: { user_id: userId } }
	});

	if (error || !data) {
		console.error('Error fetching user:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to fetch user'));
	}

	return data;
};

export const getProjectById = async (projectId: number) => {
	const { data, error } = await client.GET('/api/projects/{project_id}', {
		params: { path: { project_id: projectId } }
	});

	if (error || !data) {
		console.error('Error fetching project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to fetch project'));
	}

	return data;
};
