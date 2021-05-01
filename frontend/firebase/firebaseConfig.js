import firebase from 'firebase/app'; 

const firebaseConfig = {
    apiKey: "AIzaSyD2RV3-rxlGPadLahCmQYLxPwmwWfKCNKY",
    authDomain: "flicc-15b89.firebaseapp.com",
    projectId: "flicc-15b89",
    storageBucket: "flicc-15b89.appspot.com",
    messagingSenderId: "946648581624",
    appId: "1:946648581624:web:72ceb7bb1b8b3d3ec5c20d"
  };

  // Initialize Firebase
firebase.initializeApp(firebaseConfig);


export default firebase; 