import Workspace from './Workspace.svelte'; 

const workspace = new Workspace({
    target: document.getElementById("workspace-target"),
    props: JSON.parse(document.getElementById('workspace-props').textContent)
})

export default workspace