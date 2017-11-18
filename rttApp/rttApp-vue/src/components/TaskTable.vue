<template>
  <div id='list' class='mv2 center w-100'>
    <div class='fl w-10 pa2'>
    </div>
    <div class='fl w-80 center pa2 dib bg-light-gray shadow-3'>
      <table class='w-100 collapse'>
        <thead class='f5'>
          <tr>
            <th class='pa1'>Asset</th>
            <th class='pa1'>Date</th>
            <th class='pa1'>Description</th>
            <th class='pa1'>Category</th>
            <th class='pa1'>State</th>
          </tr>
        </thead>
        <tbody class='f6'>
          <tr v-if='this.loading'>
            <td>
              <tr aria-colspan='4'>Loading...</tr>
            </td>
          </tr>
          <task-table-row
            v-for="task in this.tasks"
            :key="task.id"
            :task="task">
          </task-table-row>
        </tbody>
      </table>
    </div>
    <div class='fl w-10 pa2'>
    </div>
  </div>
</template>

<script>
import TaskTableRow from './TaskTableRow'

export default {
  name: 'TaskTable',
  props: {
    tasks: {
      type: Array,
      required: true
    },
    loading: {
      type: Number,
      required: true
    }
  },
  components: {
    TaskTableRow
  }
}
</script>

<style scoped>
tbody tr:nth-child(odd) {
  background-color: #ccc;
}
</style>
