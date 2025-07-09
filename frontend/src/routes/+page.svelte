<script lang="ts">
	import { Button } from '@/components/ui/button';
	import * as Card from '@/components/ui/card';
	import { Badge } from '@/components/ui/badge';
	import placeholder from '@/assets/placeholder.svg';
	import {
		Lightbulb,
		Code,
		Users,
		TrendingUp,
		Skull,
		Eye,
		Rocket,
		DollarSign,
		ArrowRight,
		CheckCircle,
		Star,
		Github
	} from '@lucide/svelte';
</script>

<div class="flex min-h-screen flex-col">
	<header class="flex h-16 items-center border-b px-4 lg:px-6">
		<a class="flex items-center justify-center" href="/">
			<Rocket class="text-primary h-6 w-6" />
			<span class="ml-2 text-xl font-bold">ProjectOR</span>
		</a>
		<nav class="ml-auto flex gap-4 sm:gap-6">
			<a class="hover:text-primary text-sm font-medium transition-colors" href="#features">
				Features
			</a>
			<a class="hover:text-primary text-sm font-medium transition-colors" href="#roles">
				For Teams
			</a>
			<a class="hover:text-primary text-sm font-medium transition-colors" href="#graveyard">
				Learn
			</a>
		</nav>
		<div class="ml-6 flex gap-2">
			<Button variant="ghost" size="sm">
				<a href="/app">Sign In</a>
			</Button>
			<Button size="sm">
				<a href="/app">Get Started</a>
			</Button>
		</div>
	</header>

	<main class="flex-1">
		<section
			class="from-primary/5 via-background to-secondary/5 w-full bg-gradient-to-br py-12 md:py-24 lg:py-32 xl:py-48"
		>
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
					<div class="flex flex-col justify-center space-y-4">
						<div class="space-y-2">
							<Badge variant="secondary" class="w-fit">🚀 Where Ideas Meet Execution</Badge>
							<h1 class="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
								Connect. Build. Launch.
							</h1>
							<p class="text-muted-foreground max-w-[600px] md:text-xl">
								The ultimate platform connecting creators, developers, and investors. Turn your
								startup ideas into reality with the right team and funding.
							</p>
						</div>
						<div class="flex flex-col gap-2 min-[400px]:flex-row">
							<Button href="/app" size="lg">
								Start Building
								<ArrowRight class="ml-2 h-4 w-4" />
							</Button>
							<Button variant="outline" size="lg">Watch Demo</Button>
						</div>
						<div class="text-muted-foreground flex items-center gap-4 text-sm">
							<div class="flex items-center gap-1">
								<CheckCircle class="h-4 w-4 text-green-500" />
								Free to start
							</div>
							<div class="flex items-center gap-1">
								<CheckCircle class="h-4 w-4 text-green-500" />
								No credit card required
							</div>
						</div>
					</div>
					<div class="flex items-center justify-center">
						<div class="relative">
							<img
								src={placeholder}
								width="600"
								height="400"
								alt="Platform Dashboard"
								class="aspect-video overflow-hidden rounded-xl object-cover shadow-2xl"
							/>
							<div
								class="from-background/20 absolute inset-0 rounded-xl bg-gradient-to-t to-transparent"
							/>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section id="features" class="w-full py-12 md:py-24 lg:py-32">
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="flex flex-col items-center justify-center space-y-4 text-center">
					<div class="space-y-2">
						<Badge variant="secondary">Platform Features</Badge>
						<h2 class="text-3xl font-bold tracking-tighter sm:text-5xl">
							Everything you need to launch
						</h2>
						<p
							class="text-muted-foreground max-w-[900px] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed"
						>
							From idea conception to successful launch, our platform provides all the tools and
							connections you need.
						</p>
					</div>
				</div>
				<div class="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12">
					<Card.Root class="relative overflow-hidden">
						<Card.Header>
							<Lightbulb class="h-10 w-10 text-yellow-500" />
							<Card.Title>Idea Hub</Card.Title>
							<Card.Description>
								Post your startup ideas and get feedback from the community. Browse innovative
								concepts looking for co-founders.
							</Card.Description>
						</Card.Header>
						<Card.Content>
							<ul class="space-y-2 text-sm">
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Idea validation tools
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Community feedback
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Market research insights
								</li>
							</ul>
						</Card.Content>
					</Card.Root>

					<Card.Root class="relative overflow-hidden">
						<Card.Header>
							<Code class="h-10 w-10 text-blue-500" />
							<Card.Title>Developer Hub</Card.Title>
							<Card.Description>
								Discover exciting projects to join. Connect with founders and build the next big
								thing together.
							</Card.Description>
						</Card.Header>
						<Card.Content>
							<ul class="space-y-2 text-sm">
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Project matching
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Skill-based filtering
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Collaboration tools
								</li>
							</ul>
						</Card.Content>
					</Card.Root>

					<Card.Root class="relative overflow-hidden">
						<Card.Header>
							<Users class="h-10 w-10 text-green-500" />
							<Card.Title>Team Collaboration</Card.Title>
							<Card.Description>
								Built-in tools for seamless team communication, project management, and progress
								tracking.
							</Card.Description>
						</Card.Header>
						<Card.Content>
							<ul class="space-y-2 text-sm">
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Real-time messaging
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Task management
								</li>
								<li class="flex items-center gap-2">
									<CheckCircle class="h-4 w-4 text-green-500" />
									Progress analytics
								</li>
							</ul>
						</Card.Content>
					</Card.Root>
				</div>
			</div>
		</section>

		<section id="roles" class="bg-muted/50 w-full py-12 md:py-24 lg:py-32">
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="flex flex-col items-center justify-center space-y-4 text-center">
					<div class="space-y-2">
						<Badge variant="secondary">For Everyone</Badge>
						<h2 class="text-3xl font-bold tracking-tighter sm:text-5xl">
							Built for every role in the startup ecosystem
						</h2>
					</div>
				</div>
				<div class="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-2 lg:gap-12">
					<div class="grid gap-6 sm:grid-cols-2">
						<Card.Root class="text-center">
							<Card.Header>
								<Eye class="mx-auto h-8 w-8 text-gray-500" />
								<Card.Title class="text-lg">Viewers</Card.Title>
							</Card.Header>
							<Card.Content>
								<p class="text-muted-foreground text-sm">
									Explore ideas, follow projects, and stay updated on the latest innovations.
								</p>
							</Card.Content>
						</Card.Root>

						<Card.Root class="text-center">
							<Card.Header>
								<Code class="mx-auto h-8 w-8 text-blue-500" />
								<Card.Title class="text-lg">Developers</Card.Title>
							</Card.Header>
							<Card.Content>
								<p class="text-muted-foreground text-sm">
									Find exciting projects, showcase your skills, and join innovative teams.
								</p>
							</Card.Content>
						</Card.Root>

						<Card.Root class="text-center">
							<Card.Header>
								<Lightbulb class="mx-auto h-8 w-8 text-yellow-500" />
								<Card.Title class="text-lg">Founders</Card.Title>
							</Card.Header>
							<Card.Content>
								<p class="text-muted-foreground text-sm">
									Share your vision, build your team, and turn ideas into successful startups.
								</p>
							</Card.Content>
						</Card.Root>

						<Card.Root class="text-center">
							<Card.Header>
								<DollarSign class="mx-auto h-8 w-8 text-green-500" />
								<Card.Title class="text-lg">Investors</Card.Title>
							</Card.Header>
							<Card.Content>
								<p class="text-muted-foreground text-sm">
									Discover promising startups, connect with founders, and make strategic
									investments.
								</p>
							</Card.Content>
						</Card.Root>
					</div>
					<div class="flex items-center justify-center">
						<img
							src={placeholder}
							width="500"
							height="400"
							alt="Team Collaboration"
							class="aspect-square overflow-hidden rounded-xl object-cover"
						/>
					</div>
				</div>
			</div>
		</section>

		<section id="graveyard" class="w-full py-12 md:py-24 lg:py-32">
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
					<div class="flex flex-col justify-center space-y-4">
						<div class="space-y-2">
							<Badge variant="secondary" class="w-fit">
								<Skull class="mr-1 h-4 w-4" />
								Learn from Failure
							</Badge>
							<h2 class="text-3xl font-bold tracking-tighter sm:text-4xl xl:text-5xl/none">
								The Startup Graveyard
							</h2>
							<p class="text-muted-foreground max-w-[600px] md:text-xl">
								Learn from failed ventures. Our unique graveyard section documents startup failures
								with detailed analysis, helping you avoid common pitfalls and make better decisions.
							</p>
						</div>
						<div class="grid gap-4 sm:grid-cols-2">
							<div class="flex items-start gap-3">
								<TrendingUp class="mt-0.5 h-5 w-5 text-red-500" />
								<div>
									<h3 class="font-semibold">Failure Analysis</h3>
									<p class="text-muted-foreground text-sm">
										Detailed breakdowns of what went wrong
									</p>
								</div>
							</div>
							<div class="flex items-start gap-3">
								<Star class="mt-0.5 h-5 w-5 text-yellow-500" />
								<div>
									<h3 class="font-semibold">Key Learnings</h3>
									<p class="text-muted-foreground text-sm">
										Actionable insights for future projects
									</p>
								</div>
							</div>
						</div>
						<Button variant="outline" class="w-fit bg-transparent">Explore Graveyard</Button>
					</div>
					<div class="flex items-center justify-center">
						<img
							src={placeholder}
							width="600"
							height="400"
							alt="Startup Graveyard Analytics"
							class="aspect-video overflow-hidden rounded-xl object-cover shadow-lg"
						/>
					</div>
				</div>
			</div>
		</section>

		<section class="bg-muted/50 w-full py-12 md:py-24 lg:py-32">
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
					<div class="flex flex-col items-center space-y-2 text-center">
						<div class="text-3xl font-bold">10K+</div>
						<div class="text-muted-foreground text-sm">Active Users</div>
					</div>
					<div class="flex flex-col items-center space-y-2 text-center">
						<div class="text-3xl font-bold">500+</div>
						<div class="text-muted-foreground text-sm">Projects Launched</div>
					</div>
					<div class="flex flex-col items-center space-y-2 text-center">
						<div class="text-3xl font-bold">$2M+</div>
						<div class="text-muted-foreground text-sm">Funding Raised</div>
					</div>
					<div class="flex flex-col items-center space-y-2 text-center">
						<div class="text-3xl font-bold">95%</div>
						<div class="text-muted-foreground text-sm">Success Rate</div>
					</div>
				</div>
			</div>
		</section>

		<section class="bg-primary text-primary-foreground w-full py-12 md:py-24 lg:py-32">
			<div class="container mr-auto ml-auto px-4 md:px-6">
				<div class="flex flex-col items-center justify-center space-y-4 text-center">
					<div class="space-y-2">
						<h2 class="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
							Ready to turn your idea into reality?
						</h2>
						<p
							class="text-primary-foreground/80 mx-auto max-w-[600px] md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed"
						>
							Join thousands of creators, developers, and investors building the future together.
						</p>
					</div>
					<div class="flex flex-col gap-2 min-[400px]:flex-row">
						<Button size="lg" variant="secondary" href="/app">
							Get Started Free
							<ArrowRight class="ml-2 h-4 w-4" />
						</Button>
					</div>
				</div>
			</div>
		</section>
	</main>

	<footer
		class="flex w-full shrink-0 flex-col items-center gap-2 border-t px-4 py-6 sm:flex-row md:px-6"
	>
		<div class="flex items-center gap-2">
			<Rocket class="text-primary h-5 w-5" />
			<span class="font-semibold">ProjectOR</span>
		</div>
		<p class="text-muted-foreground text-xs sm:ml-4">© 2025 ProjectOR. All rights reserved.</p>
		<nav class="flex gap-4 sm:ml-auto sm:gap-6">
			<a class="text-xs underline-offset-4 hover:underline"> Terms of Service </a>
			<a class="text-xs underline-offset-4 hover:underline"> Privacy Policy </a>
			<a class="text-xs underline-offset-4 hover:underline"> Contact </a>
		</nav>
		<div class="flex gap-2">
			<Button
				variant="ghost"
				size="sm"
				href="https://github.com/IU-Capstone-Project-2025/ProjectOR"
			>
				<Github class="h-4 w-4" />
			</Button>
		</div>
	</footer>
</div>
