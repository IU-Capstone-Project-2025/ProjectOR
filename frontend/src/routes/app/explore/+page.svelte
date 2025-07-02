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

<div class="flex flex-row flex-wrap justify-start gap-6 p-4">
	{#if $projectsQuery.isPending}
		{#each Array(12) as _ (_)}
			<ProjectSkeleton />
		{/each}
	{:else if $projectsQuery.isError}
		<ErrorAlert text={$projectsQuery.error.message} />
	{:else if $projectsQuery.data.length === 0}
		<p class="w-full text-center text-gray-500">No projects found.</p>
	{:else}
		{#each $projectsQuery.data as project (project.title)}
			<ProjectCard {project} />
		{/each}
	{/if}
</div>
