<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import projector_logo from '$lib/assets/projector_logo.jpg';
	import CircleUserRound from '@lucide/svelte/icons/circle-user-round';
	import Plus from '@lucide/svelte/icons/plus';
	import SquareChartGantt from '@lucide/svelte/icons/square-chart-gantt';
	import { onMount } from 'svelte';
	import { userState } from '@/api/user.svelte.js';
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { API_BASE_URL } from '@/api/client';
	import { Github, DoorClosed, Webhook, User, Settings, Globe, SunMoon } from '@lucide/svelte';
	import CreateProjectDialog from './(components)/CreateProjectDialog.svelte';
	import { toggleMode } from 'mode-watcher';

	const { children } = $props();

	let isCreateProjectDialogOpen = $state(false);

	onMount(() => {
		if (!userState.user) {
			goto('/auth/login');
		}
	});

	const PAGE_HEADERS: { [index: string]: string } = {
		'/app/explore': 'Explore Projects',
		'/app/profile': 'Profile',
		'/app/settings': 'Settings',
		'/app/projects': 'My Projects'
	};
</script>

<CreateProjectDialog bind:open={isCreateProjectDialogOpen} />
<div
	style="--sidebar-width: calc(var(--spacing) * 72); --header-height: calc(var(--spacing) * 12);"
>
	<header
		class="flex h-(--header-height) shrink-0 items-center gap-2 border-b transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-(--header-height)"
	>
		<div class="flex w-full items-center justify-between gap-1 px-4 lg:gap-2 lg:px-6">
			<a href="/app">
				<div class="flex items-center gap-2">
					<img src={projector_logo} alt="ProjectOR Logo" class="h-8 w-8 rounded-full" />
					<h1 class="text-base font-medium">
						{PAGE_HEADERS[page.url.pathname] || 'ProjectOR'}
					</h1>
				</div>
			</a>
			<div class="ml-auto flex items-center gap-2">
				<Button variant="default" onclick={() => (isCreateProjectDialogOpen = true)}>
					<Plus />
					Create Project
				</Button>
				<Button variant="outline">
					<SquareChartGantt />
					My Projects
				</Button>
				<DropdownMenu.Root>
					<DropdownMenu.Trigger>
						{#snippet child({ props })}
							<Button {...props} variant="ghost" size="icon" class="ml-10">
								<CircleUserRound />
							</Button>
						{/snippet}
					</DropdownMenu.Trigger>
					<DropdownMenu.Content class="w-56" align="start">
						<DropdownMenu.Label>{userState.user?.username}</DropdownMenu.Label>
						<DropdownMenu.Separator />
						<DropdownMenu.Group>
							<DropdownMenu.Item onclick={() => goto('/app/profile')}>
								<User />
								Profile
							</DropdownMenu.Item>
							<DropdownMenu.Item>
								<Settings />
								Settings
							</DropdownMenu.Item>
							<DropdownMenu.Item onclick={() => goto('/app/explore')}>
								<Globe />
								Explore
							</DropdownMenu.Item>
							<DropdownMenu.Item onclick={toggleMode}>
								<SunMoon />
								Toggle Theme
							</DropdownMenu.Item>
						</DropdownMenu.Group>
						<DropdownMenu.Separator />
						<DropdownMenu.Item
							onclick={() =>
								window.open('https://github.com/IU-Capstone-Project-2025/ProjectOR', '_blank')}
						>
							<Github />
							GitHub
						</DropdownMenu.Item>
						<DropdownMenu.Item onclick={() => window.open(`${API_BASE_URL}docs`, '_blank')}>
							<Webhook />
							API
						</DropdownMenu.Item>
						<DropdownMenu.Separator />
						<DropdownMenu.Item
							onclick={() => {
								userState.logout();
								goto('/auth/login');
							}}
						>
							<DoorClosed />
							Log out
						</DropdownMenu.Item>
					</DropdownMenu.Content>
				</DropdownMenu.Root>
			</div>
		</div>
	</header>
</div>

{@render children()}
