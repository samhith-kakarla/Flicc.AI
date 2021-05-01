<script>
    // STATE
    let name; 

    // METHODS
    

</script>

<main>
    <img src="images/flicclogo.PNG" alt="" class="icon-logo"> <br />
    <img src="images/flicctextlogo.PNG" alt="" class="text-logo">
    <h3 class="header">Designing the perfect home theater system for you!</h3>
    <p class="name-input-label">ENTER YOUR NAME TO GET STARTED</p>
    <div>
        <input type="text" class="name-input" bind:value={name}>
        <button class="go">GO!</button>
    </div>
</main>

<style>
    .icon-logo {
        height: 250px;
    }

    .text-logo {
        height: 100px;
    }

    .h1 {
        height: 150px;
    }

    .header {

    }

    .name-input-label {

    }

    .name-input {

    }

    .go {
        color: #421961;
        font-weight: bold;
    }
</style>