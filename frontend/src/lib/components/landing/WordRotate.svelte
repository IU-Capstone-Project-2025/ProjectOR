<script lang="ts">
	import { cn } from '$lib/utils';
	import { onMount } from 'svelte';

	const {
		words,
		duration = 2100,
		class: className = ''
	}: {
		words: string[];
		duration?: number;
		class?: string;
	} = $props();

	let index = $state(0);
	const changeIndex = () => {
		index = (index + 1) % words.length;
	};
	onMount(() => {
		let interval = setInterval(changeIndex, duration);
		return () => clearInterval(interval);
	});
</script>

<div class="overflow-hidden py-2">
	{#key index}
		<h1 class={cn(className, 'text-center')}>
			{words[index]}
		</h1>
	{/key}
</div>
