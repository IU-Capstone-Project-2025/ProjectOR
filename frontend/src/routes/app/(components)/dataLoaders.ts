import { client } from '@/api/client';

export const createProject = async (title: string, description: string) => {
	const { data, error } = await client.POST('/api/projects/', {
		body: {
			title,
			description,
			is_public: true // Assuming default is public
		}
	});

	if (error || !data) {
		console.error('Error creating project:', error);
		throw new Error(JSON.stringify(error ?? 'Failed to create project'));
	}

	return data;
};
