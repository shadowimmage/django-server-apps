<template>
  <tr>
    <td class='pa1'>
      <router-link 
        class='no-underline'
        :to="{ name: 'TaskView', params: { taskurl: task.id }}">
        {{ task.asset.number }}
      </router-link>
    </td>
    <td class='pa1'>{{ timestampHuman(task.timestamp) }}</td>
    <td class='pa1'>{{ task.taskDescription }}</td>
    <td class='pa1'>{{ task.taskCategory.category }}</td>
    <td class='pa1'>{{ task.state.state }}</td>
  </tr>
</template>

<script>
import { timestampHuman } from '../utils'
export default {
  name: 'TaskTableRow',
  props: ['task'],
  methods: {
    timestampHuman
  }
}
</script>
