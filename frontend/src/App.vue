<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Minami"/>
  <Test />
  <SKLearn/>
  <Result />
  <Input />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Test from './components/Test.vue'
import Result from './components/Result.vue'
import SKLearn from './components/sklearn.vue'
import Input from './components/Input.vue'

export default {
  name: 'App',
  components: {
    Test,
    Result,
    SKLearn,
    Input
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}


.container {
  max-width: 230px;
  margin: 30px auto;
  overflow: auto;
  min-height: 40px;
  border: 5px solid green;
  padding: 30px;
  border-radius: 5px;
}

.result{
  max-width: 230px;
  margin: 30px auto;
  overflow: auto;
  min-height: 40px;
  border: 5px dashed red;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 25px 30px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}

</style>
