<template>
<label>
  <input type="file" @change="onFileChange">  
</label>
<div></div>
  <img 
    v-show="uploadedImage"
    :src="uploadedImage" alt="">
<br>
    <button @click="PostImage"> 
        Post
    </button>

</template>

<script>
import axios from 'axios'

export default {
    name: "Input",
    data() {
      return {
        uploadedImage: ""
      };
    },
    methods: {
      onFileChange(e){
        const files = e.target.files || e.dataTransfer.files;
        this.createImage(files[0]);
        this.img = files[0]
        this.img_name = files[0].name;
        this.blob = URL.createObjectURL(files[0].data)
        console.log(files[0]);
        this.$emit("FileNameSent", files[0].name)
      },
      createImage(file) {
        const reader = new FileReader();
        reader.onload = e => {
          this.uploadedImage = e.target.result;
        };
        reader.readAsDataURL(file);
        },
      remove() {
        this.uploadedImage = false;
      },
      PostImage (file) {
        axios.post('http://127.0.0.1:5000/image',{

            up_img: this.blob,
            header: {'Content-Type': 'multipart/form-data' }
        })
        .then((response) =>  {console.log(response)})
        }
    },
    props:{
        file_name: String
      },
    components: {
    }
}
</script>

<style>
</style>

