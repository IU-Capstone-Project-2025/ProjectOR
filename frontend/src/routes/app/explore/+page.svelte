<script lang="ts">
	import ProjectSkeleton from '$lib/components/skeletons/ProjectSkeleton.svelte';
	import { getProjects } from './(components)/dataLoaders';
	import { createQuery } from '@tanstack/svelte-query';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import ProjectCard from './(components)/ProjectCard.svelte';
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import * as Card from '$lib/components/ui/card';
	import * as Popover from '$lib/components/ui/popover';
	import * as Command from '$lib/components/ui/command';
	import { Search, Filter, Grid3X3, List, ChevronsUpDownIcon, CheckIcon } from '@lucide/svelte';
	import { type components } from '$lib/api/v1';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import { slide } from 'svelte/transition';
	import { cn } from '$lib/utils';
	import { Badge } from '@/components/ui/badge';

	type Project = components['schemas']['ProjectSchema'];

	const { data } = $props();

	let showFilters = $state(false);
	let searchTerm = $state('');
	let showGraveyardOnly = $state(false);
	let myProjectsOnly = $state(false);
	let selectedTags: string[] = $state([]);
	let viewMode: 'grid' | 'list' = $state('grid');

	const projectsQuery = createQuery({
		queryKey: ['projects'],
		queryFn: async () => await getProjects()
	});

	const filteredProjects = $derived(() => {
		if (!$projectsQuery.data) return [];
		let filtered = $projectsQuery.data;

		if (searchTerm) {
			filtered = filtered.filter(
				(project: Project) =>
					project.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
					(project.description &&
						project.description.toLowerCase().includes(searchTerm.toLowerCase()))
			);
		}

		if (showGraveyardOnly) {
			filtered = filtered.filter((project: Project) => project.is_dead);
		}

		if (myProjectsOnly) {
			filtered = filtered.filter((project: Project) => project.ceo_id === data.user?.id);
		}

		if (selectedTags.length > 0) {
			filtered = filtered.filter((project: Project) =>
				project.tags?.some((tag) => selectedTags.includes(tag.name))
			);
		}

		return filtered;
	});
</script>

<div class="container mx-auto space-y-6 px-4 py-6">
	<!-- Header Section -->
	<div class="flex flex-col gap-4">
		<div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
			<div>
				<h1 class="text-3xl font-bold tracking-tight">Explore Projects</h1>
				<p class="text-muted-foreground mt-1">Discover amazing projects from the community</p>
			</div>
			<div class="flex items-center gap-2">
				<Button
					variant={viewMode === 'grid' ? 'default' : 'outline'}
					size="sm"
					onclick={() => (viewMode = 'grid')}
				>
					<Grid3X3 class="h-4 w-4" />
				</Button>
				<Button
					variant={viewMode === 'list' ? 'default' : 'outline'}
					size="sm"
					onclick={() => (viewMode = 'list')}
				>
					<List class="h-4 w-4" />
				</Button>
			</div>
		</div>

		<!-- Search and Filter Section -->
		<Card.Root class="p-4">
			<div class="flex flex-col gap-4 md:flex-row">
				<div class="relative flex-1">
					<Search class="text-muted-foreground absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2" />
					<Input
						bind:value={searchTerm}
						placeholder="Search projects by title or description..."
						class="pl-10"
					/>
				</div>
				<div class="flex items-center gap-4">
					<label class="flex items-center gap-2 text-sm">
						<Checkbox bind:checked={myProjectsOnly} />
						My Projects Only
					</label>
					<Button variant="outline" size="sm" onclick={() => (showFilters = !showFilters)}>
						<Filter class="mr-2 h-4 w-4" />
						Filters
					</Button>
				</div>
			</div>
			{#if showFilters}
				<div class="space-y-4" transition:slide={{ duration: 300 }}>
					<div class="items center flex gap-2">
						<Checkbox bind:checked={showGraveyardOnly} />
						<Label>Show Graveyard Projects</Label>
					</div>
					<div class="flex items-center gap-2">
						<Popover.Root>
							<Popover.Trigger>
								{#snippet child({ props })}
									<Button
										{...props}
										variant="outline"
										role="combobox"
										class="no-scrollbar w-full overflow-x-scroll"
									>
										{#if selectedTags.length > 0}
											{#each selectedTags as tag (tag)}
												<Badge variant="outline">{tag}</Badge>
											{/each}
										{:else}
											Select tags
										{/if}
										<ChevronsUpDownIcon class="opacity-50" />
									</Button>
								{/snippet}
							</Popover.Trigger>
							<Popover.Content class="w-full" align="start">
								<Command.Root>
									<Command.Input placeholder="Search tags..." />
									<Command.List>
										<Command.Empty>No tags found.</Command.Empty>
										<Command.Group value="tags">
											{#if $projectsQuery.data}
												{#each $projectsQuery.data
													.map((project) => project.tags ?? [])
													.flat()
													.filter((tag, index, self) => self.indexOf(tag) === index)
													.sort((a, b) => a.name.localeCompare(b.name)) as tag (tag)}
													<Command.Item
														value={tag.name}
														onSelect={() => {
															if (selectedTags.includes(tag.name)) {
																selectedTags = selectedTags.filter((t) => t !== tag.name);
															} else {
																selectedTags = [...selectedTags, tag.name];
															}
														}}
													>
														<CheckIcon
															class={cn(!selectedTags.includes(tag.name) && 'text-transparent')}
														/>
														{tag.name}
													</Command.Item>
												{/each}
											{/if}
										</Command.Group>
									</Command.List>
								</Command.Root>
							</Popover.Content>
						</Popover.Root>
					</div>
					<Button
						variant="outline"
						onclick={() => {
							searchTerm = '';
							showGraveyardOnly = false;
							selectedTags = [];
							myProjectsOnly = false;
						}}
					>
						Clear filters
					</Button>
				</div>
			{/if}
		</Card.Root>
	</div>

	<!-- Results Section -->
	<div class="space-y-4">
		{#if $projectsQuery.isPending}
			<div
				class={viewMode === 'grid'
					? 'grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3'
					: 'space-y-4'}
			>
				{#each Array(12) as _ (_)}
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
				<p class="text-muted-foreground text-sm">
					Showing {filteredProjects().length} of {$projectsQuery.data.length} projects
				</p>
			</div>

			{#if filteredProjects().length === 0}
				<div class="flex flex-col items-center justify-center py-12 text-center">
					<div class="bg-muted mb-4 rounded-full p-3">
						<Search class="text-muted-foreground h-6 w-6" />
					</div>
					<h3 class="mb-2 text-lg font-semibold">No projects found</h3>
					<p class="text-muted-foreground mb-4">Try adjusting your search or filters</p>
					<Button
						variant="outline"
						onclick={() => {
							searchTerm = '';
							showGraveyardOnly = false;
							selectedTags = [];
							myProjectsOnly = false;
						}}
					>
						Clear filters
					</Button>
				</div>
			{:else}
				<div
					class={viewMode === 'grid'
						? 'grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3'
						: 'space-y-4'}
				>
					{#each filteredProjects() as project (project.title)}
						<ProjectCard {project} {viewMode} />
					{/each}
				</div>
			{/if}
		{/if}
	</div>
</div>
