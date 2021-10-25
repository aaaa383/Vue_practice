<template>

  <div calss="contianer">
      <h2>Form Below</h2>
        <input v-model="sepalLength" placeholder="sepalLength">
        <br>
        <input v-model="sepalWidth" placeholder="sepalWidth">
        <br>
        <input v-model="petalWidth" placeholder="petalWidth">
        <br>
        <input v-model="petalLength" placeholder="petalLength">
  </div>

    <button @click="submit">
        Submit
    </button>

    <h3>
        Predictions: {{predictedClass}}
    </h3>

</template>

<script>
import Button from './Button.vue'
import axios from 'axios'


export default {
    name: "SKLearn",
    data: () => ({
        sepalLength: '',
        sepalWidth: '',
        petalLength: '',
        petalWidth: '',
        predictedClass : '',
    }),
    methods: {
        submit () {
        console.log("Submit");
        axios.post('http://127.0.0.1:5000/predict', {
            sepal_length: this.sepalLength,
            sepal_width: this.sepalWidth,
            petal_length: this.petalLength,
            petal_width: this.petalWidth
        })
        .then((response) => {
            console.log(response);
            this.predictedClass = response.data.class
        })
        },
        clear () {
        this.sepalLength = ''
        this.sepalWidth = ''
        this.petalLength = ''
        this.petalWidth = ''
        }
  },
  components: {
      Button
  }

}
</script>

<style>

</style>