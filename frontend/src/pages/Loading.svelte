<script>
    // IMPORTS
    import { onMount } from 'svelte'; 
    import { Circle2 } from 'svelte-loading-spinners'; 

    // STATE

    // METHODS

    onMount(async () => {

    })
</script>

<main>
    <div class="container">
        <h1>LOADING YOUR DESIGN!</h1>
        <div class="spinner">
            <Circle2 
                size="200" 
                colorInner="#fc9baa"
                colorOuter="#fd9a2b"
                colorCenter="#f6516a"
                unit="px" 
                duration="2s"
            >
            </Circle2>
        </div>
    </div>
</main>

<style>
    .spinner {
        margin-left: 505px;
        margin-top: 100px; 
    }
</style>