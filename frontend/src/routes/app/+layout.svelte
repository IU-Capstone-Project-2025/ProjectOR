<script>
	import { Button } from '$lib/components/ui/button';
	import projector_logo from '$lib/assets/projector_logo.jpg';
	import CircleUserRound from '@lucide/svelte/icons/circle-user-round';
	import Plus from '@lucide/svelte/icons/plus';
	import SquareChartGantt from '@lucide/svelte/icons/square-chart-gantt';
	import { Input } from '@/components/ui/input/index.js';

	const { children } = $props();
</script>

<div style="--sidebar-width: calc(var(--spacing) * 72); --header-height: calc(var(--spacing) * 12);">
	<header
		class="h-(--header-height) group-has-data-[collapsible=icon]/sidebar-wrapper:h-(--header-height) flex shrink-0 items-center gap-2 border-b transition-[width,height] ease-linear"
	>
		<div class="flex w-full items-center gap-1 px-4 lg:gap-2 lg:px-6 justify-between">
			<div class="flex items-center gap-2">
				<img src={projector_logo} alt="ProjectOR Logo" class="h-8 w-8 rounded-full" />
				<h1 class="text-base font-medium">Explore Projects</h1>
			</div>
			<div class="items-center ml-auto w-full max-w-xs lg:max-w-sm">
				<Input
					type="search"
					placeholder="Search projects..."
					aria-label="Search projects"
					class="w-full max-w-xs lg:max-w-sm"
				/>
			</div>
			<div class="ml-auto flex items-center gap-2">
				<Button
					variant="default"
				>
					<Plus />
					Create Project
				</Button>
				<Button
					variant="outline"
				>
					<SquareChartGantt />
					My Projects
				</Button>
				<Button
					variant="ghost"
					size="icon"
					class="ml-10"
				>
					<CircleUserRound />
				</Button>
			</div>
		</div>
	</header>
</div>

{@render children()}