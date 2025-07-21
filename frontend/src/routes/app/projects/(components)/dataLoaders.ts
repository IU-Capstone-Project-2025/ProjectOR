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

export const generateTags = async (projectId: number) => {
	const { data, error } = await client.GET('/api/tags/generate/{project_id}', {
		params: { path: { project_id: projectId } }
	});

	if (error || !data) {
		console.error('Error generating tags:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to generate tags'));
	}

	return data;
};

export const addProjectTags = async (projectId: number, tags: string[]) => {
	const { data, error } = await client.POST('/api/tags/add/{project_id}', {
		params: { path: { project_id: projectId } },
		body: tags.map((tag) => ({ name: tag }))
	});

	if (error || !data) {
		console.error('Error adding tags to project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to add tags to project'));
	}

	return data;
};

export const removeProjectTags = async (projectId: number, tags: string[]) => {
	const { data, error } = await client.DELETE('/api/tags/remove/{project_id}', {
		params: { path: { project_id: projectId } },
		body: tags.map((tag) => ({ name: tag }))
	});

	if (error || !data) {
		console.error('Error removing tags from project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to remove tags from project'));
	}

	return data;
};

export const applyToProject = async (projectId: number) => {
	const { data, error } = await client.POST('/api/projects/{project_id}/apply', {
		params: { path: { project_id: projectId } }
	});

	if (error || !data) {
		console.error('Error applying to project:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to apply to project'));
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

export const getProjectApplications = async (projectId: number) => {
	const { data, error } = await client.GET('/api/projects/{project_id}/applications', {
		params: { path: { project_id: projectId } }
	});

	if (error || !data) {
		console.error('Error fetching project applications:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to fetch project applications'));
	}

	return data;
};

export const approveApplication = async (
	projectId: number,
	isApproved: boolean,
	userId: number,
	feedback: string
) => {
	const { data, error } = await client.PATCH('/api/projects/{project_id}/applications/approve', {
		params: { path: { project_id: projectId } },
		body: {
			is_approved: isApproved,
			user_id: userId,
			feedback
		}
	});

	if (error || !data) {
		console.error('Error approving application:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to approve application'));
	}

	return data;
};

export const enhanceProjectDescription = async (description: string) => {
	const { data, error } = await client.POST('/api/projects/enhance-description', {
		body: { project_description: description }
	});

	if (error || !data) {
		console.error('Error enhancing project description:', error);
		throw new Error(JSON.stringify(error?.detail ?? 'Failed to enhance project description'));
	}

	return data;
};
