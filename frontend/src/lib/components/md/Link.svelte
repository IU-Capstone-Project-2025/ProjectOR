<script>
	export let href = '';
	export let title = undefined;
</script>

<a {href} {title} class="text-primary font-medium underline underline-offset-4">
	<slot></slot>
</a>
