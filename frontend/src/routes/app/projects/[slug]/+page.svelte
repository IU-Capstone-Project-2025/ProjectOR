<script lang="ts">
	import { createQuery, createMutation, useQueryClient } from '@tanstack/svelte-query';
	import * as Card from '$lib/components/ui/card';
	import * as Tabs from '$lib/components/ui/tabs';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import {
		getProjectById,
		updateProject,
		generateTags,
		addProjectTags,
		removeProjectTags,
		applyToProject,
		getUserById,
		enhanceProjectDescription
	} from '../(components)/dataLoaders';
	import { goto } from '$app/navigation';
	import {
		ArrowLeft,
		Globe,
		Calendar,
		User,
		Edit3,
		Share2,
		Bookmark,
		Github,
		Send,
		MailPlus,
		X,
		Code,
		Save,
		LoaderCircle,
		FileText,
		OctagonX,
		WandSparkles,
		Users
	} from '@lucide/svelte';
	import Markdown from '$lib/components/md/Markdown.svelte';
	import { toast } from 'svelte-sonner';
	import { TagsInput } from '$lib/components/ui/tags-input';
	import type { components } from '@/api/v1';
	import RainbowButton from '@/components/RainbowButton.svelte';
	import { Skeleton } from '@/components/ui/skeleton';
	import ProjectContributors from '../(components)/ProjectContributors.svelte';

	let { data } = $props();
	let isEditing = $state(false);
	let {
		editDescription,
		editBriefDescription
	}: {
		editDescription: string;
		editBriefDescription: string;
	} = $state({
		editDescription: '',
		editBriefDescription: ''
	});
	let editTags: string[] = $state([]);
	let showContributorsDialog = $state(false);

	const queryClient = useQueryClient();

	const projectId = data.projectId;

	const projectQuery = createQuery({
		queryKey: ['project', projectId],
		queryFn: async () => await getProjectById(projectId)
	});

	function goBack() {
		goto('/app/explore');
	}

	function formatDate(dateString?: string) {
		if (!dateString) return 'Recently';
		try {
			return new Date(dateString).toLocaleDateString();
		} catch {
			return 'Recently';
		}
	}

	const handleSave = (project: components['schemas']['ProjectSchema']) => {
		if (!editBriefDescription || !editDescription) {
			toast.error('Please fill in all fields before saving.');
			return;
		}
		if (
			editBriefDescription === project.brief_description &&
			editDescription === project.description &&
			JSON.stringify(editTags) === JSON.stringify(project.tags?.map((tag) => tag.name) || [])
		) {
			isEditing = false;
			return;
		}
		$updateProjectMutation.mutate();
		let tagsToAdd = editTags.filter((tag) => !project.tags?.some((t) => t.name === tag));
		let tagsToRemove =
			project.tags?.filter((t) => !editTags.includes(t.name)).map((t) => t.name) || [];
		if (tagsToAdd.length > 0) {
			$addProjectTagsMutation.mutate({ projectId, tags: tagsToAdd });
		}
		if (tagsToRemove.length > 0) {
			$removeProjectTagsMutation.mutate({ projectId, tags: tagsToRemove });
		}
	};

	const updateProjectMutation = createMutation({
		mutationFn: async () => await updateProject(projectId, editBriefDescription, editDescription),
		onSuccess: () => {
			queryClient.invalidateQueries({ queryKey: ['project', projectId] });
			isEditing = false;
			toast.success('Project updated successfully');
		},
		onError: (error) => {
			console.error('Error updating project:', error);
			toast.error(`Failed to update project: ${error.message}`);
		}
	});

	const generateTagsMutation = createMutation({
		mutationFn: async (projectId: number) => await generateTags(projectId),
		onSuccess: (data) => {
			for (const tag of data.tags) {
				if (!editTags.includes(tag)) {
					editTags.push(tag);
				}
			}
			toast.success('Tags generated successfully');
		},
		onError: (error) => {
			console.error('Error generating tags:', error);
			toast.error(`Failed to generate tags: ${error.message}`);
		}
	});

	const addProjectTagsMutation = createMutation({
		mutationFn: async ({ projectId, tags }: { projectId: number; tags: string[] }) =>
			await addProjectTags(projectId, tags),
		onSuccess: () => {
			queryClient.invalidateQueries({ queryKey: ['project', projectId] });
			toast.success('Tags added successfully');
		},
		onError: (error) => {
			console.error('Error adding tags:', error);
			toast.error(`Failed to add tags: ${error.message}`);
		}
	});

	const removeProjectTagsMutation = createMutation({
		mutationFn: async ({ projectId, tags }: { projectId: number; tags: string[] }) =>
			await removeProjectTags(projectId, tags),
		onSuccess: () => {
			queryClient.invalidateQueries({ queryKey: ['project', projectId] });
			toast.success('Tags removed successfully');
		},
		onError: (error) => {
			console.error('Error removing tags:', error);
			toast.error(`Failed to remove tags: ${error.message}`);
		}
	});

	const applyToProjectMutation = createMutation({
		mutationFn: async (projectId: number) => await applyToProject(projectId),
		onSuccess: () => {
			toast.success('Application submitted successfully');
		},
		onError: (error) => {
			console.error('Error applying to project:', error);
			toast.error(`Failed to apply to project: ${error.message}`);
		}
	});

	const projectOwnerQuery = createQuery({
		queryKey: ['projectOwner', data.projectId],
		queryFn: async () => {
			if (!$projectQuery.data?.ceo_id) return null;
			return await getUserById($projectQuery.data.ceo_id);
		},
		enabled: !!$projectQuery.data?.ceo_id
	});

	const enhanceDescriptionMutation = createMutation({
		mutationFn: async (description: string) => await enhanceProjectDescription(description),
		onSuccess: (data) => {
			editDescription = data.enhanced_description;
			toast.success('✨ Description enhanced successfully');
		},
		onError: (error) => {
			console.error('Error enhancing description:', error);
			toast.error(`Failed to enhance description: ${error.message}`);
		}
	});
</script>

<div class="container mx-auto max-w-6xl space-y-6 px-4 py-6">
	<!-- Back Navigation -->
	<div class="flex items-center gap-4">
		<Button variant="outline" size="sm" onclick={goBack}>
			<ArrowLeft class="mr-2 h-4 w-4" />
			Back to Explore
		</Button>
	</div>

	{#if $projectQuery.isPending}
		<div class="flex justify-center py-12">
			<div class="text-muted-foreground">Loading project details...</div>
		</div>
	{:else if $projectQuery.isError}
		<div class="flex justify-center py-12">
			<ErrorAlert text={$projectQuery.error.message} />
		</div>
	{:else}
		{@const project = $projectQuery.data}

		<!-- Project Header -->
		<div class="flex flex-col gap-6 lg:flex-row">
			<!-- Main Content -->
			<div class="flex-1 space-y-6">
				<Card.Root>
					<Card.Header class="space-y-4">
						<div class="flex items-start justify-between">
							<div class="space-y-2">
								<div class="flex items-center gap-3">
									<h1 class="text-3xl font-bold tracking-tight">{project.title}</h1>
									<div class="flex flex-row gap-2">
										<Badge
											variant={project.is_dead ? 'secondary' : 'outline'}
											class="ml-2 shrink-0"
										>
											{#if project.is_dead}
												<OctagonX />
												Graveyard
											{:else}
												<Globe class="mr-1 h-3 w-3" />
												Public
											{/if}
										</Badge>
										{#if project.is_opensource}
											<Badge variant="outline" class="shrink-0">
												<Code class="mr-1 h-3 w-3" />
												Open Source
											</Badge>
										{/if}
									</div>
								</div>
							</div>
							<div class="flex items-center gap-2">
								{#if !isEditing}
									<Button size="sm">
										<Bookmark class="mr-2 h-4 w-4" />
										Bookmark
									</Button>
									<Button
										size="sm"
										variant="outline"
										onclick={() => {
											navigator
												.share({
													title: project.title,
													text: project.brief_description || 'Check out this project!',
													url: window.location.href
												})
												.catch((err) => console.error('Error sharing:', err));
										}}
									>
										<Share2 class="mr-2 h-4 w-4" />
										Share
									</Button>
								{/if}
								{#if project.ceo_id === data.user?.id}
									<Button
										size="sm"
										variant="outline"
										onclick={() => {
											editDescription = project.description || '';
											editBriefDescription = project.brief_description || '';
											editTags = project.tags?.map((tag) => tag.name) || [];
											isEditing = !isEditing;
										}}
									>
										{#if isEditing}
											<X class="mr-2 h-4 w-4" />
											Cancel
										{:else}
											<Edit3 class="mr-2 h-4 w-4" />
											Edit
										{/if}
									</Button>
									{#if isEditing}
										<Button
											size="sm"
											variant="default"
											onclick={() => handleSave(project)}
											disabled={$updateProjectMutation.isPending ||
												$addProjectTagsMutation.isPending ||
												$removeProjectTagsMutation.isPending}
										>
											{#if $updateProjectMutation.isPending || $addProjectTagsMutation.isPending || $removeProjectTagsMutation.isPending}
												<LoaderCircle class="animate-spin" />
												Saving...
											{:else}
												<Save class="mr-2 h-4 w-4" />
												Save Changes
											{/if}
										</Button>
									{/if}
								{/if}
							</div>
						</div>
						<div class="flex w-full flex-row flex-wrap gap-2">
							{#if !isEditing}
								{#each project.tags ?? [] as tag (tag.name)}
									<Badge variant="default" class="shrink-0">
										{tag.name}
									</Badge>
								{/each}
							{:else}
								<TagsInput bind:value={editTags} placeholder="Add a tag" />
								<RainbowButton
									onclick={() => $generateTagsMutation.mutate(project.id)}
									disabled={$generateTagsMutation.isPending}
									class="h-8"
								>
									{#if $generateTagsMutation.isPending}
										<LoaderCircle class="animate-spin" />
										Generating...
									{:else}
										<WandSparkles class="size-4" />
										Generate
									{/if}
								</RainbowButton>
							{/if}
						</div>

						<Separator />

						<!-- Project Meta -->
						<div class="text-muted-foreground flex items-center gap-6 text-sm">
							<div class="flex items-center gap-1">
								<User class="h-4 w-4" />
								{#if !$projectOwnerQuery.data}
									<Skeleton class="h-4 w-24" />
								{:else}
									<span>{$projectOwnerQuery.data.username}</span>
								{/if}
							</div>
							<div class="flex items-center gap-1">
								<Calendar class="h-4 w-4" />
								<span>Created {formatDate(project.created_at)}</span>
							</div>
							<div class="flex items-center gap-1">
								<Calendar class="h-4 w-4" />
								<span>Last updated {formatDate()}</span>
							</div>
						</div>
					</Card.Header>

					<Card.Content>
						<div class="space-y-6">
							<!-- Description -->
							<div>
								<h2 class="mb-3 text-lg font-semibold">About this project</h2>
								{#if isEditing}
									<Input
										bind:value={editBriefDescription}
										placeholder="Enter a brief description of the project"
										class="mb-2"
									/>
								{:else}
									<p class="text-muted-foreground leading-relaxed">
										{project.brief_description || 'No description provided for this project.'}
									</p>
								{/if}
							</div>

							<Separator />

							<!-- Project Stats -->
							<div>
								<h2 class="mb-4 text-lg font-semibold">Project Statistics</h2>
								<div class="grid grid-cols-2 gap-4 md:grid-cols-4">
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">15</div>
										<div class="text-muted-foreground text-sm">Team Size</div>
									</div>
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">3</div>
										<div class="text-muted-foreground text-sm">Contributors</div>
									</div>
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">$42.000</div>
										<div class="text-muted-foreground text-sm">Raised</div>
									</div>
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">2025</div>
										<div class="text-muted-foreground text-sm">Founded</div>
									</div>
								</div>
							</div>
						</div>
					</Card.Content>
				</Card.Root>

				<!-- Project Markdown Description -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="flex items-center gap-2">
							<FileText class="h-5 w-5" />
							Detailed Information
						</Card.Title>
					</Card.Header>
					<Card.Content>
						{#if isEditing}
							<RainbowButton
								onclick={() => $enhanceDescriptionMutation.mutate(editDescription)}
								disabled={$enhanceDescriptionMutation.isPending || !editDescription}
								class="mb-4 h-8"
							>
								{#if $enhanceDescriptionMutation.isPending}
									<LoaderCircle class="animate-spin" />
									Generating...
								{:else}
									<WandSparkles class="size-4" />
									Enhance Description
								{/if}
							</RainbowButton>
							<Tabs.Root value="edit" class="w-full">
								<Tabs.List>
									<Tabs.Trigger value="edit">Edit</Tabs.Trigger>
									<Tabs.Trigger value="preview">Preview</Tabs.Trigger>
								</Tabs.List>
								<Tabs.Content value="edit">
									<Textarea
										bind:value={editDescription}
										placeholder="Enter detailed project description"
										class="h-64"
										disabled={$enhanceDescriptionMutation.isPending}
									/>
								</Tabs.Content>
								<Tabs.Content value="preview">
									<Markdown content={editDescription} />
								</Tabs.Content>
							</Tabs.Root>
						{:else}
							<Markdown content={project.description ?? 'No information provided'} />
						{/if}
					</Card.Content>
				</Card.Root>
			</div>

			<!-- Sidebar -->
			<div class="space-y-6 lg:w-80">
				<!-- Quick Actions -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Social Links</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-2">
						<Button
							variant="outline"
							size="sm"
							class="w-full justify-start"
							href="https://google.com"
							target="_blank"
						>
							<Globe class="mr-2 h-4 w-4" />
							Website
						</Button>
						<Button
							variant="outline"
							size="sm"
							class="w-full justify-start"
							href="https://t.me"
							target="_blank"
						>
							<Send class="mr-2 h-4 w-4" />
							Telegram
						</Button>
						<Button
							variant="outline"
							size="sm"
							class="w-full justify-start"
							href="https://github.com"
							target="_blank"
						>
							<Github class="mr-2 h-4 w-4" />
							GitHub
						</Button>
					</Card.Content>
				</Card.Root>
				<!-- Contributors -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Contributors</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-3">
						<div class="flex items-center gap-3">
							{#if !$projectOwnerQuery.data}
								<Skeleton class="h-8 w-24" />
							{:else}
								<div
									class="bg-primary text-primary-foreground flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium"
								>
									{$projectOwnerQuery.data.username.slice(0, 1).toUpperCase()}
								</div>
								<div class="min-w-0 flex-1">
									<div class="text-sm font-medium">{$projectOwnerQuery.data.username}</div>
									<div class="text-muted-foreground text-xs">Owner</div>
								</div>
							{/if}
						</div>
						<div class="flex items-center gap-3">
							<div
								class="bg-primary text-primary-foreground flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium"
							>
								C
							</div>
							<div class="min-w-0 flex-1">
								<div class="text-sm font-medium">Jane Smith</div>
								<div class="text-muted-foreground text-xs">Co-Founder</div>
							</div>
						</div>
						<div class="flex items-center gap-3">
							<div
								class="bg-primary text-primary-foreground flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium"
							>
								D
							</div>
							<div class="min-w-0 flex-1">
								<div class="text-sm font-medium">David Johnson</div>
								<div class="text-muted-foreground text-xs">Developer</div>
							</div>
						</div>
						<Card.Footer class="pt-2">
							{#if project.ceo_id === data.user?.id}
								<Button
									variant="default"
									size="sm"
									class="w-full justify-center"
									onclick={() => (showContributorsDialog = true)}
								>
									<Users class="mr-2 h-4 w-4" />
									Manage Applications
								</Button>
							{:else}
								<Button
									variant="default"
									size="sm"
									class="w-full justify-center"
									onclick={() => $applyToProjectMutation.mutate(project.id)}
								>
									<MailPlus />
									Apply to Contribute
								</Button>
							{/if}
						</Card.Footer>
					</Card.Content>
				</Card.Root>

				<!-- Recent Activity -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Recent Activity</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-3">
						<div class="text-sm">
							<div class="font-medium">Description updated</div>
							<div class="text-muted-foreground text-xs">1 hours ago</div>
						</div>
						<div class="text-sm">
							<div class="font-medium">New contributor applied</div>
							<div class="text-muted-foreground text-xs">2 day ago</div>
						</div>
						<div class="text-sm">
							<div class="font-medium">Project created</div>
							<div class="text-muted-foreground text-xs">3 days ago</div>
						</div>
					</Card.Content>
				</Card.Root>
			</div>
		</div>

		<!-- Contributors Dialog -->
		{#if showContributorsDialog}
			<ProjectContributors {projectId} bind:open={showContributorsDialog} />
		{/if}
	{/if}
</div>
