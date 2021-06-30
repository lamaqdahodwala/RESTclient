<script>
	async function load_projects(){
		let all_projects = await fetch('/api/v1/get_all_projects')
		.then(res => res.json())

		return all_projects
	}
	let all_projects = load_projects()
</script>

<main>
	<br><br><br>
	{#await all_projects}
		<div class="container has-text-centered">
			<progress class='progress is-primary' max='100'></progress>
			<p class="help">Loading!</p>
		</div>
	{:then all} 
		<div class="container">
			<h1 class="title">Your projects</h1>
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
</main>
