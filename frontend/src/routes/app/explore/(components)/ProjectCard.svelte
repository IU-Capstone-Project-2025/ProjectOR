<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Button } from '$lib/components/ui/button';
	import { type components } from '@/api/v1';

	const { project }: { project: components['schemas']['ProjectSchema'] } = $props();
</script>

<Card.Root class="w-full max-w-md p-6">
	<Card.Header>
		<Card.Title class="text-xl">
			{project.title}
		</Card.Title>
	</Card.Header>

	<Card.Content class="flex h-32 flex-col gap-4 text-sm">
		<p class="truncate text-balance text-wrap">{project.description}</p>
	</Card.Content>
	<Card.Footer class="flex justify-end">
		<Button variant="default">View Project</Button>
	</Card.Footer>
</Card.Root>
