<script>
	import Marquee from './Marquee.svelte';
	import Reviewcard from './Reviewcard.svelte';

	const reviews = [
		{
			name: 'Skebob',
			username: '@Skebob',
			body: 'Noicee work. I love it. Keep it up.',
			img: 'https://avatar.vercel.sh/jack'
		},
		{
			name: 'Chupep',
			username: '@Chupep',
			body: 'Wooww, this is what I was looking for. Great work.',
			img: 'https://avatar.vercel.sh/jill'
		},
		{
			name: 'John Unitase',
			username: '@john_uni',
			body: 'ProjectOR is Amazing and so are you. Keep it up.',
			img: 'https://avatar.vercel.sh/john'
		},
		{
			name: 'AI Agent',
			username: '@AI_AGENT',
			body: 'Remarkable Stuff broooo. Added to my favourites.',
			img: 'https://avatar.vercel.sh/jane'
		},
		{
			name: 'Tralalala',
			username: '@Tralalala',
			body: 'ProjectOR is a game changer for project management. Love it!',
			img: 'https://avatar.vercel.sh/jenny'
		},
		{
			name: 'Tralalero',
			username: '@Tralalero',
			body: 'ProjectOR made easy with project idea. Great work.',
			img: 'https://avatar.vercel.sh/james'
		}
	];

	let firstRow = reviews.slice(0, reviews.length / 2);
	let secondRow = reviews.slice(reviews.length / 2);
</script>

<div
	class="bg-background relative flex h-full w-full flex-col items-center justify-center overflow-hidden rounded-lg border py-20 md:shadow-xl"
>
	<Marquee pauseOnHover class="[--duration:20s]">
		{#each firstRow as item (item.username)}
			<Reviewcard {...item} />
		{/each}
	</Marquee>
	<Marquee reverse pauseOnHover class="[--duration:20s]">
		{#each secondRow as item (item.username)}
			<Reviewcard {...item} />
		{/each}
	</Marquee>
	<div
		class="dark:from-background pointer-events-none absolute inset-y-0 left-0 w-1/3 bg-gradient-to-r from-white"
	></div>
	<div
		class="dark:from-background pointer-events-none absolute inset-y-0 right-0 w-1/3 bg-gradient-to-l from-white"
	></div>
</div>
