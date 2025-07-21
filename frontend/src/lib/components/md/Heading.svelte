<script>
	export let depth;
	export let raw;
	export let text;
	export let id = `heading-${Math.random().toString(36)}`;
</script>

{#if depth === 1}
	<h1 class="mt-4 mb-4 scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl" {id}>
		<slot></slot>
	</h1>
{:else if depth === 2}
	<h2
		class="mt-4 scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0"
		{id}
	>
		<slot></slot>
	</h2>
{:else if depth === 3}
	<h3 class="mt-4 scroll-m-20 text-2xl font-semibold tracking-tight" {id}>
		<slot></slot>
	</h3>
{:else if depth === 4}
	<h4 class="mt-4 scroll-m-20 text-xl font-semibold tracking-tight" {id}>
		<slot></slot>
	</h4>
{:else if depth === 5}
	<h5 class="mt-4 scroll-m-20 text-lg font-semibold tracking-tight" {id}>
		<slot></slot>
	</h5>
{:else if depth === 6}
	<h6 class="mt-4 scroll-m-20 text-base font-semibold tracking-tight" {id}>
		<slot></slot>
	</h6>
{:else}
	{raw}
{/if}
