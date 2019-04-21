<template>
  <div id="app">
    <TitleBar msg="Welcome to ExpenseTracker"/>
    <ExpenseViewer></ExpenseViewer>
  </div>
</template>

<script>
import TitleBar from "./components/TitleBar.vue";
import ExpenseViewer from "./components/ExpenseViewer";
import insertExpenseDialog from "./components/insertExpenseDialog";

export default {
  name: "app",
  components: {
    TitleBar,
    ExpenseViewer,
    insertExpenseDialog
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
