<script lang="ts">
	import { Skeleton } from '$lib/components/ui/skeleton';
	import * as Card from '$lib/components/ui/card';
</script>

<Card.Root class="w-full max-w-md mx-auto p-6">
	<Card.Header>
		<Card.Title class="text-xl">
			<Skeleton />
		</Card.Title>
	</Card.Header>

	<Card.Content class="flex flex-col gap-4">
		<Skeleton class="h-8 w-48" />
		<Skeleton class="h-6 w-64" />
		<div class="grid gap-4">
			<Skeleton class="h-10 w-full" />
			<Skeleton class="h-10 w-full" />
			<Skeleton class="h-10 w-full" />
		</div>
	</Card.Content>
</Card.Root>
