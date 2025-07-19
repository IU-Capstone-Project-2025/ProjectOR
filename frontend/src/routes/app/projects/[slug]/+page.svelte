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
	import { getProjectById, updateProject } from '../(components)/dataLoaders';
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
		OctagonX
	} from '@lucide/svelte';
	import Markdown from '$lib/components/md/Markdown.svelte';
	import { toast } from 'svelte-sonner';

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
								<p class="text-muted-foreground">Project ID: #{project.id}</p>
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
											onclick={() => $updateProjectMutation.mutate()}
										>
											{#if $updateProjectMutation.isPending}
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

						<Separator />

						<!-- Project Meta -->
						<div class="text-muted-foreground flex items-center gap-6 text-sm">
							<div class="flex items-center gap-1">
								<User class="h-4 w-4" />
								<span>Project Owner</span>
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
										<div class="text-2xl font-bold">7</div>
										<div class="text-muted-foreground text-sm">Branches</div>
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
							<div
								class="bg-primary text-primary-foreground flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium"
							>
								U
							</div>
							<div class="min-w-0 flex-1">
								<div class="text-sm font-medium">John Doe</div>
								<div class="text-muted-foreground text-xs">Owner</div>
							</div>
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
							<Button variant="default" size="sm" class="w-full justify-center">
								<MailPlus />
								Apply to Contribute
							</Button>
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
	{/if}
</div>
