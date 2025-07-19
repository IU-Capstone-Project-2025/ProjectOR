<script>
	export let ordered;
	export let start;
</script>

{#if ordered}
	<ol {start} class="my-6 ml-6 list-decimal [&>li]:mt-2"><slot></slot></ol>
{:else}
	<ul class="my-6 ml-6 list-disc [&>li]:mt-2"><slot></slot></ul>
{/if}
