<script lang="ts">
	import { Button } from '@/components/ui/button';
	import { Skeleton } from '@/components/ui/skeleton';
	import * as Card from '@/components/ui/card';
	import { Label } from '@/components/ui/label';
	import { Input } from '@/components/ui/input';
	import * as Avatar from '@/components/ui/avatar';
</script>

<h1 class="text-2xl font-bold text-center mb-6">
	Welcome to ProjectOR
</h1>
<div class="flex flex-col gap-4 items-center justify-center">
	<Button
		href="/auth/login"
	>
		Go to Login
	</Button>
	<Button
		href="/auth/register"
	>
		Go to Register
	</Button>
	<Button
		href="/app"
	>
		Go to App
	</Button>
</div>

<h1 class="text-center text-xl mt-32">
	Implemented components
</h1>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
	<Button>Button</Button>
	<Button variant="outline">Outline Button</Button>
	<Button disabled>Disabled Button</Button>
	<Button size="sm">Small Button</Button>
	<Button size="lg">Large Button</Button>
	<Button variant="ghost">Ghost Button</Button>
	<Button variant="destructive">Destructive Button</Button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
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
			<Skeleton class="h-6 w-3/4 mt-2" />
		</Card.Content>
	</Card.Root>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
	<Label>Email</Label>
	<Input type="email" placeholder="Enter your email" />
	<Label>Password</Label>
	<Input type="password" placeholder="Enter your password" />
	<Button>Submit</Button>
	<Button variant="outline">Outline Submit</Button>
	<Button disabled>Disabled Submit</Button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
	<Avatar.Root>
		<Avatar.Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
									alt="User Avatar" />
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
	<Avatar.Root>
		<Avatar.Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
									alt="User Avatar" />
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
	<Avatar.Root>
		<Avatar.Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ybci_L25OcWJhFyrcmoR4q_vsqoAtT_Qug&s"
									alt="User Avatar" />
		<Avatar.Fallback>U</Avatar.Fallback>
	</Avatar.Root>
</div>

