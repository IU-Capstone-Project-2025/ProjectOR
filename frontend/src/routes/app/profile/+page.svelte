<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';
	import { Badge } from '$lib/components/ui/badge';
	import { Separator } from '$lib/components/ui/separator';
	import { userState } from '@/api/user.svelte';
	import {
		User,
		Mail,
		Calendar,
		Settings,
		Edit3,
		Save,
		X,
		Camera,
		Key,
		Shield,
		Bell
	} from '@lucide/svelte';
	import { toast } from 'svelte-sonner';

	let isEditing = $state(false);
	let editedProfile = $state({
		username: userState.user?.username || '',
		email: "",
		bio: '',
		location: '',
		website: ''
	});

	function handleEdit() {
		isEditing = true;
		editedProfile = {
			username: userState.user?.username || '',
			email: "",
			bio: '',
			location: '',
			website: ''
		};
	}

	function handleSave() {
		// Here you would typically make an API call to update the profile
		toast.success('Profile updated successfully!');
		isEditing = false;
	}

	function handleCancel() {
		isEditing = false;
		editedProfile = {
			username: userState.user?.username || '',
			email: '',
			bio: '',
			location: '',
			website: ''
		};
	}

	function formatDate(date: Date) {
		return date.toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'long',
			day: 'numeric'
		});
	}
</script>

<div class="container mx-auto max-w-4xl space-y-6 px-4 py-6">
	<!-- Header -->
	<div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
		<div>
			<h1 class="text-3xl font-bold tracking-tight">Profile</h1>
			<p class="text-muted-foreground mt-1">Manage your account settings and preferences</p>
		</div>
		{#if !isEditing}
			<Button onclick={handleEdit}>
				<Edit3 class="mr-2 h-4 w-4" />
				Edit Profile
			</Button>
		{/if}
	</div>

	<div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
		<!-- Profile Card -->
		<div class="lg:col-span-1">
			<Card.Root>
				<Card.Content class="p-6 text-center">
					<div class="relative mb-4">
						<Avatar.Root class="mx-auto h-24 w-24">
							<Avatar.Image
								src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=face"
								alt="Profile"
							/>
							<Avatar.Fallback class="text-lg">
								{userState.user?.username?.[0]?.toUpperCase() || 'U'}
							</Avatar.Fallback>
						</Avatar.Root>
						{#if isEditing}
							<Button
								size="sm"
								variant="outline"
								class="absolute -right-2 -bottom-2 h-8 w-8 rounded-full p-0"
							>
								<Camera class="h-4 w-4" />
							</Button>
						{/if}
					</div>

					<h2 class="mb-1 text-xl font-semibold">
						{userState.user?.username || 'Username'}
					</h2>
					<p class="text-muted-foreground mb-4 text-sm">
						{editedProfile.email || 'email@example.com'}
					</p>

					<Badge variant="secondary" class="mb-4">
						<Shield class="mr-1 h-3 w-3" />
						Active User
					</Badge>

					<div class="text-muted-foreground flex items-center justify-center gap-1 text-xs">
						<Calendar class="h-3 w-3" />
						<span>Joined {formatDate(new Date())}</span>
					</div>
				</Card.Content>
			</Card.Root>

			<!-- Quick Stats -->
			<Card.Root class="mt-4">
				<Card.Header>
					<Card.Title class="text-sm">Quick Stats</Card.Title>
				</Card.Header>
				<Card.Content class="space-y-3">
					<div class="flex justify-between text-sm">
						<span class="text-muted-foreground">Projects Created</span>
						<span class="font-medium">12</span>
					</div>
					<div class="flex justify-between text-sm">
						<span class="text-muted-foreground">Public Projects</span>
						<span class="font-medium">8</span>
					</div>
					<div class="flex justify-between text-sm">
						<span class="text-muted-foreground">Private Projects</span>
						<span class="font-medium">4</span>
					</div>
				</Card.Content>
			</Card.Root>
		</div>

		<!-- Main Content -->
		<div class="space-y-6 lg:col-span-2">
			<!-- Personal Information -->
			<Card.Root>
				<Card.Header class="flex flex-row items-center justify-between">
					<div>
						<Card.Title>Personal Information</Card.Title>
						<Card.Description>Update your personal details</Card.Description>
					</div>
					{#if isEditing}
						<div class="flex gap-2">
							<Button size="sm" onclick={handleSave}>
								<Save class="mr-2 h-4 w-4" />
								Save
							</Button>
							<Button size="sm" variant="outline" onclick={handleCancel}>
								<X class="mr-2 h-4 w-4" />
								Cancel
							</Button>
						</div>
					{/if}
				</Card.Header>
				<Card.Content class="space-y-4">
					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div class="space-y-2">
							<Label for="username">Username</Label>
							{#if isEditing}
								<Input
									id="username"
									bind:value={editedProfile.username}
									placeholder="Enter username"
								/>
							{:else}
								<div class="bg-muted flex items-center gap-2 rounded-md p-2">
									<User class="text-muted-foreground h-4 w-4" />
									<span>{userState.user?.username || 'Not set'}</span>
								</div>
							{/if}
						</div>

						<div class="space-y-2">
							<Label for="email">Email</Label>
							{#if isEditing}
								<Input
									id="email"
									type="email"
									bind:value={editedProfile.email}
									placeholder="Enter email"
								/>
							{:else}
								<div class="bg-muted flex items-center gap-2 rounded-md p-2">
									<Mail class="text-muted-foreground h-4 w-4" />
									<span>{editedProfile.email || 'Not set'}</span>
								</div>
							{/if}
						</div>
					</div>

					<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
						<div class="space-y-2">
							<Label for="location">Location</Label>
							{#if isEditing}
								<Input
									id="location"
									bind:value={editedProfile.location}
									placeholder="Enter location"
								/>
							{:else}
								<div class="bg-muted rounded-md p-2">
									<span class="text-muted-foreground">{editedProfile.location || 'Not set'}</span>
								</div>
							{/if}
						</div>

						<div class="space-y-2">
							<Label for="website">Website</Label>
							{#if isEditing}
								<Input
									id="website"
									bind:value={editedProfile.website}
									placeholder="https://example.com"
								/>
							{:else}
								<div class="bg-muted rounded-md p-2">
									<span class="text-muted-foreground">{editedProfile.website || 'Not set'}</span>
								</div>
							{/if}
						</div>
					</div>

					<div class="space-y-2">
						<Label for="bio">Bio</Label>
						{#if isEditing}
							<Textarea
								id="bio"
								bind:value={editedProfile.bio}
								placeholder="Tell us about yourself..."
								class="min-h-[100px]"
							/>
						{:else}
							<div class="bg-muted min-h-[100px] rounded-md p-2">
								<span class="text-muted-foreground">
									{editedProfile.bio || 'No bio available.'}
								</span>
							</div>
						{/if}
					</div>
				</Card.Content>
			</Card.Root>

			<!-- Account Settings -->
			<Card.Root>
				<Card.Header>
					<Card.Title>Account Settings</Card.Title>
					<Card.Description>Manage your account preferences</Card.Description>
				</Card.Header>
				<Card.Content class="space-y-4">
					<div class="flex items-center justify-between">
						<div class="space-y-1">
							<Label class="flex items-center gap-2">
								<Key class="h-4 w-4" />
								Change Password
							</Label>
							<p class="text-muted-foreground text-sm">Update your account password</p>
						</div>
						<Button variant="outline" size="sm">Change</Button>
					</div>

					<Separator />

					<div class="flex items-center justify-between">
						<div class="space-y-1">
							<Label class="flex items-center gap-2">
								<Bell class="h-4 w-4" />
								Email Notifications
							</Label>
							<p class="text-muted-foreground text-sm">Receive notifications about your projects</p>
						</div>
						<input type="checkbox" checked class="rounded" />
					</div>

					<Separator />

					<div class="flex items-center justify-between">
						<div class="space-y-1">
							<Label class="text-destructive flex items-center gap-2">
								<Settings class="h-4 w-4" />
								Delete Account
							</Label>
							<p class="text-muted-foreground text-sm">
								Permanently delete your account and all data
							</p>
						</div>
						<Button variant="destructive" size="sm">Delete</Button>
					</div>
				</Card.Content>
			</Card.Root>
		</div>
	</div>
</div>
