import type { PageLoad } from './$types';
import { getProjects } from './(components)/dataLoaders';

export const load: PageLoad = async ({ parent }) => {
	const { queryClient } = await parent();

	await queryClient.prefetchQuery({
		queryKey: ['projects'],
		queryFn: async () => await getProjects()
	});
};
