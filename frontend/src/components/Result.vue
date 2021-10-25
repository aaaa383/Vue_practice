<template>
  <div  class="test">
    <h1>
      Results go here!
    </h1>
  </div>  
</template>

<script>
export default {
  name: 'Result',
  props: {
    color: String
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


.test{
  max-width: 230px;
  margin: 30px auto;
  overflow: auto;
  min-height: 40px;
  border: 5px dashed red;
  padding: 30px;
  border-radius: 5px;
}


h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
