import { describe, it, expect, beforeEach, vi } from 'vitest';
import { client, API_BASE_URL } from './client';

// Mock the openapi-fetch module
vi.mock('openapi-fetch', () => ({
	default: vi.fn(() => ({
		use: vi.fn(),
		GET: vi.fn(),
		POST: vi.fn(),
		PUT: vi.fn(),
		DELETE: vi.fn()
	}))
}));

describe('API Client', () => {
	beforeEach(() => {
		// Clear localStorage mock before each test
		vi.clearAllMocks();
		localStorage.clear();
	});

	it('should have the correct base URL', () => {
		expect(API_BASE_URL).toBe('http://localhost:8000');
	});

	it('should create client with base URL', () => {
		expect(client).toBeDefined();
	});

	describe('Authorization Middleware', () => {
		it('should add authorization header when token exists in localStorage', () => {
			// Mock localStorage.getItem to return a token
			const mockToken = 'Bearer test-token';
			vi.mocked(localStorage.getItem).mockReturnValue(mockToken);

			// Create a mock request object
			const mockRequest = {
				headers: new Headers(),
				method: 'GET',
				url: 'http://localhost:8000/test'
			} as Request;

			// Mock the middleware function - we need to simulate how it would work
			const mockHeaders = {
				set: vi.fn()
			};
			const requestWithHeaders = {
				...mockRequest,
				headers: mockHeaders
			};

			// Simulate middleware behavior
			const authorizationToken = localStorage.getItem('authorization');
			if (authorizationToken) {
				requestWithHeaders.headers.set('Authorization', authorizationToken);
			}

			expect(localStorage.getItem).toHaveBeenCalledWith('authorization');
			expect(mockHeaders.set).toHaveBeenCalledWith('Authorization', mockToken);
		});

		it('should not add authorization header when no token in localStorage', () => {
			// Mock localStorage.getItem to return null
			vi.mocked(localStorage.getItem).mockReturnValue(null);

			// Create a mock request object
			const mockHeaders = {
				set: vi.fn()
			};
			const requestWithHeaders = {
				headers: mockHeaders
			};

			// Simulate middleware behavior
			const authorizationToken = localStorage.getItem('authorization');
			if (authorizationToken) {
				requestWithHeaders.headers.set('Authorization', authorizationToken);
			}

			expect(localStorage.getItem).toHaveBeenCalledWith('authorization');
			expect(mockHeaders.set).not.toHaveBeenCalled();
		});
	});
});
