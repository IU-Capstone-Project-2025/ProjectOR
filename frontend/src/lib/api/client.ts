import createClient, { type Middleware } from 'openapi-fetch';
import type { paths } from './v1';

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL as string;

const authWithHeadersMiddleware: Middleware = {
	onRequest({ request }) {
		const authorizationToken = localStorage.getItem('authorization');
		if (authorizationToken) {
			request.headers.set('Authorization', authorizationToken);
		}
		return request;
	}
};

export const client = createClient<paths>({
	baseUrl: API_BASE_URL
});


client.use(authWithHeadersMiddleware);
