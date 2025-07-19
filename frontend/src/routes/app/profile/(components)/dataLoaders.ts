import { client } from '$lib/api/client';

export const getMe = async () => {
	const { data, error } = await client.POST('/api/user/get-me');
	if (error || !data) {
		console.error('Error fetching user profile:', error);
		throw new Error(JSON.stringify(error ?? 'Failed to fetch user profile'));
	}
	return data;
};
