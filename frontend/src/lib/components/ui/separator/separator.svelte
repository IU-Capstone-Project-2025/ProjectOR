<script lang="ts">
	import { cn } from '$lib/utils';

	let {
		class: className,
		orientation = 'horizontal',
		decorative = true,
		...restProps
	}: {
		class?: string;
		orientation?: 'horizontal' | 'vertical';
		decorative?: boolean;
	} & import('svelte/elements').HTMLAttributes<HTMLDivElement> = $props();
</script>

<div
	class={cn(
		'shrink-0 bg-border',
		orientation === 'horizontal' ? 'h-[1px] w-full' : 'h-full w-[1px]',
		className
	)}
	{...restProps}
	role={decorative ? 'none' : 'separator'}
	aria-orientation={orientation}
></div>
