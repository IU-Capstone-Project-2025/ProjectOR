import { getMe } from './(components)/dataLoaders';

export const load = async ({ parent }) => {
	const { queryClient } = await parent();

	await queryClient.prefetchQuery({
		queryKey: ['me'],
		queryFn: async () => await getMe()
	});
};
