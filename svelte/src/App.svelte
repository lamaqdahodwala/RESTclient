<script>
	async function load_projects(){
		let all_projects = await fetch('/api/v1/get_all_projects')
		.then(res => res.json())

		return all_projects
	}
	let all_projects = load_projects()
</script>

<br><br><br>
<main class='container'>
	<h1 class="title">Your projects</h1>
	<div class="columns">
		<div class="column">
			{#await all_projects}
				<div class="container has-text-centered">
					<progress class='progress is-primary' max='100'></progress>
					<p class="help">Loading!</p>
				</div>
			{:then all}
				<div class="container">
					<hr>
					{#each all as i}
						<div class="card">
							<div class="card-header">
								<a href='/project/{i.pk}' class="card-header-title title">{i.project_name}</a>
							</div>
							<div class="card-content">
								URL: {i.request_url}
							</div>
						</div>
						<br><br>
					{/each}
				</div>
			{/await}
		</div>
		<div class="column is-2">
			<br>
			<div class="box">
				<div class="media">
					<a href="/new" class="button is-primary">Create project</a>
				</div>
			</div>
		</div>
	</div>
</main>
