<script lang="ts">
	import '../app.css';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { Toaster } from '$lib/components/ui/sonner/index.js';
	import { ModeWatcher } from 'mode-watcher';

	let { data, children } = $props();
</script>

<ModeWatcher defaultMode={'dark'} />
<Toaster />
<QueryClientProvider client={data.queryClient}>
	{@render children()}
</QueryClientProvider>
