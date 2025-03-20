<template>
<div class="bg-gray-100 h-screen flex flex-col">
    <div class="flex-grow"></div> <!-- Empty space for chat messages -->

    <div class="flex-grow overflow-y-auto p-4 space-y-4">
        <div v-for="message in data" class="bg-white p-3 rounded-lg shadow-md w-max ">{{ message }}</div>

    </div>

    <form @submit.prevent=submit class="fixed bottom-0 left-0 w-full bg-white border-t border-gray-300 p-4 flex items-center">
        <input type="text" placeholder="Type a message..." class="flex-grow px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
        <button class="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">Send</button>
    </form>
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

</script>
