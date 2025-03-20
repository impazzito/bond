<template>
    <pre>{{ messages }}</pre>
</template>
<script setup>
import { defineOptions } from "vue";
import Mixin from "@/blocks/Mixin.vue";

defineOptions({
    mixins: [Mixin],
});
</script>
