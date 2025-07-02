import { describe, it, expect, vi, beforeEach } from 'vitest';
import { register } from './dataLoaders';
import { client } from '$lib/api/client';

// Mock the API client
vi.mock('$lib/api/client', () => ({
	client: {
		POST: vi.fn()
	}
}));

describe('Register Data Loaders', () => {
	beforeEach(() => {
		vi.clearAllMocks();
	});

	describe('register', () => {
		it('should register user successfully', async () => {
			const mockUser = {
				id: 1,
				username: 'newuser',
				created_at: '2023-01-01T00:00:00Z'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockUser,
				error: null
			});

			const result = await register('newuser', 'password123');

			expect(client.POST).toHaveBeenCalledWith('/api/auth/register', {
				body: {
					username: 'newuser',
					password: 'password123'
				}
			});

			expect(result).toEqual(mockUser);
		});

		it('should throw error when API returns error with detail', async () => {
			const mockError = {
				detail: 'Username already exists'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(register('existinguser', 'password123')).rejects.toThrow(
				JSON.stringify(mockError.detail)
			);
		});

		it('should throw error when API returns error without detail', async () => {
			const mockError = {
				message: 'Server error'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(register('newuser', 'password123')).rejects.toThrow(
				'Registration failed'
			);
		});

		it('should handle empty username and password', async () => {
			const mockError = {
				detail: 'Username and password are required'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(register('', '')).rejects.toThrow(
				JSON.stringify(mockError.detail)
			);
		});

		it('should handle special characters in credentials', async () => {
			const mockUser = {
				id: 2,
				username: 'user@example.com',
				created_at: '2023-01-01T00:00:00Z'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockUser,
				error: null
			});

			const specialUsername = 'user@example.com';
			const specialPassword = 'P@ssw0rd!123';

			const result = await register(specialUsername, specialPassword);

			expect(client.POST).toHaveBeenCalledWith('/api/auth/register', {
				body: {
					username: specialUsername,
					password: specialPassword
				}
			});

			expect(result).toEqual(mockUser);
		});

		it('should handle long username and password', async () => {
			const mockUser = {
				id: 3,
				username: 'verylongusernamethatmightcausesomeissues',
				created_at: '2023-01-01T00:00:00Z'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockUser,
				error: null
			});

			const longUsername = 'verylongusernamethatmightcausesomeissues';
			const longPassword = 'verylongpasswordwithmanycharsandnumbers123456789';

			const result = await register(longUsername, longPassword);

			expect(client.POST).toHaveBeenCalledWith('/api/auth/register', {
				body: {
					username: longUsername,
					password: longPassword
				}
			});

			expect(result).toEqual(mockUser);
		});

		it('should handle network error', async () => {
			vi.mocked(client.POST).mockRejectedValueOnce(new Error('Network error'));

			await expect(register('newuser', 'password123')).rejects.toThrow('Network error');
		});
	});
});
