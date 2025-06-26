<script lang="ts">
	import ProjectSkeleton from '$lib/components/skeletons/ProjectSkeleton.svelte';
	import { getProjects } from './(components)/dataLoaders';
	import { createQuery } from '@tanstack/svelte-query';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import ProjectCard from './(components)/ProjectCard.svelte';
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import * as Card from '$lib/components/ui/card';
	import { Search, Filter, Grid3X3, List } from '@lucide/svelte';
	import { type components } from '@/api/v1';

	type Project = components['schemas']['ProjectSchema'];

	let searchTerm = $state('');
	let showPublicOnly = $state(false);
	let viewMode = $state<'grid' | 'list'>('grid');

	const projectsQuery = createQuery({
		queryKey: ['projects'],
		queryFn: async () => await getProjects()
	});

	$effect(() => {
		// You can add search logic here if needed
	});

	const filteredProjects = $derived(() => {
		if (!$projectsQuery.data) return [];
		let filtered = $projectsQuery.data;
		
		if (searchTerm) {
			filtered = filtered.filter((project: Project) => 
				project.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
				(project.description && project.description.toLowerCase().includes(searchTerm.toLowerCase()))
			);
		}
		
		if (showPublicOnly) {
			filtered = filtered.filter((project: Project) => project.is_public);
		}
		
		return filtered;
	});
</script>

<div class="container mx-auto px-4 py-6 space-y-6">
	<!-- Header Section -->
	<div class="flex flex-col gap-4">
		<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
			<div>
				<h1 class="text-3xl font-bold tracking-tight">Explore Projects</h1>
				<p class="text-muted-foreground mt-1">Discover amazing projects from the community</p>
			</div>
			<div class="flex items-center gap-2">
				<Button 
					variant={viewMode === 'grid' ? 'default' : 'outline'} 
					size="sm"
					onclick={() => viewMode = 'grid'}
				>
					<Grid3X3 class="h-4 w-4" />
				</Button>
				<Button 
					variant={viewMode === 'list' ? 'default' : 'outline'} 
					size="sm"
					onclick={() => viewMode = 'list'}
				>
					<List class="h-4 w-4" />
				</Button>
			</div>
		</div>

		<!-- Search and Filter Section -->
		<Card.Root class="p-4">
			<div class="flex flex-col md:flex-row gap-4">
				<div class="relative flex-1">
					<Search class="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
					<Input
						bind:value={searchTerm}
						placeholder="Search projects by title or description..."
						class="pl-10"
					/>
				</div>
				<div class="flex items-center gap-4">
					<label class="flex items-center gap-2 text-sm">
						<input 
							type="checkbox" 
							bind:checked={showPublicOnly}
							class="rounded"
						/>
						Public only
					</label>
					<Button variant="outline" size="sm">
						<Filter class="h-4 w-4 mr-2" />
						Filters
					</Button>
				</div>
			</div>
		</Card.Root>
	</div>

	<!-- Results Section -->
	<div class="space-y-4">
		{#if $projectsQuery.isPending}
			<div class={viewMode === 'grid' ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6' : 'space-y-4'}>
				{#each Array(12) as _}
					<ProjectSkeleton />
				{/each}
			</div>
		{:else if $projectsQuery.isError}
			<div class="flex justify-center py-12">
				<ErrorAlert text={$projectsQuery.error.message} />
			</div>
		{:else}
			<!-- Results Count -->
			<div class="flex items-center justify-between">
				<p class="text-sm text-muted-foreground">
					Showing {filteredProjects().length} of {$projectsQuery.data.length} projects
				</p>
			</div>

			{#if filteredProjects().length === 0}
				<div class="flex flex-col items-center justify-center py-12 text-center">
					<div class="rounded-full bg-muted p-3 mb-4">
						<Search class="h-6 w-6 text-muted-foreground" />
					</div>
					<h3 class="text-lg font-semibold mb-2">No projects found</h3>
					<p class="text-muted-foreground mb-4">Try adjusting your search or filters</p>
					<Button variant="outline" onclick={() => { searchTerm = ''; showPublicOnly = false; }}>
						Clear filters
					</Button>
				</div>
			{:else}
				<div class={viewMode === 'grid' ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6' : 'space-y-4'}>
					{#each filteredProjects() as project(project.title)}
						<ProjectCard {project} {viewMode} />
					{/each}
				</div>
			{/if}
		{/if}
	</div>
</div>
