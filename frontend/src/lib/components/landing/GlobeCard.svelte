<script>
	import Globe from './Globe.svelte';
	import WordRotate from './WordRotate.svelte';
</script>

<div
	class="bg-background relative flex h-fit w-full max-w-[32rem] items-center justify-center overflow-hidden rounded-lg border px-40 pt-8 pb-40 md:pb-60 md:shadow-xl"
>
	<span
		class="pointer-events-none bg-gradient-to-b from-black to-gray-300/80 bg-clip-text text-center text-8xl leading-none font-semibold whitespace-pre-wrap text-transparent select-none dark:from-white dark:to-slate-900/10"
	>
		<WordRotate words={['Explore', 'Discover', 'Collaborate', 'Connect', 'Build', 'Launch']} />
	</span>
	<Globe class="top-28" />
	<div
		class="pointer-events-none absolute inset-0 h-full bg-[radial-gradient(circle_at_50%_200%,rgba(0,0,0,0.2),rgba(255,255,255,0))]"
	/>
</div>
