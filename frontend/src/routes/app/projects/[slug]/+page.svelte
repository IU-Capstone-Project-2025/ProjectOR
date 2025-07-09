<script lang="ts">
	import { createQuery } from '@tanstack/svelte-query';
	import * as Card from '$lib/components/ui/card';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import { getProjectById } from '../(components)/dataLoaders';
	import { goto } from '$app/navigation';
	import {
		ArrowLeft,
		Globe,
		Lock,
		Calendar,
		User,
		Edit3,
		Share2,
		Bookmark,
		GitBranch,
		Code,
		FileText
	} from '@lucide/svelte';

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
									<Badge variant={project.is_public ? 'secondary' : 'outline'}>
										{#if project.is_public}
											<Globe class="mr-1 h-3 w-3" />
											Public
										{:else}
											<Lock class="mr-1 h-3 w-3" />
											Private
										{/if}
									</Badge>
								</div>
								<p class="text-muted-foreground">Project ID: #{project.id}</p>
							</div>
							<div class="flex items-center gap-2">
								<Button size="sm">
									<Bookmark class="mr-2 h-4 w-4" />
									Bookmark
								</Button>
								<Button size="sm" variant="outline">
									<Share2 class="mr-2 h-4 w-4" />
									Share
								</Button>
								<Button size="sm" variant="outline">
									<Edit3 class="mr-2 h-4 w-4" />
									Edit
								</Button>
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
								<h2 class="mb-3 text-lg font-semibold">About this project</h2>
								<p class="text-muted-foreground leading-relaxed">
									{project.description || 'No description provided for this project.'}
								</p>
							</div>

							<Separator />

							<!-- Project Stats -->
							<div>
								<h2 class="mb-4 text-lg font-semibold">Project Statistics</h2>
								<div class="grid grid-cols-2 gap-4 md:grid-cols-4">
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">15</div>
										<div class="text-muted-foreground text-sm">Files</div>
									</div>
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">3</div>
										<div class="text-muted-foreground text-sm">Contributors</div>
									</div>
									<div class="bg-muted rounded-lg p-4 text-center">
										<div class="text-2xl font-bold">42</div>
										<div class="text-muted-foreground text-sm">Commits</div>
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
							<div
								class="bg-muted hover:bg-muted/80 flex cursor-pointer items-center gap-3 rounded-lg p-3 transition-colors"
							>
								<Code class="text-muted-foreground h-4 w-4" />
								<span class="font-medium">src/</span>
								<span class="text-muted-foreground ml-auto text-sm">Source code</span>
							</div>
							<div
								class="bg-muted hover:bg-muted/80 flex cursor-pointer items-center gap-3 rounded-lg p-3 transition-colors"
							>
								<FileText class="text-muted-foreground h-4 w-4" />
								<span class="font-medium">README.md</span>
								<span class="text-muted-foreground ml-auto text-sm">Project documentation</span>
							</div>
							<div
								class="bg-muted hover:bg-muted/80 flex cursor-pointer items-center gap-3 rounded-lg p-3 transition-colors"
							>
								<Code class="text-muted-foreground h-4 w-4" />
								<span class="font-medium">package.json</span>
								<span class="text-muted-foreground ml-auto text-sm">Dependencies</span>
							</div>
						</div>
					</Card.Content>
				</Card.Root>
			</div>

			<!-- Sidebar -->
			<div class="space-y-6 lg:w-80">
				<!-- Quick Actions -->
				<Card.Root>
					<Card.Header>
						<Card.Title class="text-sm">Quick Actions</Card.Title>
					</Card.Header>
					<Card.Content class="space-y-2">
						<Button variant="outline" size="sm" class="w-full justify-start">
							<GitBranch class="mr-2 h-4 w-4" />
							Create Branch
						</Button>
						<Button variant="outline" size="sm" class="w-full justify-start">
							<Code class="mr-2 h-4 w-4" />
							Clone Repository
						</Button>
						<Button variant="outline" size="sm" class="w-full justify-start">
							<FileText class="mr-2 h-4 w-4" />
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
							<div
								class="bg-primary text-primary-foreground flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium"
							>
								U
							</div>
							<div class="min-w-0 flex-1">
								<div class="text-sm font-medium">Project Owner</div>
								<div class="text-muted-foreground text-xs">Owner</div>
							</div>
						</div>
					</Card.Content>
				</Card.Root>
			</div>
		</div>
	{/if}
</div>
