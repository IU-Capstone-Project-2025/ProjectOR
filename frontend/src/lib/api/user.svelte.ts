import { browser } from '$app/environment';
import { jwtDecode } from 'jwt-decode';

export interface UserSvelte {
	username: string;
}

interface JWTPayload {
	sub: string; // The subject of the JWT, typically username
}

class UserState {
	user: UserSvelte | null = $state(null);
	token: string | null = $state(null);

	/*
	 * Decode token and sets the user state and token.
	 * @param {string} token - The JWT token to set.
	 *
	 * @returns {User | null} - Returns the decoded user object if successful, otherwise returns null.
	 */
	set_token(token: string): UserSvelte | null {
		try {
			const decoded = jwtDecode<JWTPayload>(token);
			this.token = token;
			this.user = {
				username: decoded.sub
			};
			if (browser) {
				localStorage.setItem('authorization', `Bearer ${token}`);
			}
			return this.user;
		} catch (error) {
			console.error('Failed to decode JWT:', error);
			localStorage.removeItem('authorization');
			return null;
		}
	}

	/*
	 * Clears the user state and token.
	 */
	logout(): void {
		this.user = null;
		this.token = null;
		if (browser) {
			localStorage.removeItem('authorization');
		}
	}

	constructor() {
		if (browser) {
			const token = localStorage.getItem('authorization');
			if (token) {
				this.set_token(token.replace('Bearer ', ''));
			} else {
				this.user = null;
				this.token = null;
			}
		}
	}
}

export const userState = new UserState();
