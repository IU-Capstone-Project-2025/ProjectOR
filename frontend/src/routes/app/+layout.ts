import { client } from '$lib/api/client';

export const load = async () => {
	const { data, error } = await client.POST('/api/user/get-me');
	if (error) {
		console.error('Failed to load user data:', error);
		return { user: null };
	}
	return { user: data };
};
