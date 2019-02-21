<template>
  <md-table
    v-model="expenses"
    md-sort="name"
    md-sort-order="asc"
    md-card
    md-fixed-header
    style="text-align:left"
  >
    <md-table-toolbar>
      <h1 class="md-title">Expenses</h1>
    </md-table-toolbar>

    <md-table-row slot="md-table-row" slot-scope="{ item }">
      <md-table-cell md-label="Name">{{ item.expense_name }}</md-table-cell>
      <md-table-cell md-label="Type" md-sort-by="expense_type">{{ item.expense_type }}</md-table-cell>
      <md-table-cell md-label="Date Created" md-sort-by="creation_date">{{ item.creation_date }}</md-table-cell>
      <md-table-cell md-label="Date Modified" md-sort-by="modified_date">{{ item.modified_date }}</md-table-cell>
      <md-table-cell md-label="Amount" md-sort-by="expense_amt">{{ item.expense_amt }}</md-table-cell>
    </md-table-row>
  </md-table>
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


