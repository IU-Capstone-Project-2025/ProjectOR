<script lang="ts">
	import SvelteMarkdown from 'svelte-markdown';
	import Heading from './Heading.svelte';
	import List from './List.svelte';
	import Link from './Link.svelte';
	import Paragraph from './Paragraph.svelte';
	import CodeSpan from './CodeSpan.svelte';
	import Table from './Table.svelte';
	import TableCell from './TableCell.svelte';
	import TableHead from './TableHead.svelte';
	import TableRow from './TableRow.svelte';
	import Blockquote from './Blockquote.svelte';

	const { content }: { content: string } = $props();
</script>

<SvelteMarkdown
	source={content}
	renderers={{
		heading: Heading,
		list: List,
		link: Link,
		paragraph: Paragraph,
		codespan: CodeSpan,
		table: Table,
		tablecell: TableCell,
		tablehead: TableHead,
		tablerow: TableRow,
		blockquote: Blockquote
	}}
/>
