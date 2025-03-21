<template>
    <header>
        <nav>
            <ul>
                <li><strong>Chat app</strong></li>
            </ul>
            <ul>
                <li><a href="#" class="contrast">About</a></li>
                <li><a href="#" class="contrast">Services</a></li>
                <li><a href="#" class="contrast">Products</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <pre v-for="msg in messages">{{ msg }}</pre>
    </main>
    <footer>
        <form
            @submit.prevent="submit"
            class="w-full bg-white border-t border-gray-300 p-4 flex items-center"
        >
            <textarea
                placeholder="Type something..."
                type="text"
                v-model="input"
                ref="field"
            />
            <fieldset class="grid">
                <select v-model="api">
                    <option value="/chat">Chat</option>
                    <option value="/python">Python</option>
                </select>
                <button>Send</button>
            </fieldset>
        </form>
    </footer>
</template>

<script setup>
import api_call from "@/utils/api_call.js";
import { RouterLink, RouterView } from "vue-router";
import { onMounted, ref, nextTick } from "vue";

import ChatResponse from "@/blocks/ChatResponse.vue";
import ProcessStdout from "@/blocks/ProcessStdout.vue";
import ProcessExit from "@/blocks/ProcessExit.vue";
import ProcessStderr from "@/blocks/ProcessStderr.vue";
import UserInput from "@/blocks/UserInput.vue";

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

async function push_api(api, payload, ...args) {
    messages.value.push({ api, ...payload });

    for await (const response of api_call(api, payload, ...args)) {
        messages.value.push(response);

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

async function submit() {
    console.log("submit");

    push_api(api.value, { text: input.value });
}
</script>
