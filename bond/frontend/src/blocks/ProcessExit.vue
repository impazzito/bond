<template>
    {{ messages[0].code == 0 ? "👍 Success" : "⚠️ Error" }}
</template>
<script setup>
import { defineOptions } from "vue";
import Mixin from "@/blocks/Mixin.vue";

defineOptions({
    mixins: [Mixin],
});
</script>
