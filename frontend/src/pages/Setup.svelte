<script>
    // IMPORTS
    import { onMount } from 'svelte'; 

    // STATE
    export let name; 
    let camera;
    let captureFile; 
    let canvas; 
    let context;
    let width, height, ratio; 

    // METHODS
    onMount(async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true }); 
            camera.srcObject = stream;
            camera.play(); 

            canvas = document.querySelector('canvas'); 
            context = canvas.getContext('2d');
            context.fillRect(0, 0, width, height);

            camera.addEventListener('loadedmetadata', function() {
                ratio = camera.width / camera.height;
                width = camera.width - 100; 
                height = parseInt(width / ratio, 10);
                canvas.width = width;
                canvas.height = height;
            }, false);
        } catch (error) {
            console.log(error); 
            console.log("camera access denied"); 
        }
    }); 

    function captureImage () {
        context.fillRect(0, 0, width, height);
        context.drawImage(camera, 0, 0, width, height);

        captureFile = canvas.toDataURL('image/png'); 
    }
    
</script>

<main>
    <h1>TAKE A PICTURE OF YOUR SPACE...</h1>
    <div>
        <video bind:this={camera} width="400" height="280" kind="captions" class="camera" />
        <div class="screenshot">
            <p style="text-align: left">YOUR IMAGE: </p>
            <canvas id="canvas" width="400" height="280" class="screenshot-canvas"></canvas>
        </div>
    </div>
    <button on:click={captureImage}>TAKE PIC</button>
    <p>OR UPLOAD AN IMAGE!</p>
    <input type="file" accept="image/*" capture="user">
    <button>CONTINUE</button>
</main>

<style>
    .camera {
        display: inline-block;
        margin: 10px auto;
    }

    .screenshot {
        display: inline-block;
        margin: 20px;
    }

    .screenshot-canvas {
        margin-bottom: 40px;
    }
</style>