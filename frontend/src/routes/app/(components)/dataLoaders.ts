import { client } from '$lib/api/client';
import type { components } from '@/api/v1';

export const createProject = async (title: string, description: string, isOpensource: boolean, isDead: boolean) => {
	const { data, error } = await client.POST('/api/projects/', {
		body: {
			title,
			description,
			is_public: true,
			is_opensource: isOpensource,
			is_dead: isDead
		}
	});

	if (error || !data) {
		console.error('Error creating project:', error);
		throw new Error(JSON.stringify(error ?? 'Failed to create project'));
	}

	return data;
};

export const setRole = async (role: components['schemas']['UserRole']) => {
	const { data, error } = await client.POST('/api/user/set-role', {
		body: {
			role
		}
	});
	if (error || !data) {
		console.error('Error setting user role:', error);
		throw new Error(JSON.stringify(error ?? 'Failed to set user role'));
	}
	return data;
};
