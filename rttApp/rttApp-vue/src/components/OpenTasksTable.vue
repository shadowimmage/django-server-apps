<template>
  <div id='OpenTasksTable' class='ph4'>
    <div class='w-100 page_title'>
      <h2 class='f4 tc'>Open Tasks</h2>
    </div>
    <div class='table_container'>
      <task-table :tasks='tasks' :loading='loading'>
      </task-table>
    </div>
  </div>
</template>

<script>
import TaskTable from './TaskTable'
import { TASKS_QUERY } from '../constants/graphql'

export default {
  name: 'OpenTasks',
  data () {
    return {
      tasks: [],
      loading: 0
    }
  },
  components: {
    TaskTable
  },
  apollo: {
    tasks: {
      query: TASKS_QUERY
    }
  }
}
</script>