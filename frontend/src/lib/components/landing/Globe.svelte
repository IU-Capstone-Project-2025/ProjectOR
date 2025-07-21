<script lang="ts">
	import { onMount } from 'svelte';
	import createGlobe from 'cobe';
	import { Spring } from 'svelte/motion';
	import { cn } from '$lib/utils';

	const x = new Spring(0, {
		stiffness: 0.04,
		damping: 0.4,
		precision: 0.005
	});

	const { class: className = '' }: { class?: string } = $props();
	let pointerInteracting: number | null = $state(null);
	let pointerInteractionMovement = $state(0);
	let canvas: HTMLCanvasElement;

	let phi = 0;
	let width = 0;

	let onResize = () => {
		width = canvas.offsetWidth;
	};

	// eslint-disable-next-line  @typescript-eslint/no-explicit-any
	let onRender = (state: any) => {
		if (!pointerInteracting) {
			phi += 0.005;
		}
		state.phi = phi + x.current;
		state.width = width * 2;
		state.height = width * 2;
	};

	onMount(() => {
		// Adds the resize event listener when the component is mounted
		window.addEventListener('resize', onResize);
		onResize();

		// eslint-disable-next-line  @typescript-eslint/no-unused-vars
		const globe = createGlobe(canvas, {
			devicePixelRatio: 2,
			width: width,
			height: width,
			phi: 0,
			theta: 0.3,
			dark: 1,
			diffuse: 0.4, // 1.2
			mapSamples: 16000,
			mapBrightness: 1.2, // 6
			baseColor: [0.3, 0.3, 0.3],
			markerColor: [251 / 255, 100 / 255, 21 / 255],
			glowColor: [1, 1, 1],
			markers: [
				{ location: [14.5995, 120.9842], size: 0.03 },
				{ location: [19.076, 72.8777], size: 0.03 },
				{ location: [23.8103, 90.4125], size: 0.05 },
				{ location: [30.0444, 31.2357], size: 0.07 },
				{ location: [39.9042, 116.4074], size: 0.08 },
				{ location: [-23.5505, -46.6333], size: 0.05 },
				{ location: [19.4326, -99.1332], size: 0.04 },
				{ location: [40.7128, -74.006], size: 0.1 },
				{ location: [34.6937, 135.5022], size: 0.05 },
				{ location: [41.0082, 28.9784], size: 0.06 },
				{ location: [51.5074, -0.1278], size: 0.1 },
				{ location: [55.7558, 37.6173], size: 0.05 },
				{ location: [48.8566, 2.3522], size: 0.08 },
				{ location: [52.52, 13.405], size: 0.07 },
				{ location: [35.6762, 139.6503], size: 0.1 },
				{ location: [37.7749, -122.4194], size: 0.1 },
				{ location: [55.6761, 12.5683], size: 0.05 },
				{ location: [59.9139, 10.7522], size: 0.05 },
				{ location: [60.1695, 24.9354], size: 0.05 },
				{ location: [64.1355, -21.8954], size: 0.05 },
				{ location: [55.7513, 48.732], size: 0.5 }
			],
			onRender: onRender
		});

		// Removes the resize event listener when the component is unmounted to prevent memory leaks
		return () => {
			window.removeEventListener('resize', onResize);
		};
	});
</script>

<main class={cn('absolute inset-0 mx-auto aspect-[1/1] w-full max-w-[600px]', className)}>
	<canvas
		class="h-full w-full [contain:layout_paint_size]"
		bind:this={canvas}
		onpointerdown={(e) => {
			pointerInteracting = e.clientX - pointerInteractionMovement;
			canvas.style.cursor = 'grabbing';
		}}
		onpointerup={() => {
			pointerInteracting = null;
			canvas.style.cursor = 'grab';
		}}
		onpointerout={() => {
			pointerInteracting = null;
			canvas.style.cursor = 'grab';
		}}
		onmousemove={(e) => {
			if (pointerInteracting !== null) {
				const delta = e.clientX - pointerInteracting;
				pointerInteractionMovement = delta;
				x.set(delta / 200);
			}
		}}
	></canvas>
</main>
