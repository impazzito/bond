<template>
    <div class="bg-gray-100 h-screen flex flex-col">
        <div class="flex-grow"></div>
        <!-- Empty space for chat messages -->

        <div class="flex-grow overflow-y-auto p-4 space-y-4">
            <div
                v-for="msg in messages"
                class="p-3 rounded-lg shadow-md w-max"
                :class="{
                    'bg-blue-500 text-white': msg.user,
                    'bg-white': !msg.user,
                }"
            >
                {{ msg }}
            </div>
        </div>

        <form
            @submit.prevent="submit"
            class="fixed bottom-0 left-0 w-full bg-white border-t border-gray-300 p-4 flex items-center"
        >
            <input
                placeholder="Type something..."
                class="w-full px-3 py-2 rounded-lg bg-white dark:bg-zinc-900 border dark:border-zinc-800 text-sm text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 transition-all duration-200 focus:outline-hidden focus:ring-2 focus:ring-indigo-500/20 border-indigo-500"
                type="text"
                v-model="input"
                ref="field"
            />
            <button
                class="ml-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            >
                Send
            </button>
        </form>
    </div>
</template>

<script setup>
import api_call from "@/utils/api_call.js";
import { RouterLink, RouterView } from "vue-router";
import { onMounted, ref } from "vue";

const messages = ref([]);
const field = ref(null);
const input = ref("ciao");

async function push_api(...args) {
    for await (const response of api_call(...args)) {
        messages.value.push(response);
    }
}

onMounted(async () => {
    field.value.focus();

    push_api(
        "/process",
        {
            bin: "/bin/sh",
            args: [
                "-c",
                'for i in 1 2 3 4; do echo "Message $i"; sleep 0.1; done',
            ],
        },
        "sleep",
    );

    push_api(
        "/python",
        {
            text: "import django; print(django.VERSION)",
            dependencies: ["django"],
        },
        "python",
    );
});

async function submit() {
    console.log("submit");
    messages.value.push({ text: input.value, user: true });

    push_api("/chat", { text: input.value }, "chat");
}
</script>
