<template>
  <div>
    <article class="message m-6">
      <div class="message-header">
        <p>Recomendaciones</p>
        <button class="delete" aria-label="delete"></button>
      </div>
      <div class="message-body">
        {{message}}
      </div>
    </article>

  </div>
</template>

<script>
export default {
  name: "TipsHelpView",
  data() {
    return {
      message: "Don't drive in or through flooded areas or standing water—cars or other vehicles won't protect you from floodwaters. They can be swept away or may stall in moving water. Do not drink flood water, or use it to wash dishes, brush teeth, or wash or prepare food. Drink clean, safe water."
    }
  }
}
</script>

<style scoped>

</style>