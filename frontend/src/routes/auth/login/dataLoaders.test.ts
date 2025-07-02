import { describe, it, expect, vi, beforeEach } from 'vitest';
import { login } from './dataLoaders';
import { client } from '$lib/api/client';

// Mock the API client
vi.mock('$lib/api/client', () => ({
	client: {
		POST: vi.fn()
	}
}));

describe('Auth Data Loaders', () => {
	beforeEach(() => {
		vi.clearAllMocks();
	});

	describe('login', () => {
		it('should login successfully', async () => {
			const mockToken = {
				access_token: 'mock-token',
				token_type: 'bearer',
				expires_in: 3600
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockToken,
				error: null
			});

			const result = await login('testuser', 'testpass');

			expect(client.POST).toHaveBeenCalledWith('/api/auth/token', {
				body: {
					grant_type: 'password',
					scope: '',
					username: 'testuser',
					password: 'testpass'
				},
				bodySerializer: expect.any(Function)
			});

			expect(result).toEqual(mockToken);
		});

		it('should serialize body as FormData', async () => {
			const mockToken = {
				access_token: 'mock-token',
				token_type: 'bearer'
			};

			let capturedFormData: FormData | null = null;
			
			vi.mocked(client.POST).mockImplementationOnce(async (url, options) => {
				if (options?.bodySerializer) {
					const body = {
						grant_type: 'password',
						scope: '',
						username: 'testuser',
						password: 'testpass'
					};
					capturedFormData = options.bodySerializer(body) as FormData;
				}
				return { data: mockToken, error: null };
			});

			await login('testuser', 'testpass');

			expect(capturedFormData).toBeInstanceOf(FormData);
			expect(capturedFormData?.get('username')).toBe('testuser');
			expect(capturedFormData?.get('password')).toBe('testpass');
			expect(capturedFormData?.get('grant_type')).toBe('password');
			expect(capturedFormData?.get('scope')).toBe('');
		});

		it('should throw error when API returns error', async () => {
			const mockError = {
				detail: 'Invalid credentials'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(login('wronguser', 'wrongpass')).rejects.toThrow(
				JSON.stringify(mockError.detail)
			);
		});

		it('should handle empty credentials', async () => {
			const mockError = {
				detail: 'Username and password required'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(login('', '')).rejects.toThrow(
				JSON.stringify(mockError.detail)
			);
		});

		it('should handle special characters in credentials', async () => {
			const mockToken = {
				access_token: 'mock-token',
				token_type: 'bearer'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockToken,
				error: null
			});

			const specialUsername = 'user@example.com';
			const specialPassword = 'pass@word!123';

			const result = await login(specialUsername, specialPassword);

			expect(client.POST).toHaveBeenCalledWith('/api/auth/token', {
				body: {
					grant_type: 'password',
					scope: '',
					username: specialUsername,
					password: specialPassword
				},
				bodySerializer: expect.any(Function)
			});

			expect(result).toEqual(mockToken);
		});
	});
});
