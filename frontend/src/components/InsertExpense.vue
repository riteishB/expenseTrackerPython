<template>
  <form novalidate class="md-layout">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">CreateExpense</div>
      </md-card-header>

      <md-card-content>
        <div class="md-layout md-gutter">
          <div class="input-container">
            <md-field>
              <label for="expense_name">Expense Name</label>
              <md-input
                name="expense_name"
                id="expense_name"
                autocomplete="name for expense"
                v-model="expense.expense_name"
              />
            </md-field>
          </div>
          <div class="input-container">
            <md-field>
              <label for="expense_amt">Expense Amount</label>
              <md-input
                name="expense_amt"
                id="expense_amt"
                autocomplete="expense amount"
                v-model="expense.expense_amt"
              />
            </md-field>
          </div>
          <div class="input-container">
            <md-field>
              <label for="expense_type">Expense Type</label>
              <md-input
                name="expense_type"
                id="expense_type"
                autocomplete="name for expense"
                v-model="expense.expense_type"
              />
            </md-field>
          </div>
        </div>
      </md-card-content>
      <md-card-actions>
        <md-button class="md-primary" v-on:click="saveExpense">Save Expense</md-button>
      </md-card-actions>
    </md-card>
  </form>
</template>



<script>
import { store } from "../services/store.js";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import Vue from "vue";
Vue.use(VueMaterial);

export default {
  name: "InsertExpense",
  props: {
    showDialog: true
  },
  data: function() {
    return {
      expense: {
        expense_name: null,
        expense_amt: null,
        expense_type: null
      }
    };
  },
  methods: {
    async saveExpense() {
      await store.saveExpense(this.expense);
      if (store.getError("saveExpense") === null) {
        this.$emit("update:showDialog", false);
      }
    }
  }
};
</script>

<style scope>
.input-container {
  width: 100%;
  padding: 20px;
}
</style>



