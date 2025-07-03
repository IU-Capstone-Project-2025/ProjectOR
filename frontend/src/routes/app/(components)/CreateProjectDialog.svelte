<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import { Textarea } from '@/components/ui/textarea';
	import { createMutation, useQueryClient } from '@tanstack/svelte-query';
	import { toast } from 'svelte-sonner';
	import { createProject } from './dataLoaders';
	import { LoaderCircle } from '@lucide/svelte';

	let name = $state('');
	let description = $state('');

	let { open = $bindable(false) }: { open: boolean } = $props();
	const id = $props.id();

	const queryClient = useQueryClient();

	const createProjectMutation = createMutation({
		mutationFn: async ({ title, description }: { title: string; description: string }) =>
			await createProject(title, description),
		onSuccess: () => {
			queryClient.invalidateQueries({ queryKey: ['projects'] });
			toast.success('Project created successfully');
			open = false;
			name = '';
			description = '';
		},
		onError: (error) => {
			toast.error(`Failed to create project: ${error.message}`);
		}
	});
</script>

<Dialog.Root bind:open>
	<Dialog.Content class="sm:max-w-2xl">
		<Dialog.Header>
			<Dialog.Title>Create Project</Dialog.Title>
			<Dialog.Description>Fill in the details below to create a new project.</Dialog.Description>
		</Dialog.Header>
		<div class="grid gap-4 py-4">
			<div class="grid grid-cols-4 items-center gap-4">
				<Label for="name-{id}" class="text-right">Name</Label>
				<Input bind:value={name} id="name-{id}" class="col-span-3" />
			</div>
			<div class="grid grid-cols-4 items-center gap-4">
				<Label for="username-{id}" class="text-right">Description</Label>
				<Textarea
					bind:value={description}
					id="username-{id}"
					class="col-span-3 max-h-40"
					placeholder="Enter a brief description of the project"
				/>
			</div>
		</div>
		<Dialog.Footer>
			<Button
				type="submit"
				disabled={!name || !description || $createProjectMutation.isPending}
				onclick={() => $createProjectMutation.mutate({ title: name, description })}
			>
				{#if $createProjectMutation.isPending}
					<LoaderCircle class="animate-spin" />
					Loading...
				{:else}
					Create Project
				{/if}
			</Button>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
