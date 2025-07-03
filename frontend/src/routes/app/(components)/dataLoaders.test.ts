import { describe, it, expect, vi, beforeEach } from 'vitest';
import { createProject } from './dataLoaders';
import { client } from '@/api/client';

// Mock the API client
vi.mock('@/api/client', () => ({
	client: {
		POST: vi.fn()
	}
}));

describe('Project Data Loaders', () => {
	beforeEach(() => {
		vi.clearAllMocks();
	});

	describe('createProject', () => {
		it('should create project successfully', async () => {
			const mockProject = {
				id: 1,
				title: 'Test Project',
				description: 'Test Description',
				is_public: true,
				created_at: '2023-01-01T00:00:00Z',
				updated_at: '2023-01-01T00:00:00Z'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockProject,
				error: null
			});

			const result = await createProject('Test Project', 'Test Description');

			expect(client.POST).toHaveBeenCalledWith('/api/projects/', {
				body: {
					title: 'Test Project',
					description: 'Test Description',
					is_public: true
				}
			});

			expect(result).toEqual(mockProject);
		});

		it('should throw error when API returns error', async () => {
			const mockError = { detail: 'Project creation failed' };

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: mockError
			});

			await expect(createProject('Test Project', 'Test Description')).rejects.toThrow(
				JSON.stringify(mockError)
			);
		});

		it('should throw error when no data is returned', async () => {
			vi.mocked(client.POST).mockResolvedValueOnce({
				data: null,
				error: null
			});

			await expect(createProject('Test Project', 'Test Description')).rejects.toThrow(
				'Failed to create project'
			);
		});

		it('should handle empty title and description', async () => {
			const mockProject = {
				id: 2,
				title: '',
				description: '',
				is_public: true,
				created_at: '2023-01-01T00:00:00Z',
				updated_at: '2023-01-01T00:00:00Z'
			};

			vi.mocked(client.POST).mockResolvedValueOnce({
				data: mockProject,
				error: null
			});

			const result = await createProject('', '');

			expect(client.POST).toHaveBeenCalledWith('/api/projects/', {
				body: {
					title: '',
					description: '',
					is_public: true
				}
			});

			expect(result).toEqual(mockProject);
		});
	});
});
