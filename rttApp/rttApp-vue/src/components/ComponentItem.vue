<template>
  <li class='dib'>{{ components.component.model.make.maker }} {{ components.component.model.modelName }} {{ components.component.serial }}</li>
</template>


<script>
export default {
  name: 'ComponentItem',
  props: ['components']
}
</script>
