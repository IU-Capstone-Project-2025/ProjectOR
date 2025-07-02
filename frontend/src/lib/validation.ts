/**
 * Validation utilities for form inputs
 */

export interface ValidationResult {
	isValid: boolean;
	errors: string[];
}

/**
 * Validate email format
 */
export function validateEmail(email: string): ValidationResult {
	const errors: string[] = [];
	
	if (!email || email.trim() === '') {
		errors.push('Email is required');
	} else {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if (!emailRegex.test(email)) {
			errors.push('Invalid email format');
		}
	}

	return {
		isValid: errors.length === 0,
		errors
	};
}

/**
 * Validate password strength
 */
export function validatePassword(password: string): ValidationResult {
	const errors: string[] = [];
	
	if (!password) {
		errors.push('Password is required');
	} else {
		if (password.length < 8) {
			errors.push('Password must be at least 8 characters long');
		}
		if (!/[A-Z]/.test(password)) {
			errors.push('Password must contain at least one uppercase letter');
		}
		if (!/[a-z]/.test(password)) {
			errors.push('Password must contain at least one lowercase letter');
		}
		if (!/\d/.test(password)) {
			errors.push('Password must contain at least one number');
		}
	}

	return {
		isValid: errors.length === 0,
		errors
	};
}

/**
 * Validate username
 */
export function validateUsername(username: string): ValidationResult {
	const errors: string[] = [];
	
	if (!username || username.trim() === '') {
		errors.push('Username is required');
	} else {
		if (username.length < 3) {
			errors.push('Username must be at least 3 characters long');
		}
		if (username.length > 50) {
			errors.push('Username must be less than 50 characters long');
		}
		if (!/^[a-zA-Z0-9_@.-]+$/.test(username)) {
			errors.push('Username can only contain letters, numbers, and the characters: _ @ . -');
		}
	}

	return {
		isValid: errors.length === 0,
		errors
	};
}

/**
 * Validate project title
 */
export function validateProjectTitle(title: string): ValidationResult {
	const errors: string[] = [];
	
	if (!title || title.trim() === '') {
		errors.push('Project title is required');
	} else {
		if (title.trim().length < 3) {
			errors.push('Project title must be at least 3 characters long');
		}
		if (title.trim().length > 100) {
			errors.push('Project title must be less than 100 characters long');
		}
	}

	return {
		isValid: errors.length === 0,
		errors
	};
}

/**
 * Validate project description
 */
export function validateProjectDescription(description: string): ValidationResult {
	const errors: string[] = [];
	
	// Description is optional, but if provided, should have some constraints
	if (description && description.length > 1000) {
		errors.push('Project description must be less than 1000 characters long');
	}

	return {
		isValid: errors.length === 0,
		errors
	};
}
