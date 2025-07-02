import { describe, it, expect } from 'vitest';

describe('Test Setup', () => {
	it('should run vitest correctly', () => {
		expect(true).toBe(true);
	});

	it('should have access to vi global', () => {
		expect(typeof vi).toBe('object');
		expect(vi.fn).toBeDefined();
		expect(vi.mock).toBeDefined();
	});

	it('should have localStorage mock available', () => {
		expect(localStorage).toBeDefined();
		expect(localStorage.getItem).toBeDefined();
		expect(localStorage.setItem).toBeDefined();
		expect(localStorage.removeItem).toBeDefined();
		expect(localStorage.clear).toBeDefined();
	});

	it('should have environment variables mocked', () => {
		// Test that VITE_API_BASE_URL is available
		expect(import.meta.env.VITE_API_BASE_URL).toBe('http://localhost:8000');
	});
});
