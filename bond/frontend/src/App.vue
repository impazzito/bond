
<template>
  <h1>hello {{data}}</h1>
  <input type="text" v-model="inputData" @keyup.enter="submit()">
  <button @click="submit()">submit</button>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

import { onMounted,ref } from 'vue'

const data = ref()
const inputData = ref()
const connection = new WebSocket("ws://localhost:8500/ws")


function submit()  {
  console.log('click')
  connection.send(inputData.value)
}

onMounted(() => {

  connection.onmessage = e=>{

    data.value = e.data

  }

})

</script>


<style scoped></style>
