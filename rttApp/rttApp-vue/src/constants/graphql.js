import gql from 'graphql-tag'

// export const ALL_TASKS_QUERY = gql`
//   query AllTasksQuery {
//     allTasks {
//       timestamp
//       id
//       asset {
//         number
//       }
//       taskDescription
//       state {
//         state
//       }
//     }
//   }
// `

export const ALL_STATES_QUERY = gql`
  query AllStatesQuery {
    allStates {
      id
      state
    }
  }
`

export const TASKS_QUERY = gql`
  query TasksQuery ($searchAssetNumber: Int) {
    tasks (assetNumber: $searchAssetNumber) {
      id
      asset{
        number
      }
      timestamp
      taskDescription
      taskCategory {
        category
      }
      state {
        state
      }
    }
  }
`

export const TASK_DETAIL_QUERY = gql`
  query ($taskID: ID!) {
    task(taskID: $taskID) {
      id
      asset {
        number
        model {
          make {
            maker
          }
          modelName
        }
        serial
        macAddress
        notes
        assetAssemblyRef {
          component {
            id
            model {
              make {
                maker
              }
              modelName
            }
            serial
          }
        }
      }
      state {
        state
      }
      taskDescription
      submittedByUser {
        username
      }
      taskDate
      originalLocation
      replacementAsset {
        number
        model {
          make {
            maker
          }
          modelName
        }
      }
      fixDescription
      managementComments
      dateCompleted
    }
  }
`
