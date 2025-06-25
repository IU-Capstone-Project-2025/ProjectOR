<script lang="ts">
	import ProjectSkeleton from '$lib/components/skeletons/ProjectSkeleton.svelte';
	import { getProjects } from './(components)/dataLoaders';
	import { createQuery } from '@tanstack/svelte-query';
	import ErrorAlert from '@/components/ErrorAlert.svelte';
	import ProjectCard from './(components)/ProjectCard.svelte';

	const projectsQuery = createQuery({
		queryKey: ['projects'],
		queryFn: async () => await getProjects()
	});
</script>

<div class="flex flex-row flex-wrap gap-6 p-4 justify-start">
	{#if $projectsQuery.isPending}
		{#each Array(12) as _}
			<ProjectSkeleton />
		{/each}
	{:else if $projectsQuery.isError}
		<ErrorAlert text={$projectsQuery.error.message} />
	{:else}
		{#if $projectsQuery.data.length === 0}
			<p class="text-gray-500 w-full text-center">No projects found.</p>
		{:else}
			{#each $projectsQuery.data as project}
				<ProjectCard {project} />
			{/each}
		{/if}
	{/if}
</div>
