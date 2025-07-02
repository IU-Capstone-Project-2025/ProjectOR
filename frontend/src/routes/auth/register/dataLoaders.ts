import { client } from '$lib/api/client';

export const register = async (username: string, password: string) => {
	const { data, error } = await client.POST('/api/auth/register', {
		body: {
			username,
			password
		}
	});
	if (error) {
		throw new Error(JSON.stringify(error?.detail ?? 'Registration failed'));
	}
	return data;
};
