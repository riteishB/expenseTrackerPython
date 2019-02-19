<template>
  <div class="expenseViewContainer">
    <h2>Expenses</h2>
    <ul id="example-1">
      <md-list v-for="expense in expenses" v-bind:key="expense.id">
        <md-list-item>{{expense.expense_name}}</md-list-item>
      </md-list>
    </ul>
  </div>
</template>

<style>
.expenseViewContainer {
  width: 400px;
  height: 400px;
  border: 1px solid black;
  box-shadow: 0 0 3px 1px black;
}
</style>

<script>
import axios from "axios";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";

import Vue from "vue";
Vue.use(VueMaterial);
export default {
  name: "ExpenseViewer",
  data: () => {
    return {
      expenses: []
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000")
      .then(response => {
        this.expenses = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
  //   props: {}
};
</script>


