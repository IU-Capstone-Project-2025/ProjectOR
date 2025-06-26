<script lang="ts">
	import { type components } from '@/api/v1';
	import { createQuery } from '@tanstack/svelte-query';
	import * as Card from '$lib/components/ui/card';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import { getProjectById } from '../(components)/dataLoaders';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { 
		ArrowLeft, 
		Globe, 
		Lock, 
		Calendar, 
		User, 
		Edit3, 
		Trash2,
		Share2,
		Bookmark,
		GitBranch,
		Code,
		FileText
	} from '@lucide/svelte';

	type Project = components['schemas']['ProjectSchema'] & { id: number };

	let { data } = $props();
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
</script>

<div class="container mx-auto px-4 py-6 max-w-6xl space-y-6">
	<!-- Back Navigation -->
	<div class="flex items-center gap-4">
		<Button variant="outline" size="sm" onclick={goBack}>
			<ArrowLeft class="h-4 w-4 mr-2" />
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
		<div class="flex flex-col lg:flex-row gap-6">
			<!-- Main Content -->
			<div class="flex-1 space-y-6">
				<Card.Root>
					<Card.Header class="space-y-4">
						<div class="flex items-start justify-between">
							<div class="space-y-2">
								<div class="flex items-center gap-3">
									<h1 class="text-3xl font-bold tracking-tight">{project.title}</h1>
									<Badge variant={project.is_public ? 'secondary' : 'outline'}>
										{#if project.is_public}
											<Globe class="h-3 w-3 mr-1" />
											Public
										{:else}
											<Lock class="h-3 w-3 mr-1" />
											Private
										{/if}
									</Badge>
								</div>
								<p class="text-muted-foreground">Project ID: #{project.id}</p>
							</div>
							<div class="flex items-center gap-2">
								<Button size="sm">
									<Bookmark class="h-4 w-4 mr-2" />
									Bookmark
								</Button>
								<Button size="sm" variant="outline">
									<Share2 class="h-4 w-4 mr-2" />
									Share
								</Button>
								<Button size="sm" variant="outline">
									<Edit3 class="h-4 w-4 mr-2" />
									Edit
								</Button>
							</div>
						</div>

						<Separator />

						<!-- Project Meta -->
						<div class="flex items-center gap-6 text-sm text-muted-foreground">
							<div class="flex items-center gap-1">
								<User class="h-4 w-4" />
								<span>Project Owner</span>
							</div>
							<div class="flex items-center gap-1">
								<Calendar class="h-4 w-4" />
								<span>Created {formatDate()}</span>
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
								<h2 class="text-lg font-semibold mb-3">About this project</h2>
								<p class="text-muted-foreground leading-relaxed">
									{project.description || 'No description provided for this project.'}
								</p>
							</div>

							<Separator />

							<!-- Project Stats -->
							<div>
								<h2 class="text-lg font-semibold mb-4">Project Statistics</h2>
								<div class="grid grid-cols-2 md:grid-cols-4 gap-4">
									<div class="text-center p-4 bg-muted rounded-lg">
										<div class="text-2xl font-bold">15</div>
										<div class="text-sm text-muted-foreground">Files</div>
									</div>
									<div class="text-center p-4 bg-muted rounded-lg">
										<div class="text-2xl font-bold">3</div>
										<div class="text-sm text-muted-foreground">Contributors</div>
									</div>
									<div class="text-center p-4 bg-muted rounded-lg">
										<div class="text-2xl font-bold">42</div>
										<div class="text-sm text-muted-foreground">Commits</div>
									</div>
									<div class="text-center p-4 bg-muted rounded-lg">
										<div class="text-2xl font-bold">7</div>
										<div class="text-sm text-muted-foreground">Branches</div>
									</div>
								</div>
							</div>
						</div>
					</Card.Content>
				</Card.Root>

				<!-- Project Files/Content -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="flex items-center gap-2">
							<FileText class="h-5 w-5" />
							Project Files
						</Card.Title>
					</Card.Header>
					<Card.Content>
						<div class="space-y-2">
							<div class="flex items-center gap-3 p-3 bg-muted rounded-lg hover:bg-muted/80 transition-colors cursor-pointer">
								<Code class="h-4 w-4 text-muted-foreground" />
								<span class="font-medium">src/</span>
								<span class="text-sm text-muted-foreground ml-auto">Source code</span>
							</div>
							<div class="flex items-center gap-3 p-3 bg-muted rounded-lg hover:bg-muted/80 transition-colors cursor-pointer">
								<FileText class="h-4 w-4 text-muted-foreground" />
								<span class="font-medium">README.md</span>
								<span class="text-sm text-muted-foreground ml-auto">Project documentation</span>
							</div>
							<div class="flex items-center gap-3 p-3 bg-muted rounded-lg hover:bg-muted/80 transition-colors cursor-pointer">
								<Code class="h-4 w-4 text-muted-foreground" />
								<span class="font-medium">package.json</span>
								<span class="text-sm text-muted-foreground ml-auto">Dependencies</span>
							</div>
						</div>
					</Card.Content>
				</Card.Root>
			</div>

			<!-- Sidebar -->
			<div class="lg:w-80 space-y-6">
				<!-- Quick Actions -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Quick Actions</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-2">
						<Button variant="outline" size="sm" class="w-full justify-start">
							<GitBranch class="h-4 w-4 mr-2" />
							Create Branch
						</Button>
						<Button variant="outline" size="sm" class="w-full justify-start">
							<Code class="h-4 w-4 mr-2" />
							Clone Repository
						</Button>
						<Button variant="outline" size="sm" class="w-full justify-start">
							<FileText class="h-4 w-4 mr-2" />
							Download ZIP
						</Button>
					</Card.Content>
				</Card.Root>

				<!-- Recent Activity -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Recent Activity</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-3">
						<div class="text-sm">
							<div class="font-medium">Initial commit</div>
							<div class="text-muted-foreground text-xs">2 hours ago</div>
						</div>
						<div class="text-sm">
							<div class="font-medium">Added README</div>
							<div class="text-muted-foreground text-xs">1 day ago</div>
						</div>
						<div class="text-sm">
							<div class="font-medium">Project created</div>
							<div class="text-muted-foreground text-xs">3 days ago</div>
						</div>
					</Card.Content>
				</Card.Root>

				<!-- Contributors -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Contributors</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-3">
						<div class="flex items-center gap-3">
							<div class="h-8 w-8 bg-primary rounded-full flex items-center justify-center text-primary-foreground text-sm font-medium">
								U
							</div>
							<div class="flex-1 min-w-0">
								<div class="font-medium text-sm">Project Owner</div>
								<div class="text-muted-foreground text-xs">Owner</div>
							</div>
						</div>
					</Card.Content>
				</Card.Root>
			</div>
		</div>
	{/if}
</div>
