<script>
    // IMPORTS
    import { onMount } from 'svelte'; 
    import { Circle2 } from 'svelte-loading-spinners'; 
    import firebase from '../../firebase/firebaseConfig.js'; 

    // STATE
    export let name; 
    export let captureFile; 
    let lengthOfRoom, widthOfRoom, heightOfRoom; 
    let speakers, subwoofers, receiver, screen, projector = {}; 

    // METHODS
    function getDimensionsOfRoom () {
        // Use Firebase ML Model Here
    }

    function getSpeakers (l, w, h) {

    }

    function getSubwoofers (l, w, h) {

    }

    function getReceiver (l, w, h) {

    }

    function getScreen (l, w, h) {

    }

    function getProjector (l, w, h) {

    }

    onMount(async () => {
        await getSpeakers(); 
        await getSubwoofers(); 
        await getReceiver(); 
        await getScreen(); 
        await getProjector(); 
    }); 
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