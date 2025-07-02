<script lang="ts">
	import { CircleAlertIcon } from '@lucide/svelte';
	import * as Alert from '$lib/components/ui/alert';
	import { trim } from '@/utils';

	const { text }: { text: string } = $props();
</script>

<Alert.Root variant="destructive">
	<CircleAlertIcon class="size-4" />
	<Alert.Title>Error</Alert.Title>
	<Alert.Description>{trim(text, '"')}</Alert.Description>
</Alert.Root>
