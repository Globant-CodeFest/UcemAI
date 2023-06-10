<template>
  <div>
    <AlertHelp></AlertHelp>
    <Temps></Temps>
  </div>
</template>

<script>
import AlertHelp from "@/components/Alert";
import Temps from "@/components/Temps";

export default {
  name: "HomePageView",
  components: {Temps, AlertHelp}

}
</script>

<style scoped>

</style>