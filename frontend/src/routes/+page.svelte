<script lang="ts">
	import { Button } from '@/components/ui/button';

	let cnt = $state(0);
</script>

<h1>Hello world!</h1>
<Button onclick={() => cnt++}>Click me ! ({cnt})</Button>
