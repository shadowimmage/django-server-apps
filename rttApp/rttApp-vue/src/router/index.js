import Vue from 'vue'
import Router from 'vue-router'

import AssetSearch from '@/components/AssetSearch'
import OpenTasksTable from '@/components/OpenTasksTable'
import TaskView from '@/components/TaskView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/open'
    },
    {
      path: '/search',
      name: 'Search',
      component: AssetSearch
    },
    {
      path: '/open',
      name: 'Open',
      component: OpenTasksTable
    },
    {
      path: '/task/:taskurl',
      name: 'TaskView',
      component: TaskView
    }
  ],
  mode: 'history'
})
