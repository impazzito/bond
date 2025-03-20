<template>
  <div class="justify-center flex bg-yellow-300 items-center h-screen">
    <div class="text-4xl">
      Hello Vue 3 + Tailwind CSS
      <pre>{{ data }}</pre>
      <input type="text" v-model="input" @keyup.enter="submit()">
      <button @click="submit()">submit</button>
      <RouterView />
    </div>
  </div>
</template>


<script setup>
import api_call from '@/utils/api_call.js';
import { RouterLink, RouterView } from 'vue-router'
import { onMounted,ref } from 'vue'

const data = ref([])
const input = ref('ciao')


async function submit()  {
  console.log('click')
  for await (const response of api_call('/chat')) {
      data.value.push(response)
  }
}

onMounted(() => submit())

</script>
