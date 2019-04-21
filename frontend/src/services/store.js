import axios from "axios";
export const store = {
  state: {
    expenses: [],
    msgs: {}
  },

  setError(errorContext, err) {
    this.state.msgs[errorContext] = err;
  },

  async getAllExpenses() {
    try {
      const response = await axios.get("http://localhost:5000");
      this.state.expenses = response.data;
    } catch (err) {
      this.setError("getAllExpenses", err);
    }
  },

  async saveExpense(expenseData) {
    try {
      await axios.post("http://localhost:5000", expenseData);
      await this.getAllExpenses();
    } catch (err) {
      this.setError("saveExpense", err);
    }
  },

  async deleteExpense(id) {
    try {
      const url = `http://localhost:5000/${id}`;
      await axios.delete(url);
      await this.getAllExpenses();
    } catch (err) {
      this.setError("deleteExpense", err);
    }
  }
};
