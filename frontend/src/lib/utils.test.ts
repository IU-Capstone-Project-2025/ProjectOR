import { describe, it, expect } from 'vitest';
import { cn, trim } from './utils';

describe('utils', () => {
	describe('cn', () => {
		it('should merge class names', () => {
			expect(cn('px-2 py-1', 'text-red-500')).toBe('px-2 py-1 text-red-500');
		});

		it('should merge tailwind classes with conflict resolution', () => {
			expect(cn('px-2 px-4')).toBe('px-4');
		});

		it('should handle conditional classes', () => {
			expect(cn('px-2', true && 'py-1', false && 'text-red-500')).toBe('px-2 py-1');
		});

		it('should handle arrays and objects', () => {
			expect(cn(['px-2', 'py-1'], { 'text-red-500': true, 'bg-blue-500': false })).toBe('px-2 py-1 text-red-500');
		});
	});

	describe('trim', () => {
		it('should trim specific character from start and end', () => {
			expect(trim('"hello world"', '"')).toBe('hello world');
		});

		it('should trim multiple characters from start and end', () => {
			expect(trim('"""hello world"""', '"')).toBe('hello world');
		});

		it('should not trim characters in the middle', () => {
			expect(trim('"hello " world"', '"')).toBe('hello " world');
		});

		it('should return original string if no trimming needed', () => {
			expect(trim('hello world', '"')).toBe('hello world');
		});

		it('should handle empty string', () => {
			expect(trim('', '"')).toBe('');
		});

		it('should handle string with only trim characters', () => {
			expect(trim('"""', '"')).toBe('');
		});
	});
});
