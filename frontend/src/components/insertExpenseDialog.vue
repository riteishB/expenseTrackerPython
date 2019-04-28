<template>
  <div>
    <md-dialog :md-active.sync="showDialog">
      <md-button class="md-primary" @click="showDialog = false" style="width: 20px">
        <md-icon>close</md-icon>
      </md-button>
      <InsertExpense v-bind:showDialog.sync="showDialog"></InsertExpense>
    </md-dialog>

    <md-button class="md-primary md-raised" @click="showDialog = true">Add Expenses</md-button>
  </div>
</template>

<script>
import InsertExpense from "./InsertExpense";
import axios from "axios";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import Vue from "vue";

Vue.use(VueMaterial);

export default {
  name: "insertExpenseDialog",
  components: {
    InsertExpense
  },
  data: () => ({
    showDialog: false
  })
};
</script>

<style>
.md-dialog {
  max-width: 768px;
  background: white;
}
</style>