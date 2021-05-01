<script>
	// PAGES
	import Home from './pages/Home.svelte'; 
	import Setup from './pages/Setup.svelte'; 
	import Dashboard from './pages/Dashboard.svelte'; 
	import Loading from './pages/Loading.svelte'; 

</script>

<main>
	<Home></Home>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>