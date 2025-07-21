<script lang="ts">
	import * as Dialog from '$lib/components/ui/dialog';
	import { createQuery, createMutation, useQueryClient } from '@tanstack/svelte-query';
	import { Button } from '$lib/components/ui/button';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	import { getProjectApplications, approveApplication, getUserById } from './dataLoaders';
	import { toast } from 'svelte-sonner';
	import { LoaderCircle, UserCheck, UserX, MessageSquare } from '@lucide/svelte';
	import { Badge } from '$lib/components/ui/badge';
	import ErrorAlert from '$lib/components/ErrorAlert.svelte';
	import type { components } from '$lib/api/v1';

	// Props
	let { open = $bindable(false), projectId } = $props<{ open: boolean; projectId: number }>();

	// State variables
	let selectedApplication = $state<components['schemas']['ApplicationSchema'] | null>(null);
	let feedbackText = $state('');
	let showFeedbackDialog = $state(false);
	let currentAction = $state<'approve' | 'decline' | null>(null);

	const queryClient = useQueryClient();

	// Query to fetch project applications
	const applicationsQuery = createQuery({
		queryKey: ['projectApplications', projectId],
		queryFn: () => getProjectApplications(projectId),
		enabled: !!projectId
	});

	// Mutation for approving or declining applications
	const applicationMutation = createMutation({
		mutationFn: ({
			projectId,
			isApproved,
			userId,
			feedback
		}: {
			projectId: number;
			isApproved: boolean;
			userId: number;
			feedback: string;
		}) => approveApplication(projectId, isApproved, userId, feedback),
		onSuccess: () => {
			// Invalidate and refetch project applications
			queryClient.invalidateQueries({ queryKey: ['projectApplications', projectId] });
			toast.success(
				`Application ${currentAction === 'approve' ? 'approved' : 'declined'} successfully`
			);
			// Reset state
			showFeedbackDialog = false;
			selectedApplication = null;
			feedbackText = '';
			currentAction = null;
		},
		onError: (error) => {
			toast.error(`Failed to ${currentAction} application: ${error.message}`);
		}
	});

	// Function to handle application action (approve/decline)
	function handleApplicationAction(
		application: components['schemas']['ApplicationSchema'],
		action: 'approve' | 'decline'
	) {
		selectedApplication = application;
		currentAction = action;
		showFeedbackDialog = true;
	}

	// Function to submit the application decision
	function submitApplicationDecision() {
		if (!selectedApplication) return;

		$applicationMutation.mutate({
			projectId,
			isApproved: currentAction === 'approve',
			userId: selectedApplication.user_id,
			feedback: feedbackText
		});
	}
</script>

<!-- Main Dialog for Project Contributors -->
<Dialog.Root bind:open>
	<Dialog.Content class="sm:max-w-3xl">
		<Dialog.Header>
			<Dialog.Title>Project Applications</Dialog.Title>
			<Dialog.Description>Review and manage applications for your project.</Dialog.Description>
		</Dialog.Header>

		<div class="max-h-[60vh] overflow-y-auto py-4">
			{#if $applicationsQuery.isPending}
				<div class="flex items-center justify-center py-8">
					<LoaderCircle class="h-8 w-8 animate-spin" />
				</div>
			{:else if $applicationsQuery.isError}
				<ErrorAlert text={$applicationsQuery.error.message} />
			{:else if $applicationsQuery.data.length === 0}
				<div class="text-muted-foreground py-8 text-center">
					No applications have been submitted for this project yet.
				</div>
			{:else}
				<div class="space-y-6">
					{#each $applicationsQuery.data as application ([application.user_id, application.project_id])}
						<div class="rounded-lg border p-4">
							<div class="flex items-start justify-between">
								<div>
									{#await getUserById(application.user_id)}
										<div class="bg-muted h-5 w-32 animate-pulse rounded"></div>
									{:then user}
										<h3 class="text-lg font-medium">{user.username}</h3>
									{:catch error}
										<div class="text-destructive">Failed to load user: {error.message}</div>
									{/await}

									<div class="mt-2">
										<Badge
											variant={application.is_approved === null
												? 'outline'
												: application.is_approved
													? 'default'
													: 'destructive'}
										>
											{#if application.is_approved === null}
												Pending
											{:else if application.is_approved}
												Approved
											{:else}
												Declined
											{/if}
										</Badge>
										{#if application.created_at}
											<span class="text-muted-foreground ml-2 text-xs">
												Applied on {new Date(application.created_at).toLocaleDateString()}
											</span>
										{/if}
									</div>
								</div>

								{#if application.is_approved === null}
									<div class="flex gap-2">
										<Button
											size="sm"
											variant="default"
											onclick={() => handleApplicationAction(application, 'approve')}
										>
											<UserCheck class="mr-1 h-4 w-4" />
											Approve
										</Button>
										<Button
											size="sm"
											variant="destructive"
											onclick={() => handleApplicationAction(application, 'decline')}
										>
											<UserX class="mr-1 h-4 w-4" />
											Decline
										</Button>
									</div>
								{/if}
							</div>

							{#if application.feedback}
								<div class="mt-3">
									<p class="mb-1 text-sm font-medium">Your feedback:</p>
									<p class="bg-muted rounded p-3 text-sm">{application.feedback}</p>
								</div>
							{/if}
						</div>
					{/each}
				</div>
			{/if}
		</div>

		<Dialog.Footer>
			<Dialog.Close>
				<Button variant="outline">Close</Button>
			</Dialog.Close>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>

<!-- Feedback Dialog -->
<Dialog.Root bind:open={showFeedbackDialog}>
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>
				{currentAction === 'approve' ? 'Approve' : 'Decline'} Application
			</Dialog.Title>
			<Dialog.Description>
				{#if currentAction === 'approve'}
					Provide feedback for the applicant about their acceptance.
				{:else}
					Please explain why you're declining this application.
				{/if}
			</Dialog.Description>
		</Dialog.Header>

		<div class="space-y-4 py-4">
			<div class="space-y-2">
				<Label for="feedback">Feedback</Label>
				<Textarea
					id="feedback"
					bind:value={feedbackText}
					placeholder={currentAction === 'approve'
						? 'Welcome to the team! Please provide any onboarding details...'
						: 'Thank you for your application, however...'}
					rows={5}
				/>
			</div>
		</div>

		<Dialog.Footer>
			<Button
				variant="outline"
				onclick={() => {
					showFeedbackDialog = false;
					selectedApplication = null;
					feedbackText = '';
					currentAction = null;
				}}
			>
				Cancel
			</Button>
			<Button
				variant={currentAction === 'approve' ? 'default' : 'destructive'}
				onclick={submitApplicationDecision}
				disabled={$applicationMutation.isPending}
			>
				{#if $applicationMutation.isPending}
					<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
					Processing...
				{:else}
					<MessageSquare class="mr-2 h-4 w-4" />
					Send {currentAction === 'approve' ? 'Approval' : 'Rejection'}
				{/if}
			</Button>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
