// functions that can be used in vue spaces

export function timestampHuman (timestamp) {
  const datetime = new Date(timestamp)
  const options = { day: '2-digit', month: '2-digit', year: '2-digit', hour: 'numeric', minute: 'numeric' }
  return datetime.toLocaleString('en-US', options)
}
