import type { PageLoad } from './$types';
import { getProjectById } from '../(components)/dataLoaders';

export const load: PageLoad = async ({ params, parent, fetch }) => {
	const { queryClient } = await parent();
	const projectId = parseInt(params.slug);

	if (isNaN(projectId)) {
		throw new Error('Invalid project ID');
	}

	await queryClient.prefetchQuery({
		queryKey: ['project', projectId],
		queryFn: async () => await getProjectById(projectId)
	});

	return {
		projectId
	};
};
