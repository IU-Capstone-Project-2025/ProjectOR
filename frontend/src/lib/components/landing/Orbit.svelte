<script lang="ts">
	import { cn } from '$lib/utils';
	import OrbitingCircles from './OrbitingCircles.svelte';
	import { Code, Lightbulb, Eye, DollarSign } from '@lucide/svelte';

	let className: string = '';
	export { className as class };
</script>

<div
	class={cn(
		'bg-background relative flex h-[400px] w-full max-w-[26rem] items-center justify-center overflow-hidden rounded-xl border md:shadow-xl',
		className
	)}
>
	<span
		class="pointer-events-none bg-gradient-to-b from-black to-gray-300/80 bg-clip-text text-center text-6xl leading-none font-semibold whitespace-pre-wrap text-transparent dark:from-white dark:to-slate-900/10"
	>
		ProjectOR
	</span>

	<!--  Inner Circles  -->
	<OrbitingCircles class="h-[30px] w-[30px] border-none bg-transparent" duration={20} radius={80}>
		<DollarSign class="text-green-500" />
	</OrbitingCircles>
	<OrbitingCircles
		class="h-[30px] w-[30px] border-none bg-transparent"
		duration={20}
		radius={80}
		delay={-10}
	>
		<Eye />
	</OrbitingCircles>

	<!-- Outer Circles (reverse)  -->
	<OrbitingCircles
		class="h-[45px] w-[45px] border-none bg-transparent"
		radius={160}
		duration={20}
		reverse
	>
		<Lightbulb class="text-yellow-500" />
	</OrbitingCircles>
	<OrbitingCircles
		class="h-[45px] w-[45px] border-none bg-transparent"
		radius={160}
		duration={20}
		delay={-10}
		reverse
	>
		<Code class="text-blue-500" />
	</OrbitingCircles>
</div>
