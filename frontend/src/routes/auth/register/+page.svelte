<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { goto } from '$app/navigation';
	import { createMutation } from '@tanstack/svelte-query';
	import { register } from './dataLoaders';
	import { toast } from 'svelte-sonner';
	import { LoaderCircle } from '@lucide/svelte';
	import { userState } from '@/api/user.svelte';

	const id = $props.id();

	let { username, password, confirmPassword } = $state({
		username: '',
		password: '',
		confirmPassword: ''
	});

	const registerMutation = createMutation({
		mutationFn: async () => await register(username, password),
		onSuccess: (data) => {
			toast.success('Registration successful! Redirecting...');
			userState.set_token(data.access_token);
			goto('/app');
		},
		onError: (error: Error) => {
			toast.error(`Registration failed: ${error.message}`);
		}
	});
</script>

<div class="flex flex-col gap-6">
	<Card.Root>
		<Card.Header class="text-center">
			<Card.Title class="text-xl">Welcome to ProjectOR</Card.Title>
			<Card.Description>Create your account to start collaborate!</Card.Description>
		</Card.Header>
		<Card.Content>
			<form>
				<div class="grid gap-6">
					<div class="grid gap-6">
						<div class="grid gap-3">
							<Label for="username-{id}">Username</Label>
							<Input bind:value={username} id="username-{id}" type="text" required />
						</div>
						<div class="grid gap-3">
							<Label for="password-{id}">Password</Label>
							<Input bind:value={password} id="password-{id}" type="password" required />
						</div>
						<div class="grid gap-3">
							<Label for="confirm-password-{id}">Confirm Password</Label>
							<Input
								bind:value={confirmPassword}
								id="confirm-password-{id}"
								type="password"
								required
							/>
						</div>
						<Button
							type="submit"
							class="w-full"
							disabled={!username ||
								!password ||
								password !== confirmPassword ||
								$registerMutation.isPending}
							onclick={() => $registerMutation.mutate()}
						>
							{#if $registerMutation.isPending}
								<LoaderCircle class="animate-spin" />
								Loading...
							{:else}
								Register
							{/if}
						</Button>
					</div>
					<div class="text-center text-sm">
						Already have an account?
						<a href="/auth/login" class="underline underline-offset-4"> Sign in </a>
					</div>
				</div>
			</form>
		</Card.Content>
	</Card.Root>
	<div
		class="text-muted-foreground *:[a]:hover:text-primary text-center text-xs text-balance *:[a]:underline *:[a]:underline-offset-4"
	>
		By clicking continue, you agree to our <a>Terms of Service</a>
		and <a>Privacy Policy</a>.
	</div>
</div>
