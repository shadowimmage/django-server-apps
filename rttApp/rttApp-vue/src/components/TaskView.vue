<template>
  <div :id="$route.name">
    <div class='w-100 page_title dib bt'>
      <h2 class='pl4 f4 tl' v-if='this.loading'>Loading...</h2>
      <h2 class='pl4 f4 tl' v-if='!this.loading'>Issue {{ $route.params.taskurl }} - {{ task.state.state }}</h2>
    </div>
    <div class='ph4 w-100 center dib' v-if='!this.loading'>
      <div id='asset_info' class='ph2 mb2 w-100 bg-light-gray shadow-3 dib'>
        <h3 class='tl f5 cf'>Asset {{ task.asset.number }}</h3>
        <div>
          <div class='db fl ph3 cf'>
            <h4 class='mt0 f6 tl'>Metadata</h4>
            <table id='assetMetadata' class='collapse mw7 mb2'>
              <tr>
                <td class='nowrap tr v-top'>make:</td>
                <td class='pl2'>{{ task.asset.model.make.maker }}</td>
              </tr>
              <tr>
                <td class='nowrap tr v-top'>model:</td>
                <td class='pl2'>{{ task.asset.model.modelName }}</td>
              </tr>
              <tr>
                <td class='nowrap tr v-top'>serial:</td>
                <td class='pl2'>{{ task.asset.serial }}</td>
              </tr>
              <tr>
                <td class='nowrap tr v-top'>mac address:</td>
                <td class='pl2'>{{ task.asset.macAddress }}</td>
              </tr>
              <tr>
                <td class='nowrap tr v-top'>notes:</td>
                <td class='pl2'>{{ task.asset.notes }}</td>
              </tr>
            </table>
          </div>
          <div class='db fl ph3 cf'>
            <h4 class='mt0 f6 tl fl'>Components</h4>
            <button class='mh2 f6 fl br-pill ba'>edit</button>
            <!-- for component in component list... -->
            <ul class='list db mb2'>
              <component-item
                v-for="components in this.task.asset.assetAssemblyRef"
                :key="components.component.id"
                :components="components">
              </component-item>
            </ul>
          </div>
        </div>
      </div>
      <div id='task_info' class='ph2 mb2 w-100 bg-light-gray shadow-3 dib'>
        <h3 class='tl f5'>Issue Detail</h3>
          <div class='db fl ph3 cf'>
            <h4 class='mv0 f6 tl'>State</h4>
            <span class='dib mb2 ph2 pv1 f6 b--dark-gray bg-light-gray'>{{ task.state.state }}</span>
            <h4 class='mv0 f6 tl'>Description</h4>
            <p class='pl2 db w-100 mw7'>{{ task.taskDescription }}</p>
          </div>
          <div class='db fl ph3 cf'>
            <h4 class='mv0 f6 tl'>Submitted by</h4>
            <span class='pl2 mb2 db'>{{ task.submittedByUser.username }}</span>
            <h4 class='mv0 f6 tl'>Task Date</h4>
            <span class='pl2 mb2 db'>{{ timestampHuman(task.taskDate) }}</span>
            <h4 class='mv0 f6 tl'>Original Location</h4>
            <span class='pl2 mb2 db'>{{ task.originalLocation }}</span>
            <h4 class='mv0 f6 tl'>Replacement Asset</h4>
            <span class='pl2 mb2 db' v-if='task.replacementAsset'>
              {{ task.replacementAsset.number }} - 
              {{ task.replacementAsset.model.make.maker }} 
              {{ task.replacementAsset.model.modelName }}</span>
            <span class='pl2 mb2 db' v-if='!task.replacementAsset'>None</span>
          </div>
      </div>
      <div id='fix_info' class='ph2 mb2 w-100 bg-light-gray shadow-3 dib'>
        <h3 class='tl f5'>Repair/Fix Info</h3>
          <div class='ph3'>
            <div class='pv2'>
              <label class='db f6' for='fixDescription'>Fix description</label>
              <textarea 
                class='w-100 db f6 mw8' 
                name='Fix Description' 
                id='fixDescription' 
                rows='5' v
                v-model='task.fixDescription'>
              </textarea>
            </div>
            <div class='pv2'>
              <label class='db f6' for='managementComments'>Management Comments</label>
              <textarea 
                class='w-100 db f6 mw8' 
                name='Management Comments' 
                id='managementComments' 
                rows='5' 
                v-model='task.managementComments'>
              </textarea>
            </div>
            <div id='stateControl' class='pv2'>
              <label for='stateSelect' class='db f6'>Set state</label>
              <select id='stateSelect' class='f6'>
              <!-- for state in states -->
                <option 
                  v-for='state in allStates' 
                  :key='state.id' 
                  :state='state.state' 
                  :value='state'>{{ state.state }}
                </option>
              </select>
            </div>
            <div class='pv2'>
              <!-- show only if state selected is resolved -->
              <label for='dateCompleted' class='db f6'>Date Completed</label>
              <input type='date' id='dateCompleted' class='f6' />
            </div>
            <div id='save' class='pv2'>
              <button class='dib f6 pv1 ph2 bg--gray b--dark-gray ba br1 mb2'>Save</button>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { TASK_DETAIL_QUERY, ALL_STATES_QUERY } from '../constants/graphql'
import ComponentItem from './ComponentItem'
import { timestampHuman } from '../utils'

export default {
  name: 'TaskView',
  data () {
    return {
      task: [],
      allStates: [],
      loading: 0
    }
  },
  apollo: {
    task: {
      query: TASK_DETAIL_QUERY,
      variables () {
        return {
          taskID: this.$route.params.taskurl
        }
      }
    },
    allStates: {
      query: ALL_STATES_QUERY
    }
  },
  components: {
    ComponentItem
  },
  methods: {
    timestampHuman
  }
}
</script>

<style scoped>
#assetMetadata {
  table-layout: auto;
}
</style>
