import { describe, it, expect } from 'vitest';
import {
	validateEmail,
	validatePassword,
	validateUsername,
	validateProjectTitle,
	validateProjectDescription
} from './validation';

describe('Validation utilities', () => {
	describe('validateEmail', () => {
		it('should validate correct email formats', () => {
			const validEmails = [
				'test@example.com',
				'user.name@domain.org',
				'user+tag@domain.co.uk',
				'123@numbers.com'
			];

			validEmails.forEach(email => {
				const result = validateEmail(email);
				expect(result.isValid).toBe(true);
				expect(result.errors).toHaveLength(0);
			});
		});

		it('should reject invalid email formats', () => {
			const invalidEmails = [
				'invalid-email',
				'@domain.com',
				'user@',
				'user space@domain.com',
				'user@@domain.com'
			];

			invalidEmails.forEach(email => {
				const result = validateEmail(email);
				expect(result.isValid).toBe(false);
				expect(result.errors).toContain('Invalid email format');
			});
		});

		it('should require email', () => {
			const result = validateEmail('');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Email is required');
		});
	});

	describe('validatePassword', () => {
		it('should validate strong passwords', () => {
			const strongPasswords = [
				'Password123',
				'MyStr0ngP@ss',
				'SecurePass1',
				'C0mpl3xP@ssw0rd'
			];

			strongPasswords.forEach(password => {
				const result = validatePassword(password);
				expect(result.isValid).toBe(true);
				expect(result.errors).toHaveLength(0);
			});
		});

		it('should reject passwords without uppercase letters', () => {
			const result = validatePassword('password123');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Password must contain at least one uppercase letter');
		});

		it('should reject passwords without lowercase letters', () => {
			const result = validatePassword('PASSWORD123');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Password must contain at least one lowercase letter');
		});

		it('should reject passwords without numbers', () => {
			const result = validatePassword('Password');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Password must contain at least one number');
		});

		it('should reject short passwords', () => {
			const result = validatePassword('Pass1');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Password must be at least 8 characters long');
		});

		it('should require password', () => {
			const result = validatePassword('');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Password is required');
		});
	});

	describe('validateUsername', () => {
		it('should validate correct usernames', () => {
			const validUsernames = [
				'user123',
				'test_user',
				'user.name',
				'user@domain.com',
				'user-name'
			];

			validUsernames.forEach(username => {
				const result = validateUsername(username);
				expect(result.isValid).toBe(true);
				expect(result.errors).toHaveLength(0);
			});
		});

		it('should reject usernames with invalid characters', () => {
			const result = validateUsername('user name'); // space not allowed
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Username can only contain letters, numbers, and the characters: _ @ . -');
		});

		it('should reject short usernames', () => {
			const result = validateUsername('ab');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Username must be at least 3 characters long');
		});

		it('should reject long usernames', () => {
			const longUsername = 'a'.repeat(51);
			const result = validateUsername(longUsername);
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Username must be less than 50 characters long');
		});

		it('should require username', () => {
			const result = validateUsername('');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Username is required');
		});
	});

	describe('validateProjectTitle', () => {
		it('should validate correct project titles', () => {
			const validTitles = [
				'My Project',
				'Project 123',
				'A Valid Project Title'
			];

			validTitles.forEach(title => {
				const result = validateProjectTitle(title);
				expect(result.isValid).toBe(true);
				expect(result.errors).toHaveLength(0);
			});
		});

		it('should reject short titles', () => {
			const result = validateProjectTitle('ab');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Project title must be at least 3 characters long');
		});

		it('should reject long titles', () => {
			const longTitle = 'a'.repeat(101);
			const result = validateProjectTitle(longTitle);
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Project title must be less than 100 characters long');
		});

		it('should require title', () => {
			const result = validateProjectTitle('');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Project title is required');
		});

		it('should handle whitespace-only titles', () => {
			const result = validateProjectTitle('   ');
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Project title is required');
		});
	});

	describe('validateProjectDescription', () => {
		it('should validate correct descriptions', () => {
			const validDescriptions = [
				'',
				'A short description',
				'A longer description with more details about the project'
			];

			validDescriptions.forEach(description => {
				const result = validateProjectDescription(description);
				expect(result.isValid).toBe(true);
				expect(result.errors).toHaveLength(0);
			});
		});

		it('should reject very long descriptions', () => {
			const longDescription = 'a'.repeat(1001);
			const result = validateProjectDescription(longDescription);
			expect(result.isValid).toBe(false);
			expect(result.errors).toContain('Project description must be less than 1000 characters long');
		});

		it('should allow exactly 1000 characters', () => {
			const maxDescription = 'a'.repeat(1000);
			const result = validateProjectDescription(maxDescription);
			expect(result.isValid).toBe(true);
			expect(result.errors).toHaveLength(0);
		});
	});
});
