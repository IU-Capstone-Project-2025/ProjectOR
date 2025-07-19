<script>
	export let header;
	export let align;
</script>

{#if header}
	<th
		{align}
		class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right"
		><slot></slot></th
	>
{:else}
	<td
		{align}
		class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right"
		><slot></slot></td
	>
{/if}
