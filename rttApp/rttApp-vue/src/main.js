// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import 'tachyons'
import ApolloClient, { createNetworkInterface } from 'apollo-client'
import VueApollo from 'vue-apollo'
import App from './App'
import router from './router'

Vue.config.productionTip = false

const networkInterface = createNetworkInterface({
  uri: 'http://localhost:8000/graphql/',
  opts: {
    credentials: 'same-origin'
  }
})

networkInterface.use([{
  applyMiddleware (req, next) {
    if (!req.options.headers) {
      req.options.headers = {}  // Create the header object if needed.
    }
    // req.options.headers['Accept'] = 'application/json' <-- not needed
    // req.options.headers['Content-Type'] = 'application/graphql' <-- BAD
    req.options.headers['X-CSRFToken'] = localStorage.getItem('csrftoken') ? localStorage.getItem('csrftoken') : null
    next()
  }
}])

const apolloClient = new ApolloClient({
  networkInterface,
  connectToDevTools: true
})

Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
  defaultOptions: {
    $loadingKey: 'loading'
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  apolloProvider,
  router,
  render: h => h(App)
})
