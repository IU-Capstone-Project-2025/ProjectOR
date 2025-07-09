<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import ChooseRoleDialog from './(components)/ChooseRoleDialog.svelte';

	const { data } = $props();
	let isChooseRoleDialogOpen = $state(false);

	onMount(() => {
		if (!data.user) {
			goto('/auth/login');
			return;
		}
		if (data.user.role === 'VIEWER') {
			isChooseRoleDialogOpen = true;
			return;
		}
		goto('/app/explore');
	});
</script>

<ChooseRoleDialog bind:open={isChooseRoleDialogOpen} />
