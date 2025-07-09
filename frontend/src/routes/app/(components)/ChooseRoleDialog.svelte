<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
	import { Button } from '$lib/components/ui/button';
	import { Check, Eye, Rocket, Code, TrendingUp, LoaderCircle } from '@lucide/svelte';
	import { Badge } from '@/components/ui/badge';
	import { cn } from '$lib/utils';
	import { setRole } from './dataLoaders';
	import { createMutation } from '@tanstack/svelte-query';
	import { goto } from '$app/navigation';
	import { toast } from 'svelte-sonner';
	import { type components } from '$lib/api/v1';

	type UserRole = components['schemas']['UserRole'];
	const roles = [
		{
			value: 'VIEWER' as UserRole,
			label: 'Viewer',
			description: 'Browse and explore content',
			icon: Eye,
			color: 'bg-blue-50 border-blue-200 hover:bg-blue-100',
			iconColor: 'text-blue-600'
		},
		{
			value: 'FOUNDER' as UserRole,
			label: 'Founder',
			description: 'Build and manage your startup',
			icon: Rocket,
			color: 'bg-purple-50 border-purple-200 hover:bg-purple-100',
			iconColor: 'text-purple-600'
		},
		{
			value: 'DEVELOPER' as UserRole,
			label: 'Developer',
			description: 'Create and contribute to projects',
			icon: Code,
			color: 'bg-green-50 border-green-200 hover:bg-green-100',
			iconColor: 'text-green-600'
		},
		{
			value: 'INVESTOR' as UserRole,
			label: 'Investor',
			description: 'Discover investment opportunities',
			icon: TrendingUp,
			color: 'bg-orange-50 border-orange-200 hover:bg-orange-100',
			iconColor: 'text-orange-600'
		}
	];

	let { open = $bindable(false) }: { open: boolean } = $props();
	let selectedRole: UserRole | null = $state(null);

	const setRoleMutation = createMutation({
		mutationFn: async (role: UserRole) => await setRole(role),
		onSuccess: () => {
			toast.success('Role set successfully! Redirecting...');
			// invalidateAll();
			goto('/app/explore');
		},
		onError: (error) => {
			toast.error(`Failed to set role: ${error.message}`);
		}
	});
</script>

<Dialog.Root bind:open>
	<Dialog.Content class="sm:max-w-md" interactOutsideBehavior="ignore">
		<Dialog.Header class="text-center">
			<Dialog.Title class="text-2xl font-semibold">Choose Your Role</Dialog.Title>
			<Dialog.Description class="text-muted-foreground">
				Select the role that best describes you to personalize your experience
			</Dialog.Description>
		</Dialog.Header>

		<div class="grid gap-3 py-4">
			{#each roles as role (role.value)}
				{@const isSelected = selectedRole === role.value}
				{@const Icon = role.icon}
				<button
					onclick={() => (selectedRole = role.value)}
					class={cn(
						'relative flex items-center gap-4 rounded-lg border-2 p-4 text-left transition-all duration-200',
						isSelected ? 'border-primary bg-primary/5 ring-primary/20 ring-2' : role.color
					)}
				>
					<div class={cn('rounded-lg p-2', isSelected ? 'bg-primary/10' : 'bg-white')}>
						<Icon class={cn('h-5 w-5', isSelected ? 'text-primary' : role.iconColor)} />
					</div>

					<div class="flex-1">
						<div class="flex items-center gap-2">
							<h3 class="text-foreground font-medium">{role.label}</h3>
							{#if isSelected}
								<Badge variant="default" class="h-5 px-2">
									<Check class="h-3 w-3" />
								</Badge>
							{/if}
						</div>
						<p class="text-muted-foreground mt-1 text-sm">{role.description}</p>
					</div>
				</button>
			{/each}
		</div>

		<div class="flex gap-3 pt-4">
			<Button
				onclick={() => {
					if (!selectedRole) {
						toast.error('Please select a role to continue.');
						return;
					}
					$setRoleMutation.mutate(selectedRole);
				}}
				disabled={!selectedRole}
				class="flex-1"
			>
				{#if $setRoleMutation.isPending}
					<LoaderCircle class="animate-spin" />
					Loading...
				{:else}
					Continue
				{/if}
			</Button>
		</div>
	</Dialog.Content>
</Dialog.Root>
