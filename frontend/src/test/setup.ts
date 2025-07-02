import '@testing-library/jest-dom';

// Mock localStorage
Object.defineProperty(window, 'localStorage', {
	value: {
		getItem: vi.fn(),
		setItem: vi.fn(),
		removeItem: vi.fn(),
		clear: vi.fn(),
	},
	writable: true,
});

// Mock environment variables
vi.mock('$env/static/private', () => ({}));
vi.mock('$env/dynamic/private', () => ({}));

// Mock API base URL
vi.stubEnv('VITE_API_BASE_URL', 'http://localhost:8000');
