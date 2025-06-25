<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Label } from '$lib/components/ui/label/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import { goto } from '$app/navigation';

	const id = $props.id();

	let { email, password } = $state({
		email: '',
		password: ''
	});
</script>

<div class="flex flex-col gap-6">
	<Card.Root>
		<Card.Header class="text-center">
			<Card.Title class="text-xl">Welcome back</Card.Title>
			<Card.Description>Sign in to your account to continue collaborating!</Card.Description>
		</Card.Header>
		<Card.Content>
			<form>
				<div class="grid gap-6">
					<div class="grid gap-6">
						<div class="grid gap-3">
							<Label for="email-{id}">Email</Label>
							<Input
								bind:value={email}
								id="email-{id}"
								type="email"
								placeholder="m@example.com"
								required
							/>
						</div>
						<div class="grid gap-3">
							<Label for="password-{id}">Password</Label>
							<Input bind:value={password} id="password-{id}" type="password" required />
						</div>
						<Button
							type="submit"
							class="w-full"
							disabled={!email || !password}
							onclick={() => {
								goto('/app');
							}}
							>Login
						</Button>
					</div>
					<div class="text-center text-sm">
						Don&apos;t have an account?
						<a href="/auth/register" class="underline underline-offset-4"> Sign up </a>
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
