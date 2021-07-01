<script>
    export let id;
    async function load_project(){
        let res = await fetch(`/api/v1/get_project/${id}`)
        let json = await res.json()
        return json
    }

    let prom = load_project()
</script>

{#await prom}
    <div class="container has-text-centered">
        <progress max='100' class='progress is-primary'></progress>
        <p class="help">Loading!</p>
    </div>
{:then data} 
    <nav class="navbar">
        <div class="navbar-brand">
            <div class="navbar-item">
                <h1 class="title">{data.project_name}</h1>
            </div>
        </div>
    </nav>
    <div class="container">
        <input type="text" class='input' value={data.request_url}>
    </div>
{:catch error}
<div class="message">
    <div class="message-header">
        <h1 class="title">Error!</h1>
    </div>
</div>
{/await}