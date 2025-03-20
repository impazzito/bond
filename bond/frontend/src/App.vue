<template>
    <div class="bg-gray-100 h-screen flex flex-col">
        <!-- Empty space for chat messages -->

        <div class="flex-grow overflow-y-auto p-4 space-y-4" ref="panel">
            <template :id="id" v-for="(block, id) in blocks">
                <template :id="id" v-for="(messages, type) in block">
                    <component :is="type" :messages="messages" />
                </template>
                <hr />
            </template>
        </div>

        <form
            @submit.prevent="submit"
            class="w-full bg-white border-t border-gray-300 p-4 flex items-center"
        >
            <input
                placeholder="Type something..."
                class="w-full px-3 py-2 rounded-lg bg-white dark:bg-zinc-900 border dark:border-zinc-800 text-sm text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 transition-all duration-200 focus:outline-hidden focus:ring-2 focus:ring-indigo-500/20 border-indigo-500"
                type="text"
                v-model="input"
                ref="field"
            />
            <select
                v-model="api"
                class="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
            >
                <option value="/chat">Chat</option>
                <option value="/python">Python</option>
            </select>
            <button
                class="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
                Send
            </button>
        </form>
    </div>
</template>

<script setup>
import api_call from "@/utils/api_call";
import ChatResponse from "@/blocks/ChatResponse.vue";
import ProcessStdout from "@/blocks/ProcessStdout.vue";
import ProcessExit from "@/blocks/ProcessExit.vue";
import ProcessStderr from "@/blocks/ProcessStderr.vue";
import UserInput from "@/blocks/UserInput.vue";
import { RouterLink, RouterView } from "vue-router";
import { onMounted, ref, nextTick, defineOptions } from "vue";
import uuid from "@/utils/uuid";

defineOptions({
    components: {
        ChatResponse,
        ProcessStdout,
        ProcessStderr,
        UserInput,
        ProcessExit,
    },
});

const messages = ref([]);
const field = ref(null);
const panel = ref(null);
const input = ref("ciao");
const api = ref("/chat");

const blocks = ref({});

async function push_api(api, payload, ...args) {
    const current = {};

    blocks.value[uuid()] = current;

    // messages.value.push({ api, ...payload });

    for await (const response of api_call(api, payload, ...args)) {
        if (!current[response.type]) current[response.type] = [];

        current[response.type].push(response);

        nextTick(() =>
            panel.value.scrollTo({
                top: panel.value.scrollHeight,
                behavior: "smooth",
            }),
        );
    }
}

onMounted(async () => {
    field.value.focus();

    push_api("/process", {
        bin: "/bin/sh",
        args: ["-c", 'for i in 1 2 3 4; do echo "Message $i"; sleep 0.1; done'],
    });

    setTimeout(
        () =>
            push_api("/python", {
                text: "import django; print(django.VERSION)",
                dependencies: ["django"],
            }),
        1000,
    );
});

const submit = async () => {
    push_api(api.value, { text: input.value });
};
</script>
