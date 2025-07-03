<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button';
	import * as Avatar from '$lib/components/ui/avatar';
	import { type components } from '@/api/v1';
	import { Badge } from '$lib/components/ui/badge';
	import { Eye, Lock, Globe, Calendar, User } from '@lucide/svelte';
	import { goto } from '$app/navigation';

	const {
		project,
		viewMode = 'grid'
	}: {
		project: components['schemas']['ProjectSchema'] & { id: number };
		viewMode?: 'grid' | 'list';
	} = $props();

	function handleViewProject() {
		goto(`/app/projects/${project.id}`);
	}

	function formatDate(dateString?: string) {
		if (!dateString) return 'Recently';
		try {
			return new Date(dateString).toLocaleDateString();
		} catch {
			return 'Recently';
		}
	}
</script>

{#if viewMode === 'grid'}
	<Card.Root
		class="group cursor-pointer transition-all duration-200 hover:shadow-lg"
		onclick={handleViewProject}
	>
		<Card.Header class="pb-3">
			<div class="flex items-start justify-between">
				<Card.Title
					class="group-hover:text-primary line-clamp-2 text-lg font-semibold transition-colors"
				>
					{project.title}
				</Card.Title>
				<Badge variant={project.is_public ? 'secondary' : 'outline'} class="ml-2 shrink-0">
					{#if project.is_public}
						<Globe class="mr-1 h-3 w-3" />
						Public
					{:else}
						<Lock class="mr-1 h-3 w-3" />
						Private
					{/if}
				</Badge>
			</div>
		</Card.Header>

		<Card.Content class="space-y-4">
			<p class="text-muted-foreground line-clamp-3 min-h-[3rem] text-sm">
				{project.description || 'No description available.'}
			</p>

			<div class="text-muted-foreground flex items-center justify-between text-xs">
				<div class="flex items-center gap-1">
					<User class="h-3 w-3" />
					<span>Project Owner</span>
				</div>
				<div class="flex items-center gap-1">
					<Calendar class="h-3 w-3" />
					<span>{formatDate()}</span>
				</div>
			</div>
		</Card.Content>

		<Card.Footer class="pt-4">
			<Button
				variant="default"
				size="sm"
				class="w-full transition-shadow group-hover:shadow-md"
				onclick={(e) => {
					e.stopPropagation();
					handleViewProject();
				}}
			>
				<Eye class="mr-2 h-4 w-4" />
				View Project
			</Button>
		</Card.Footer>
	</Card.Root>
{:else}
	<!-- List View -->
	<Card.Root
		class="group cursor-pointer transition-all duration-200 hover:shadow-md"
		onclick={handleViewProject}
	>
		<Card.Content class="p-6">
			<div class="flex items-center justify-between">
				<div class="min-w-0 flex-1">
					<div class="mb-2 flex items-center gap-3">
						<h3 class="group-hover:text-primary truncate text-lg font-semibold transition-colors">
							{project.title}
						</h3>
						<Badge variant={project.is_public ? 'secondary' : 'outline'}>
							{#if project.is_public}
								<Globe class="mr-1 h-3 w-3" />
								Public
							{:else}
								<Lock class="mr-1 h-3 w-3" />
								Private
							{/if}
						</Badge>
					</div>
					<p class="text-muted-foreground mb-3 line-clamp-2 text-sm">
						{project.description || 'No description available.'}
					</p>
					<div class="text-muted-foreground flex items-center gap-4 text-xs">
						<div class="flex items-center gap-1">
							<User class="h-3 w-3" />
							<span>Project Owner</span>
						</div>
						<div class="flex items-center gap-1">
							<Calendar class="h-3 w-3" />
							<span>{formatDate()}</span>
						</div>
					</div>
				</div>
				<div class="ml-4 flex items-center gap-2">
					<Button
						variant="default"
						size="sm"
						onclick={(e) => {
							e.stopPropagation();
							handleViewProject();
						}}
					>
						<Eye class="mr-2 h-4 w-4" />
						View
					</Button>
				</div>
			</div>
		</Card.Content>
	</Card.Root>
{/if}
