import { client } from '$lib/api/client';

export const login = async (username: string, password: string) => {
	const { error, data } = await client.POST('/api/auth/token', {
		body: {
			grant_type: 'password',
			scope: '',
			username,
			password
		},
		bodySerializer(body) {
			const fd = new FormData();
			for (const [key, value] of Object.entries(body)) {
				fd.append(key, value as string);
			}
			return fd;
		}
	});

	if (error) {
		console.error(error);
		throw new Error(JSON.stringify(error.detail));
	}

	return data;
};