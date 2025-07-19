import { View, CodeXml, Crown, CircleDollarSign, type Icon } from '@lucide/svelte';
import type { Component } from 'svelte';

export const USER_ROLES: {
	[key: string]: {
		label: string;
		description: string;
		icon: Component<Icon>;
	};
} = {
	VIEWER: {
		label: 'Viewer',
		description: 'Can view projects and data, but cannot make changes.',
		icon: View
	},
	FOUNDER: {
		label: 'Founder',
		description: 'Can create and manage projects',
		icon: Crown
	},
	DEVELOPER: {
		label: 'Developer',
		description: 'Can contribute to projects and manage code.',
		icon: CodeXml
	},
	INVESTOR: {
		label: 'Investor',
		description: 'Can financially support projects.',
		icon: CircleDollarSign
	}
};
