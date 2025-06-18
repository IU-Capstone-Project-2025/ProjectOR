<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';

	const id = $props.id();

	let { email, password, confirmPassword } = $state({
		email: '',
		password: '',
		confirmPassword: ''
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
							disabled={!email || !password || password !== confirmPassword}
							>Register
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
		By clicking continue, you agree to our <a href="##">Terms of Service</a>
		and <a href="##">Privacy Policy</a>.
	</div>
</div>
