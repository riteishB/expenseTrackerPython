<template>
  <div class="header">
  <!-- <h1> Header </h1> -->
  <h1> {{msg}} </h1>
  <!-- <p>{{msg}}</p> -->
</div>

</template>

<style>
/* Style the body */
body {
  font-family: Arial;
  margin: 0;
}

/* Header/Logo Title */
.header {
  padding: 10px;
  text-align: left;
  background: #089579;
  color: white;
  font-size: 10px;
}


 /* Page Content */
.content {padding:20px;} 
</style>



<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
