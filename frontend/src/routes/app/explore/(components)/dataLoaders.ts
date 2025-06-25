import { client } from '@/api/client';

export const getProjects = async () => {
	const { data, error } = await client.GET('/api/projects/');
	if (error || !data) {
		console.error('Error fetching projects:', error);
		throw new Error(JSON.stringify(error ?? 'Failed to fetch projects'));
	}
	return data;
};