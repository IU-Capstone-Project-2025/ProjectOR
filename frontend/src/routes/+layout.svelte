<script lang="ts">
	import '../app.css';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { Toaster } from '$lib/components/ui/sonner/index.js';

	let { data, children } = $props();
</script>

<Toaster />
<QueryClientProvider client={data.queryClient}>
	{@render children()}
</QueryClientProvider>
