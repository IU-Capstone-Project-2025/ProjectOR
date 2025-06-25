<script lang="ts">
	import ProjectSkeleton from '$lib/components/skeletons/ProjectSkeleton.svelte';
</script>

<div class="flex flex-row flex-wrap gap-6 p-4">
	{#each Array(12) as _}
		<ProjectSkeleton />
	{/each}
</div>
