<template>
  <div id='AssetSearch' class='ph4'>
    <div class='w-100 page_title'>
      <h2 class='f4 tc'>Task Search</h2>
    </div>
    <div>
      <label for='asset_search'>Search:</label>
      <input 
        id='asset_search' 
        type='number' 
        v-model='searchAssetNumber'
        placeholder='Asset Number'></input>
    </div>
    <div class='table_container'>
      <task-table :tasks='tasks' :loading='loading'>
      </task-table>
    </div>
  </div>
</template>

<script>
import { TASKS_QUERY } from '../constants/graphql'
import TaskTable from './TaskTable'

export default {
  name: 'AssetSearch',
  data () {
    return {
      tasks: [],
      searchAssetNumber: '',
      loading: 0
    }
  },
  apollo: {
    tasks: {
      query: TASKS_QUERY,
      variables () {
        return {
          searchAssetNumber: this.searchAssetNumber
        }
      },
      skip () {
        return !this.searchAssetNumber
      }
    }
  },
  components: {
    TaskTable
  }
}
</script>
