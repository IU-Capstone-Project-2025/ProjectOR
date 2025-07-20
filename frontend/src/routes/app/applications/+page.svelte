<script lang="ts">
	import { getApplications, getProjectById } from './(components)/dataLoaders';
	import { createQuery } from '@tanstack/svelte-query';
	import * as Card from '$lib/components/ui/card';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import {
		LoaderCircle,
		Clock,
		CheckCircle2,
		XCircle,
		Calendar,
		ArrowRight,
		Building
	} from '@lucide/svelte';
	import { goto } from '$app/navigation';

	// Query to fetch user applications
	const applicationsQuery = createQuery({
		queryKey: ['userApplications'],
		queryFn: () => getApplications()
	});

	// Format date helper
	function formatDate(dateString?: string) {
		if (!dateString) return 'Recently';
		try {
			return new Date(dateString).toLocaleDateString('en-US', {
				year: 'numeric',
				month: 'short',
				day: 'numeric'
			});
		} catch {
			return 'Recently';
		}
	}

	// Get status badge variant
	function getStatusVariant(isApproved: boolean | null) {
		if (isApproved === null) return 'outline';
		return isApproved ? 'default' : 'destructive';
	}

	// Get status text
	function getStatusText(isApproved: boolean | null) {
		if (isApproved === null) return 'Pending';
		return isApproved ? 'Approved' : 'Declined';
	}

	// Get status icon
	function getStatusIcon(isApproved: boolean | null) {
		if (isApproved === null) return Clock;
		return isApproved ? CheckCircle2 : XCircle;
	}
</script>

<div class="container mx-auto max-w-5xl space-y-6 px-4 py-6">
	<div class="flex flex-col gap-2">
		<h1 class="text-3xl font-bold tracking-tight">My Applications</h1>
		<p class="text-muted-foreground">
			Review all the projects you've applied to and their current status
		</p>
	</div>

	<Separator />

	<div class="space-y-6">
		{#if $applicationsQuery.isPending}
			<div class="flex justify-center py-12">
				<LoaderCircle class="h-8 w-8 animate-spin" />
			</div>
		{:else if $applicationsQuery.isError}
			<div class="flex justify-center py-8">
				<ErrorAlert text={$applicationsQuery.error.message} />
			</div>
		{:else if $applicationsQuery.data.length === 0}
			<div class="flex flex-col items-center justify-center py-16 text-center">
				<div class="bg-muted mb-4 rounded-full p-6">
					<Building class="text-muted-foreground h-10 w-10" />
				</div>
				<h3 class="mb-2 text-2xl font-semibold">No applications yet</h3>
				<p class="text-muted-foreground mb-6 max-w-md">
					You haven't applied to any projects yet. Explore projects and start contributing!
				</p>
				<Button onclick={() => goto('/app/explore')}>Explore Projects</Button>
			</div>
		{:else}
			<div class="grid gap-4 md:grid-cols-2">
				{#each $applicationsQuery.data as application (application)}
					{#await getProjectById(application.project_id)}
						<div class="bg-muted h-40 w-full animate-pulse rounded"></div>
					{:then project}
						<Card.Root>
							<Card.Header>
								<div class="flex items-start justify-between">
									<div>
										<Card.Title>{project.title}</Card.Title>
										<Card.Description class="mt-1">
											<div class="flex items-center gap-2">
												<Calendar class="h-3 w-3" />
												<span>Applied on {formatDate(application.created_at)}</span>
											</div>
										</Card.Description>
									</div>
									<Badge
										variant={getStatusVariant(application.is_approved)}
										class="flex items-center gap-1"
									>
										<svelte:component
											this={getStatusIcon(application.is_approved)}
											class="h-3 w-3"
										/>
										{getStatusText(application.is_approved)}
									</Badge>
								</div>
							</Card.Header>
							<Card.Content class="space-y-3">
								{#if application.feedback}
									<div class="mt-2">
										<p class="text-muted-foreground mb-1 text-xs font-medium">
											Feedback from project owner:
										</p>
										<div class="bg-muted rounded p-2 text-sm">
											{application.feedback}
										</div>
									</div>
								{/if}
							</Card.Content>
							<Card.Footer>
								<div class="flex w-full justify-end">
									<Button
										variant="outline"
										size="sm"
										class="w-full sm:w-auto"
										onclick={() => goto(`/app/projects/${application.project_id}`)}
									>
										View Project
										<ArrowRight class="ml-2 h-4 w-4" />
									</Button>
								</div>
							</Card.Footer>
						</Card.Root>
					{:catch error}
						<div class="text-destructive">Failed to load project: {error.message}</div>
					{/await}
				{/each}
			</div>
		{/if}
	</div>
</div>
