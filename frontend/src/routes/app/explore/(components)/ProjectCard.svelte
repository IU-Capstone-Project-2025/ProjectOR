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
	<Card.Root class="group hover:shadow-lg transition-all duration-200 cursor-pointer" onclick={handleViewProject}>
		<Card.Header class="pb-3">
			<div class="flex items-start justify-between">
				<Card.Title class="text-lg font-semibold line-clamp-2 group-hover:text-primary transition-colors">
					{project.title}
				</Card.Title>
				<Badge variant={project.is_public ? 'secondary' : 'outline'} class="ml-2 shrink-0">
					{#if project.is_public}
						<Globe class="h-3 w-3 mr-1" />
						Public
					{:else}
						<Lock class="h-3 w-3 mr-1" />
						Private
					{/if}
				</Badge>
			</div>
		</Card.Header>

		<Card.Content class="space-y-4">
			<p class="text-sm text-muted-foreground line-clamp-3 min-h-[3rem]">
				{project.description || 'No description available.'}
			</p>
			
			<div class="flex items-center justify-between text-xs text-muted-foreground">
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
				class="w-full group-hover:shadow-md transition-shadow"
				onclick={(e) => {
					e.stopPropagation();
					handleViewProject();
				}}
			>
				<Eye class="h-4 w-4 mr-2" />
				View Project
			</Button>
		</Card.Footer>
	</Card.Root>
{:else}
	<!-- List View -->
	<Card.Root class="group hover:shadow-md transition-all duration-200 cursor-pointer" onclick={handleViewProject}>
		<Card.Content class="p-6">
			<div class="flex items-center justify-between">
				<div class="flex-1 min-w-0">
					<div class="flex items-center gap-3 mb-2">
						<h3 class="text-lg font-semibold truncate group-hover:text-primary transition-colors">
							{project.title}
						</h3>
						<Badge variant={project.is_public ? 'secondary' : 'outline'}>
							{#if project.is_public}
								<Globe class="h-3 w-3 mr-1" />
								Public
							{:else}
								<Lock class="h-3 w-3 mr-1" />
								Private
							{/if}
						</Badge>
					</div>
					<p class="text-sm text-muted-foreground line-clamp-2 mb-3">
						{project.description || 'No description available.'}
					</p>
					<div class="flex items-center gap-4 text-xs text-muted-foreground">
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
				<div class="flex items-center gap-2 ml-4">
					<Button 
						variant="default" 
						size="sm"
						onclick={(e) => {
							e.stopPropagation();
							handleViewProject();
						}}
					>
						<Eye class="h-4 w-4 mr-2" />
						View
					</Button>
				</div>
			</div>
		</Card.Content>
	</Card.Root>
{/if}
