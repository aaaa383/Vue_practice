<template>
  <div>
    <h1>{{ title }}</h1>
    <Button
      :text="'Add Task'"
      :color="'red'"
    />
    <Button
      :text="'Heello World'"
      :color="'black'"
    />
  </div>
</template>

<script>
import Button from './Button.vue'


export default {
  name: 'Header',
  props: {
    title: String,
  },
components: {
    Button
  },
}
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
</style>