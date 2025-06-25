<script lang="ts">
	import { Button } from '@/components/ui/button';
	import { Skeleton } from '@/components/ui/skeleton';
	import * as Card from '@/components/ui/card';
	import { Label } from '@/components/ui/label';
	import { Input } from '@/components/ui/input';
	import * as Avatar from '@/components/ui/avatar';
</script>

<h1 class="mb-6 text-center text-2xl font-bold">Welcome to ProjectOR</h1>
<div class="flex flex-col items-center justify-center gap-4">
	<Button href="/auth/login">Go to Login</Button>
	<Button href="/auth/register">Go to Register</Button>
	<Button href="/app">Go to App</Button>
</div>

<h1 class="mt-32 text-center text-xl">Implemented components</h1>
<div class="mt-4 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
	<Button>Button</Button>
	<Button variant="outline">Outline Button</Button>
	<Button disabled>Disabled Button</Button>
	<Button size="sm">Small Button</Button>
	<Button size="lg">Large Button</Button>
	<Button variant="ghost">Ghost Button</Button>
	<Button variant="destructive">Destructive Button</Button>
</div>
<div class="mt-4 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
	<Card.Root>
		<Card.Header>
			<Card.Title>Card Title</Card.Title>
		</Card.Header>
		<Card.Content>
			<p>This is a simple card component.</p>
		</Card.Content>
	</Card.Root>
	<Card.Root>
		<Card.Header>
			<Card.Title>Card with Skeleton</Card.Title>
		</Card.Header>
		<Card.Content>
			<Skeleton class="h-10 w-full" />
			<Skeleton class="mt-2 h-6 w-3/4" />
		</Card.Content>
	</Card.Root>
</div>
<div class="mt-4 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
	<Label>Email</Label>
	<Input type="email" placeholder="Enter your email" />
	<Label>Password</Label>
	<Input type="password" placeholder="Enter your password" />
	<Button>Submit</Button>
	<Button variant="outline">Outline Submit</Button>
	<Button disabled>Disabled Submit</Button>
</div>
<div class="mt-4 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
	<Avatar.Root>
		<Avatar.Image
			src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
			alt="User Avatar"
		/>
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
	<Avatar.Root>
		<Avatar.Image
			src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
			alt="User Avatar"
		/>
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
	<Avatar.Root>
		<Avatar.Image
			src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
			alt="User Avatar"
		/>
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
</div>
