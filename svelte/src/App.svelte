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
		<div class="container">
			<progress class='progress is-primary' max='100'></progress>
		</div>
	{:then all} 
		<div class="container">
			{#each all as i}
				<div class="card">
					<div class="card-header">
						<h1 class="card-header-title title">{i.project_name}</h1>
					</div>
					<div class="card-content">
						URL: {i.req_url}
					</div>
				</div>
			{/each}
		</div>
	{/await}
</main>
