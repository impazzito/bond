<template>
    <pre><template v-for="(message, index) in messages" :key="index"
            >{{ message.text }}</template></pre>
</template>

<script setup>
import { defineOptions } from "vue";
import Mixin from "@/blocks/Mixin.vue";

defineOptions({
    mixins: [Mixin],
});
</script>
