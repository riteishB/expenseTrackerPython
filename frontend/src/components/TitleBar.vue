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

</style>


<!-- Script below is called in the template tag above, name should match the file name, and msg should be of data type intended to pass -->
<!-- props is what we pass from a component to another component -->

<script>
export default {
  name: "TitleBar",
  props: {         
    msg: String
  }
};
</script>

