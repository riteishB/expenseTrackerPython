<template>
  <md-table
    v-model="state.expenses"
    md-sort="name"
    md-sort-order="asc"
    md-card
    md-fixed-header
    style="text-align:left"
  >
    <md-table-toolbar>
      <h1 class="md-title">Expenses</h1>
      <insertExpenseDialog></insertExpenseDialog>
    </md-table-toolbar>

    <md-table-row slot="md-table-row" slot-scope="{ item }">
      <md-table-cell md-label="Name">{{ item.expense_name }}</md-table-cell>
      <md-table-cell md-label="Type" md-sort-by="expense_type">{{ item.expense_type }}</md-table-cell>
      <md-table-cell md-label="Date Created" md-sort-by="creation_date">{{ item.creation_date }}</md-table-cell>
      <md-table-cell md-label="Date Modified" md-sort-by="modified_date">{{ item.modified_date }}</md-table-cell>
      <md-table-cell md-label="Amount" md-sort-by="expense_amt">{{ item.expense_amt }}</md-table-cell>
      <md-table-cell md-label="Actions">
        <md-menu md-direction="bottom-start">
          <md-button md-size="medium" md-menu-trigger>
            <md-icon>more_vert</md-icon>
          </md-button>

          <md-menu-content>
            <md-menu-item v-on:click="deleteExpense(item.id)">
              <md-icon>delete_outline</md-icon>Delete
            </md-menu-item>
            <md-menu-item v-on:click="updateExpense(item.id)">
              <md-icon>update</md-icon>Update
            </md-menu-item>
          </md-menu-content>
        </md-menu>
      </md-table-cell>
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
import insertExpenseDialog from "./insertExpenseDialog";
import InsertExpense from "./InsertExpense";
import axios from "axios";
import { store } from "../services/store.js";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";

import Vue from "vue";
Vue.use(VueMaterial);
export default {
  name: "ExpenseViewer",
  components: {
    insertExpenseDialog
  },
  data: () => {
    return {
      state: store.state
    };
  },
  methods: {
    showOptions() {
      console.log("Option clicked");
    },
    deleteExpense(id) {
      store.deleteExpense(id);
    },
    updateExpense(id) {
      console.log("Updating expense with id ", id);
    }
  },
  async mounted() {
    await store.getAllExpenses();
  }
};
</script>


